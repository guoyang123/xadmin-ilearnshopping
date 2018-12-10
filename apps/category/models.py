from datetime import datetime
from django.db import models

# Create your models here.


class Category(models.Model):

    parent_id = models.IntegerField(default=0, verbose_name="父类id")
    name = models.CharField(default="", max_length=50, verbose_name="类别名称", help_text="类别名称")
    status = models.IntegerField(default=1, verbose_name="类别状态")
    sort_order = models.IntegerField(default=0, verbose_name="排序")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="修改时间")

    class Meta:
        verbose_name = "品类列表"
        verbose_name_plural = verbose_name
        db_table = "neuedu_category"

    def __str__(self):
        return self.name



