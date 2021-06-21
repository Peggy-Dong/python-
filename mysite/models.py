from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    year = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Type(models.Model):
	年度 = models.CharField(max_length=200)
	地區 =models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Paper(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Metal(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Plastic(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Glass(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Textile(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區


class Ea(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Battery(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Cs(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Drug(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Oil(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Other(models.Model):
	地區 = models.CharField(max_length=200)
	民國100年 = models.PositiveIntegerField(default=0)
	民國101年 = models.PositiveIntegerField(default=0)
	民國102年 = models.PositiveIntegerField(default=0)
	民國103年 = models.PositiveIntegerField(default=0)
	民國104年 = models.PositiveIntegerField(default=0)
	民國105年 = models.PositiveIntegerField(default=0)
	民國106年 = models.PositiveIntegerField(default=0)
	民國107年 = models.PositiveIntegerField(default=0)
	民國108年 = models.PositiveIntegerField(default=0)
	民國109年 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.地區

class Yilan(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Keelung(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Taipei(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Newtaipei(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Taoyuan(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Hsinchu(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Hsinchuc(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Miaoli(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Taichung(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Changhua(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Nantou(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Yunlin(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Chiayi(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Chiayic(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Tainan(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Kaohsiung(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Pingtung(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Taitung(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Hualien(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度


class Penghu(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Kinmen(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度

class Renjiang(models.Model):
	年度 = models.CharField(max_length=200)
	總計 = models.PositiveIntegerField(default=0)
	紙類 = models.PositiveIntegerField(default=0)
	金屬類 = models.PositiveIntegerField(default=0)
	塑膠橡膠= models.PositiveIntegerField(default=0)
	玻璃 = models.PositiveIntegerField(default=0)
	紡織品 = models.PositiveIntegerField(default=0)
	家用電品 = models.PositiveIntegerField(default=0)
	電池 = models.PositiveIntegerField(default=0)
	通訊物品 = models.PositiveIntegerField(default=0)
	特殊用藥廢容器 = models.PositiveIntegerField(default=0)
	食用油 = models.PositiveIntegerField(default=0)
	其他 = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.年度