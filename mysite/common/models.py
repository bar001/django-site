from django.db import models


class Brand(models.Model):
	name = models.CharField(max_length = 255)


class Equipment(models.Model):
	count = models.IntegerField(default=0)
	name = models.CharField(max_length=255)
	description = models.TextField(null = True, blank = True)
	price = models.DecimalField(default = 0, max_digits=2, decimal_places=2)
	brand = models.ForeignKey(Brand)	
    
    

   		
