from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	#@daverobb2011
	class Meta:
		verbose_name_plural = 'categories'
		


class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.PositiveIntegerField() 
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	image = models.ImageField(upload_to='static/images')

	def __str__(self):
		return self.name