from django.contrib import admin
from mysite.models import Post,Type

class PostAdmin(admin.ModelAdmin):
    list_display = ('year','title', 'body', 'pub_date')

admin.site.register(Post, PostAdmin)

#class YearAdmin(admin.ModelAdmin):
 #   list_display = ('year', 'area')

#admin.site.register(Year, YearAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('年度','地區','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')

admin.site.register(Type, TypeAdmin)


# Register your models here.
