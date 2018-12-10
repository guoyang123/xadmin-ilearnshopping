
from goods.models import Goods,GoodsCarousel
from .serializers import GoodsSerializer,GoodsCarouselSerializer

from rest_framework import  generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import  viewsets
from rest_framework import  mixins
# cbv开发模型


class GoodsPagination(PageNumberPagination):
    page_size = 1
    # 每页查询数量
    page_size_query_param = "pageSize"
    # 查询页数
    page_query_param = "pageNum"
    max_page_size = 20


class GoodsListView(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    商品列表页
    """
    queryset=Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination


class GoodsCarouselListView(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    商品轮播列表页
    """
    queryset=GoodsCarousel.objects.all()
    serializer_class = GoodsCarouselSerializer
    pagination_class = GoodsPagination