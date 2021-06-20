from django.contrib import admin
from mysite.models import Post,Type,Paper,Paper1,Plastic,Glass,Textile,Ea,Battery,Cs,Drug,Oil,Other

class PostAdmin(admin.ModelAdmin):
	list_display = ('year','title', 'body', 'pub_date')

admin.site.register(Post, PostAdmin)

#class YearAdmin(admin.ModelAdmin):
 #   list_display = ('year', 'area')

#admin.site.register(Year, YearAdmin)

class TypeAdmin(admin.ModelAdmin):
	list_display = ('年度','地區','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')

admin.site.register(Type, TypeAdmin)

class PaperAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Paper, PaperAdmin)

class Paper1Admin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Paper1, Paper1Admin)

class PlasticAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Plastic, PlasticAdmin)


class GlassAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Glass, GlassAdmin)

class TextileAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Textile, TextileAdmin)

class EaAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Ea, EaAdmin)

class BatteryAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Battery, BatteryAdmin)

class CsAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Cs, CsAdmin)

class DrugAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Drug, DrugAdmin)


class OilAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Oil, OilAdmin)


class OtherAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Other, OtherAdmin)