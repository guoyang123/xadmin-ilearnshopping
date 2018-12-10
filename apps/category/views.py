
from category.models import Category
from .serializer import CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
# cbv开发模型


class CategoryPagination(PageNumberPagination):
    page_size = 1
    # 每页查询数量
    page_size_query_param = "pageSize"
    # 查询页数
    page_query_param = "pageNum"
    max_page_size = 10


class CategoryListView(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    类别列表页
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
