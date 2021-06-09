from django.contrib import admin
from mysite.models import Post,Type

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pub_date')

admin.site.register(Post, PostAdmin)

#class YearAdmin(admin.ModelAdmin):
 #   list_display = ('year', 'area')

#admin.site.register(Year, YearAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('year','area','total', 'paper','metal','plastic')

admin.site.register(Type, TypeAdmin)


# Register your models here.
