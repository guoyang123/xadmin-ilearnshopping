from datetime import datetime
from django.db import models


class UserInfo(models.Model):

    username = models.CharField(default="", max_length=50, verbose_name="用户名")
    password = models.CharField(default="", max_length=50, verbose_name="密码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    phone = models.CharField( max_length=11, verbose_name="移动电话")
    question = models.CharField(default="", max_length=100, verbose_name="问题")
    answer = models.CharField(default="", max_length=100, verbose_name="答案")
    role = models.IntegerField(default=1, verbose_name="用户角色")
    create_time=models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="修改时间")

    class Meta:
        verbose_name = "会员列表"
        verbose_name_plural = verbose_name
        db_table = "neuedu_user"

    def __str__(self):
        return self.username