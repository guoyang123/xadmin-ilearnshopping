import xadmin
from .models import Goods,GoodsCarousel
from datetime import  datetime
class GoodsRecordAdmin(object):


    # 定义后台列表显示字段
    list_display = ['id', 'name','main_image', 'price', 'stock','status','create_time','update_time']
    # 定义搜索字段
    search_fields = ['category_id', 'name', 'price']
    # 定义过滤字段
    list_filter = ['category_id', 'name', 'price', 'stock', 'status']
    # 定义列表页可编辑字段
    list_editable=['stock','status','update_time']
    # 页面自动刷新
    #refresh_times=[3,5]
    readonly_fields=['create_time','update_time']


class GoodsCasouelAdmin(object):

    # 定义后台列表显示字段
    list_display =['id', 'name', 'main_image', 'price', 'stock','status','create_time','update_time']
    # 定义搜索字段
    search_fields = ['category_id', 'name', 'price']
    # 定义过滤字段
    list_filter = ['category_id', 'name', 'price', 'stock', 'status']

    def queryset(self):
        # 调用父类的queryset方法
       qs= super(GoodsCasouelAdmin,self).queryset()
       qs=qs.filter(is_banner=True)
       return qs


xadmin.site.register(Goods, GoodsRecordAdmin)
xadmin.site.register(GoodsCarousel, GoodsCasouelAdmin)





