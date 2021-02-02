from decimal import Decimal
from django.shortcuts import render
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from goods.models import SKU
from orders.serializers import OrderSKUSerializer, OrderSerializer


class OrderSettlementView(APIView):
    permission_classes = [IsAuthenticated]

    # GET /orders/settlement/
    def get(self, request):
        """
        获取订单结算商品的数据:
        1. 从redis中获取用户所要结算商品的sku_id和结算数量count
        2. 根据商品sku_id获取对应商品的数据&组织运费
        3. 将结算数据序列化并返回
        """
        # 1. 从redis中获取用户所要结算商品的sku_id和结算数量count
        # redis链接
        redis_conn = get_redis_connection('cart')

        # 从redis set中获取用户购物车中被勾选的商品的sku_id
        user = request.user
        cart_selected_key = 'cart_selected_%s' % user.id

        # Set(b'<sku_id>', b'<sku_id>', ...)
        sku_ids = redis_conn.smembers(cart_selected_key)

        # 从redis hash中获取用户购物车中所有商品的id和对应的数量count
        cart_key = 'cart_%s' % user.id
        # {
        #     b'<sku_id>': b'<count>',
        #     ...
        # }
        cart_redis = redis_conn.hgetall(cart_key)

        # 转换数据
        # {
        #     '<sku_id>': '<count>',
        #     ...
        # }
        cart_dict = {}

        for sku_id, count in cart_redis.items():
            cart_dict[int(sku_id)] = int(count)

        # 2. 根据商品sku_id获取对应商品的数据&组织运费
        skus = SKU.objects.filter(id__in=sku_ids)

        for sku in skus:
            # 给sku对象增加属性count，保存该商品所要结算的数量count
            sku.count = cart_dict[sku.id]

        # 运费
        freight = Decimal(10.0)

        # 3. 将结算数据序列化并返回
        serializer = OrderSKUSerializer(skus, many=True)

        response_data = {
            'freight': freight,
            'skus': serializer.data
        }
        return Response(response_data)


# POST /orders/
class OrdersView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def post(self, request):
        """
        订单数据保存(订单创建):
        1. 获取address和pay_method并进行校验(完整性，address是否存在，pay_method是否合法)
        2. 创建订单并保存订单数据
        3. 返回应答，订单创建成功
        """
        # 1. 获取address和pay_method并进行校验(完整性，address是否存在，pay_method是否合法)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. 创建订单并保存订单数据(create)
        serializer.save()

        # 3. 返回应答，订单创建成功
        return Response(serializer.data, status=status.HTTP_201_CREATED)
