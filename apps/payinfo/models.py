from datetime import datetime
from django.db import models
# Create your models here.


class PayInfo(models.Model):
    """
    商品状态
    """
    PAY_PLATFOMR = (
        (1, "支付宝"),
        (2, "微信"),
    )
    """
    商品
    """
    user_id = models.IntegerField(verbose_name="用户id")
    order_no = models.IntegerField(verbose_name="订单号")
    pay_platform = models.IntegerField(choices=PAY_PLATFOMR, verbose_name="支付平台", help_text="支付平台")
    platform_number=models.CharField(default="", verbose_name="流水号",max_length=200)
    platform_status=models.CharField(default="", verbose_name="支付状态",max_length=20)
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = '支付列表'
        verbose_name_plural = verbose_name
        db_table="neuedu_payinfo"







