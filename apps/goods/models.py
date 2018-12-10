from datetime import datetime
from django.db import models
from simditor.fields import RichTextField
from DjangoUeditor.models import UEditorField
from category.models import Category
# Create your models here.


class Goods(models.Model):
    """
    商品状态
    """
    GOODS_STATUS = (
        (1, "在售"),
        (2, "下架"),
        (3, "删除"),
    )
    """
    商品
    """
    category = models.ForeignKey(Category, verbose_name="商品类别",related_name="cates", on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100, verbose_name="商品名")
    subtitle = models.CharField(default="", verbose_name="商品子标题",max_length=200)
    main_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="商品主图")
    sub_images = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="商品子图")
    detail=RichTextField(verbose_name="详情内容",null=True,blank=True)
    # detail = UEditorField(verbose_name='商品详情', width=600, height=300, toolbars="full", imagePath="goods/ueditor/",
    #                        filePath="goods/ueditor/", upload_settings={"imageMaxSize": 1204000},
    #                       default='',null=True,blank=True)
    price = models.FloatField(default=0, verbose_name="商品价格")
    stock= models.IntegerField(default=0, verbose_name="商品库存")
    status= models.IntegerField(choices=GOODS_STATUS, verbose_name="商品状态", help_text="商品状态")

    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_banner = models.BooleanField(default=False, verbose_name="是否轮播")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")



    class Meta:
        verbose_name = '商品列表'
        verbose_name_plural = verbose_name
        db_table="neuedu_product"

    def __str__(self):
        return self.name


class GoodsCarousel(Goods):
    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name
        proxy = True  # 不会创建新的表







