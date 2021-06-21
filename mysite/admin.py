from django.contrib import admin
from mysite.models import Post,Type,Paper,Metal,Plastic,Glass,Textile,Ea,Battery,Cs,Drug,Oil,Other
from mysite.models import Yilan,Keelung,Taipei,Newtaipei,Taoyuan,Hsinchu,Hsinchuc
from mysite.models import Miaoli,Taichung,Changhua,Nantou,Yunlin
from mysite.models import Chiayi,Chiayic,Tainan,Kaohsiung,Pingtung
from mysite.models import Hualien,Taitung,Renjiang,Kinmen,Penghu
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

class MetalAdmin(admin.ModelAdmin):
	list_display = ('地區','民國100年','民國101年','民國102年','民國103年','民國104年','民國105年','民國106年','民國107年','民國108年','民國109年')

admin.site.register(Metal, MetalAdmin)

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

class YilanAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Yilan, YilanAdmin)

class KeelungAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Keelung, KeelungAdmin)

class TaipeiAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Taipei, TaipeiAdmin)

class NewtaipeiAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Newtaipei, NewtaipeiAdmin)

class TaoyuanAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Taoyuan, TaoyuanAdmin)

class HsinchuAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Hsinchu, HsinchuAdmin)

class HsinchucAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Hsinchuc, HsinchucAdmin)

class MiaoliAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Miaoli, MiaoliAdmin)

class TaichungAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Taichung, TaichungAdmin)

class ChanghuaAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Changhua, ChanghuaAdmin)

class NantouAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Nantou, NantouAdmin)

class YunlinAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Yunlin, YunlinAdmin)

class ChiayiAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Chiayi, ChiayiAdmin)

class ChiayicAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Chiayic, ChiayicAdmin)

class TainanAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Tainan, TainanAdmin)

class KaohsiungAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Kaohsiung, KaohsiungAdmin)

class PingtungAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Pingtung, PingtungAdmin)

class TaitungAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Taitung, TaitungAdmin)

class HualienAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Hualien, HualienAdmin)

class PenghuAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Penghu, PenghuAdmin)

class KinmenAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Kinmen, KinmenAdmin)

class RenjiangAdmin(admin.ModelAdmin):
	list_display = ('年度','總計', '紙類','金屬類','塑膠橡膠','玻璃','紡織品','家用電品','電池','通訊物品','特殊用藥廢容器','食用油','其他')
admin.site.register(Renjiang, RenjiangAdmin)