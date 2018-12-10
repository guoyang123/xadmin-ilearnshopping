from django.db import models
from  datetime import  datetime
# Create your models here.


class Order(models.Model):
    PAYMENT_TYPE = (
        (1, "在线支付"),
    )

    ORDER_STATUS=(
        (0, "已取消"),
        (10, "未付款"),
        (20, "已付款"),
        (40, "已发货"),
        (50, "交易成功"),
        (60, "交易关闭"),
    )

    user_id = models.IntegerField(verbose_name="用户id")
    order_no = models.IntegerField(verbose_name="订单号")
    shipping_id=models.IntegerField(verbose_name="收货地址")
    payment= models.FloatField( verbose_name="实际付款金额")
    payment_type=models.IntegerField(choices=PAYMENT_TYPE,verbose_name="付款方式",help_text="付款方式")
    postage= models.IntegerField(default=0,verbose_name="运费")
    status= models.IntegerField(choices=ORDER_STATUS, verbose_name="订单状态", help_text="订单状态")
    payment_time = models.DateTimeField(default=datetime.now, verbose_name="付款时间")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发货时间")
    end_time = models.DateTimeField(default=datetime.now, verbose_name="交易完成时间")
    close_time = models.DateTimeField(default=datetime.now, verbose_name="交易关闭时间")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="下单时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name="订单列表"
        verbose_name_plural=verbose_name
        db_table="neuedu_order"


class NoPayOrder(Order):
    class Meta:
        verbose_name = "未付款订单"
        verbose_name_plural = verbose_name
        proxy = True  # 不会创建新的表


class PayOrder(Order):
    class Meta:
        verbose_name = "已付款订单"
        verbose_name_plural = verbose_name
        proxy = True  # 不会创建新的表


class SendOrder(Order):
    class Meta:
        verbose_name = "已发货订单"
        verbose_name_plural = verbose_name
        proxy = True  # 不会创建新的表


class CancelOrder(Order):
    class Meta:
        verbose_name = "已取消订单"
        verbose_name_plural = verbose_name
        proxy = True  # 不会创建新的表


class FinishOrder(Order):
    class Meta:
        verbose_name = "已完成订单"
        verbose_name_plural = verbose_name
        proxy = True  # 不会创建新的表