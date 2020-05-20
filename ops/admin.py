from django.contrib import admin
from .models import *
# Register your models here.
# 此处设置页面显示标题
admin.site.site_header = '集中化Websalt自动化运维'

# 此处设置页面头部标题
admin.site.site_title = '集中化Websalt自动化运维'

class IpaddrAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'pod', 'machina_type']
    list_filter = ['pod']
    search_fields = ['ip']

admin.site.register(Ipaddr, IpaddrAdmin)
admin.site.register(Os)
admin.site.register(MinionInfo)
admin.site.register(JobInfo)
