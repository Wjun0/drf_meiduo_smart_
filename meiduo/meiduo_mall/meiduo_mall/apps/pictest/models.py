from django.db import models

# Create your models here.


class PicTest(models.Model):
    """FDFS上传图片测试模型类"""
    image = models.ImageField(verbose_name='图片')

    class Meta:
        db_table = 'tb_pics'
        verbose_name = 'FDFS上传图片测试'
        verbose_name_plural = verbose_name

