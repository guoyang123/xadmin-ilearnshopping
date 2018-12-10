import xadmin
from .models import Order,NoPayOrder,CancelOrder,FinishOrder,SendOrder,PayOrder

class OrderRecordAdmin(object):

    # 定义后台列表显示字段
    list_display = ['order_no', 'status', 'user_id', 'shipping_id', 'payment','payment_time','create_time']
    # 定义搜索字段
    search_fields = ['order_no']
    # 定义过滤字段
    list_filter = ['order_no', 'status', 'user_id', 'shipping_id',]
    # 定义列表页可编辑字段
    list_editable=['status','update_time']
    # 页面自动刷新
    #refresh_times=[3,5]
    readonly_fields=['order_no', 'postage','payment_type','status', 'user_id', 'shipping_id', 'payment','create_time','update_time']
    exclude=['send_time','close_time','end_time','payment_time']


class NoPayOrderRecordAdmin(object):

    # 定义后台列表显示字段
    list_display = ['order_no', 'status', 'user_id', 'shipping_id', 'payment','payment_time','create_time']
    # 定义搜索字段
    search_fields = ['order_no']
    # 定义过滤字段
    list_filter = ['order_no', 'status', 'user_id', 'shipping_id',]
    # 定义列表页可编辑字段
    list_editable=['status','update_time']
    readonly_fields = ['order_no', 'postage', 'payment_type', 'status', 'user_id', 'shipping_id', 'payment',
                       'create_time', 'update_time']
    exclude = ['send_time', 'close_time', 'end_time', 'payment_time']

    def queryset(self):
            # 调用父类的queryset方法
           qs= super(NoPayOrderRecordAdmin,self).queryset()
           qs=qs.filter(status=10)
           return qs


class PayOrderRecordAdmin(object):

    # 定义后台列表显示字段
    list_display = ['order_no', 'status', 'user_id', 'shipping_id', 'payment','payment_time','create_time']
    # 定义搜索字段
    search_fields = ['order_no']
    # 定义过滤字段
    list_filter = ['order_no', 'status', 'user_id', 'shipping_id',]
    # 定义列表页可编辑字段
    list_editable=['status','update_time']
    readonly_fields = ['order_no', 'postage', 'payment_type', 'status', 'user_id', 'shipping_id', 'payment',
                       'create_time', 'payment_time']
    exclude = ['send_time', 'close_time', 'end_time', 'update_time']
    def queryset(self):
            # 调用父类的queryset方法
           qs= super(PayOrderRecordAdmin,self).queryset()
           qs=qs.filter(status=20)
           return qs


class CancelOrderRecordAdmin(object):
    # 定义后台列表显示字段
    list_display = ['order_no', 'status', 'user_id', 'shipping_id', 'payment', 'payment_time', 'create_time']
    # 定义搜索字段
    search_fields = ['order_no']
    # 定义过滤字段
    list_filter = ['order_no', 'status', 'user_id', 'shipping_id', ]
    # 定义列表页可编辑字段
    list_editable = ['status', 'update_time']
    readonly_fields = ['order_no', 'postage', 'payment_type', 'status', 'user_id', 'shipping_id', 'payment',
                       'create_time', 'close_time']
    exclude = ['send_time', 'payment_time', 'end_time', 'update_time']
    def queryset(self):
        # 调用父类的queryset方法
        qs = super(CancelOrderRecordAdmin, self).queryset()
        qs = qs.filter(status=0)
        return qs


class SendOrderRecordAdmin(object):
    # 定义后台列表显示字段
    list_display = ['order_no', 'status', 'user_id', 'shipping_id', 'payment', 'payment_time', 'create_time']
    # 定义搜索字段
    search_fields = ['order_no']
    # 定义过滤字段
    list_filter = ['order_no', 'status', 'user_id', 'shipping_id', ]
    # 定义列表页可编辑字段
    list_editable = ['status', 'update_time']
    readonly_fields = ['order_no', 'postage', 'payment_type', 'status', 'user_id', 'shipping_id', 'payment',
                       'create_time', 'send_time']
    exclude = ['close_time', 'payment_time', 'end_time', 'update_time']
    def queryset(self):
        # 调用父类的queryset方法
        qs = super(SendOrderRecordAdmin, self).queryset()
        qs = qs.filter(status=40)
        return qs


class FinishOrderRecordAdmin(object):
    # 定义后台列表显示字段
    list_display = ['order_no', 'status', 'user_id', 'shipping_id', 'payment', 'payment_time', 'create_time']
    # 定义搜索字段
    search_fields = ['order_no']
    # 定义过滤字段
    list_filter = ['order_no', 'status', 'user_id', 'shipping_id', ]
    # 定义列表页可编辑字段
    list_editable = ['status', 'update_time']
    readonly_fields = ['order_no', 'postage', 'payment_type', 'status', 'user_id', 'shipping_id', 'payment',
                       'create_time', 'end_time']
    exclude = ['close_time', 'payment_time', 'send_time', 'update_time']
    def queryset(self):
        # 调用父类的queryset方法
        qs = super(FinishOrderRecordAdmin, self).queryset()
        qs = qs.filter(status=50)
        return qs


xadmin.site.register(Order, OrderRecordAdmin)
xadmin.site.register(NoPayOrder, NoPayOrderRecordAdmin)
xadmin.site.register(PayOrder, PayOrderRecordAdmin)
xadmin.site.register(CancelOrder, CancelOrderRecordAdmin)
xadmin.site.register(SendOrder, SendOrderRecordAdmin)
xadmin.site.register(FinishOrder, FinishOrderRecordAdmin)


