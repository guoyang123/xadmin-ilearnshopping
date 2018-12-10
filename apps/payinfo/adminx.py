import xadmin
from .models import PayInfo


class PayInfoRecordAdmin(object):

    # 定义后台列表显示字段
    list_display = ['id','order_no',  'user_id', 'pay_platform','platform_number','platform_status','create_time']
    # 定义搜索字段
    search_fields = ['order_no','platform_number','pay_platform']
    # 定义过滤字段
    list_filter = ['order_no', 'platform_number', 'pay_platform', 'platform_status',]
    # 定义列表页可编辑字段
    #list_editable=['status','update_time']
    # 页面自动刷新
    #refresh_times=[3,5]


xadmin.site.register(PayInfo, PayInfoRecordAdmin)


