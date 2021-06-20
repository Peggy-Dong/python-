from django.contrib import admin
from mysite.models import Post,Type,Paper,metal,glass,plastic,EA,textile,CS,oil,drug,battery,other

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

class metalAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(metal, metalAdmin)
# Register your models here.
class glassAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(glass, glassAdmin)
class plasticAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(plastic, plasticAdmin)
class EAAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(EA, EAAdmin)
class textileAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(textile, textileAdmin)
class CSAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(CS, CSAdmin)
class oilAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(oil, oilAdmin)
class drugAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(drug, drugAdmin)
class batteryAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(battery, batteryAdmin)

class otherAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(other, otherAdmin)