"""ilearnshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path,include
import xadmin

from userinfo.views import UserInfoListView
from category.views import CategoryListView
from goods.views import GoodsListView
from  order.views import OrderListView
from payinfo.views import PayInfoListView
from  orderitem.views import OrderItemListView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
router=DefaultRouter()
# 配置goods的url
router.register(r"userinfo",UserInfoListView)
router.register(r"category",CategoryListView)
router.register(r"goods",GoodsListView)
router.register(r"order",OrderListView)
router.register(r"payinfo",PayInfoListView)
router.register(r"orderItem",OrderItemListView)
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^', include(router.urls)),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('simditor/', include('simditor.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
