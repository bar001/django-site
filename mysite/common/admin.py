from django.contrib import admin
from .models import Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields': ['name']})
	]
	list_display = ('name',)
	
	
admin.site.register(Brand, BrandAdmin)