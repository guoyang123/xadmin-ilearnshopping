
from order.models import Order
from .serializers import OrderSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework import  viewsets
from rest_framework import  mixins
# cbv开发模型


class OrderPagination(PageNumberPagination):
    page_size = 1
    # 每页查询数量
    page_size_query_param = "pageSize"
    # 查询页数
    page_query_param = "pageNum"
    max_page_size = 20


class OrderListView(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    订单列表页
    """
    queryset=Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination

