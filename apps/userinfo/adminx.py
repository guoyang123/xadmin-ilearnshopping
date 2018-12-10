import xadmin
from .models import UserInfo
from xadmin import views


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "睿乐Go后台管理系统"  # 设置站点标题
    site_footer = "华北区TTC讲师团队"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


class UserInfoAdmin(object):

    # 定义后台列表显示字段
    list_display = ['id','username', 'email', 'phone', 'question', 'answer','update_time']
    # 定义搜索字段
    search_fields = ['username', 'phone']
    # 定义过滤字段
    list_filter = ['username', 'email', 'phone', 'question']
    # 定义列表页可编辑字段
    #list_editable=['name','click_num']
    # 页面自动刷新
    #refresh_times=[3,5]
    #model_icon="fa address-book"

xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)




