
from userinfo.models import UserInfo
from .serializer import UserInfoSerializer

from rest_framework import  generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import  viewsets
from rest_framework import  mixins
# cbv开发模型


class UserInfoPagination(PageNumberPagination):
    page_size = 1
    # 每页查询数量
    page_size_query_param = "pageSize"
    # 查询页数
    page_query_param = "pageNum"
    max_page_size = 10


class UserInfoListView(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    用户列表页
    """
    queryset=UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    pagination_class = UserInfoPagination


