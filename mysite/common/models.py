from django.db import models

class Equipment(models.Model):
	count = models.IntegerField(default=0)
    name = models.CharField(max_lengh=255)
    price = models.DecimalField(default = 0)
    
    
class Brand(models.Model):
	name = models.CharField(max_lengh = 255)
   		
