import xadmin
from .models import OrderItem


class OrderItemRecordAdmin(object):

    # 定义后台列表显示字段
    list_display = ['order_no', 'product_name', 'user_id', 'product_name', 'current_unit_price','quantity','total_price']
    # 定义搜索字段
    search_fields = ['order_no','user_id']
    # 定义过滤字段
    list_filter = ['order_no']
    # 定义列表页可编辑字段
  #  list_editable=['status','update_time']
    # 页面自动刷新
    #refresh_times=[3,5]
    readonly_fields= ['order_no', 'product_name', 'product_id','product_image','user_id',  'current_unit_price','quantity','total_price','create_time','update_time']

  #  exclude=['send_time','close_time','end_time','payment_time']


xadmin.site.register(OrderItem, OrderItemRecordAdmin)


