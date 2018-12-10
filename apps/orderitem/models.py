from django.db import models
from datetime import  datetime
from goods.models import Goods
# Create your models here.


class OrderItem(models.Model):
    user_id = models.IntegerField(verbose_name="用户id")
    order_no = models.IntegerField(verbose_name="订单号")
    product_id = models.IntegerField(verbose_name="商品id")
    product_name=models.CharField(default='',max_length=100,verbose_name="商品名称")
    product_image=models.CharField(default='',max_length=500,verbose_name="商品图片")
    current_unit_price= models.FloatField(verbose_name="实际金额")
    quantity=models.IntegerField(verbose_name="商品数量")
    total_price=models.IntegerField(verbose_name="商品总价")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name="订单明细"
        verbose_name_plural=verbose_name
        db_table="neuedu_order_item"
