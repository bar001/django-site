from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
   	url(r'^/CreateEquipment$', views.createEquip, name='newEquip'),
	url(r'^/Equipments$', views.equipments, name='equipments'),
	url(r'^/CreateBrand$', views.createBrand, name='newBrand'),
	url(r'^/Brands$', views.brands, name='brands'),
	url(r'^$', views.index, name='index'),
	]