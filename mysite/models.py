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

#class Year(models.Model):
#	year = models.CharField(max_length=200)
#	area =models.CharField(max_length=200)
#	def __str__(self):
#		return self.name

class Type(models.Model):
	year = models.CharField(max_length=200)
	area =models.CharField(max_length=200)
	total = models.PositiveIntegerField(default=0)
	paper = models.PositiveIntegerField(default=0)
	metal = models.PositiveIntegerField(default=0)
	plastic= models.PositiveIntegerField(default=0)


	def __str__(self):
		return self.area


