
from payinfo.models import PayInfo
from .serializers import PayInfoSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework import  viewsets
from rest_framework import  mixins
# cbv开发模型


class PayInfoPagination(PageNumberPagination):
    page_size = 1
    # 每页查询数量
    page_size_query_param = "pageSize"
    # 查询页数
    page_query_param = "pageNum"
    max_page_size = 20


class PayInfoListView(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    支付列表页
    """
    queryset=PayInfo.objects.all()
    serializer_class = PayInfoSerializer
    pagination_class = PayInfoPagination

