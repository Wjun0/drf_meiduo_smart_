1. 用户部分-省市区三级联动(地区信息视图集使用)

   ```http
   GET /areas/: 获取所有省级地区的数据
   GET /areas/(?P<pk>\d+)/: 获取指定地区的数据
   
   视图集对象action属性:
   	重写get_serializer_class和get_queryset，根据不同的操作返回不同的序列化器类和不同的查询集。
   ```

2. 用户部分-省市区三级联动(网站优化-数据缓存介绍)

   ```http
   概念:
   	对于经常被用户所使用的数据，为了提升网站的性能，可以将这些数据存放到缓存中，当用户来访问的时候，直接从缓存中获取数据进行返回；只有缓存中不存在的时间再去查询数据库。
   ```

3. 用户部分-省市区三级联动(网站优化-地区数据的缓存)

   ```http
   GET /areas/
   GET /areas/(?P<pk>\d+)/
   
   缓存设置获取扩展包：drf-extensions
   
   装饰器：
   cache_response：
   	当客户端来访问时，先到缓存中获取对应的数据，如果获取到则直接进行返回；如果获取不到就会调用API代码，并且在返回响应之前会先将响应数据在缓存中进行存储。
   	
   	@cache_response()
   	def get(self, request):
   		pass
   	
   注意：继承CacheResponseMixin时需要放在ReadOnlyModelViewSet类的前面。
   ```

4. 用户部分-地址管理(地址模型类创建&用户默认地址字段添加)

   ```http
   一对一关系：
   	一个用户只有一个默认地址，一个默认地址一定只对应一个用户。
   	models.OneToOneField('模型类', ...)
   ```

   | id(用户id) | ...  | default_address_id(默认地址id) |
   | ---------- | ---- | ------------------------------ |
   | 2          |      | 3                              |
   |            |      |                                |
   |            |      |                                |

   ```python
   # 一对多
   class BookInfo(...):
   	pass
   	
   class HeroInfo(...):
   	hbook = models.ForeignKey(BookInfo, ...)
   
   # 查询和图书对象关联的英雄(由1查多)
   book.heroinfo_set.all()
   
   # 查询和英雄对象关联的图书(由多查1)
   hero.hbook
   
   # 一对一
   class User(...):
   	default_address = models.OneToOneField(Address, ..., related_name='addr_user')
   
   class Address(...):
   	pass
   	
   # 查询和用户对象关联的默认地址
   user.default_address
   
   # 查询和默认地址关联的用户
   default_address.addr_user
   ```

5. 用户部分-地址管理(地址新增-API接口设计与实现)

   ```http
   API接口设计:
   	POST /addresses/
   	参数:
   		通过请求头传递jwt token
   		{
   			"title": "地址标题",
               "reciver": "收货人",
               "province_id": "省id",
               "city_id": "市id",
               "district_id": "区县id",
               "place": "详细地址",
               "mobile": "手机号",
               "tel": "固定电话", # 可以不传
               "email": "邮箱" # 可以不传
   		}
   	响应:
   		{
   			"id": "地址id",
   			"title": "地址标题",
               "reciver": "收货人",
               "province_id": "省id",
               "city_id": "市id",
               "district_id": "区县id",
               "place": "详细地址",
               "mobile": "手机号",
               "tel": "固定电话",
               "email": "邮箱",
               "province": "省名称",
               "city": "市名称",
               "district": "区县名称",
   		}
   		
   # 地址数量上限判断
   
   <序列化器类对象>.context['request']：获取request对象
   ```

6. 用户部分-地址管理(地址新增-前端vue逻辑)

7. 用户部分-地址管理(查询|删除|修改)

8. 用户部分-地址管理(设为默认|修改地址标题)

9. 商品部分-商品数据表设计(广告分类表和广告内容表)

10. 商品部分-商品数据表设计(商品分类表和商品频道表)

11. 商品部分-商品数据表设计(SPU和SKU概念)

12. 商品部分-商品数据表设计(商品信息关键表设计)

13. 商品部分-商品数据表设计(商品其他数据表说明)

14. 商品部分-商品模型类的定义&表创建

15. 商品部分-FDFS文件存储系统(介绍&amp;上传文件流程)

16. 商品部分-Docker(介绍&安装&启动&停止)

17. 商品部分-Docker(镜像image操作)

18. 商品部分-Docker(容器container操作)

    

    

    

    

    

    

    

    

