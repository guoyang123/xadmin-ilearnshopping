import xadmin
from .models import Category


class CategoryAdmin(object):

    # 定义后台列表显示字段
    list_display = ['id','name', 'parent_id', 'status', 'create_time','update_time']
    # 定义搜索字段
    search_fields = ['name', 'parent_id','status']
    # 定义过滤字段
    list_filter =['name', 'parent_id','status']
    # 定义列表页可编辑字段
    list_editable=['name','parent_id','status']
    # 页面自动刷新
    #refresh_times=[3,5]


xadmin.site.register(Category, CategoryAdmin)





