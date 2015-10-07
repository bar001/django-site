from django.shortcuts import render
from . import models


def index(request):
	return render(request, 'index.html', {})


def equipments(request):
	equips = models.Equipment.objects.all()
	return render(request, 'common/equipments.html', {'equips': equips})


def brands(request):
	brands = models.Brand.objects.all()
	return render(request, 'common/brands.html', {'brands': brands})


def createEquip(request):
	return render(request, 'common/createEquip.html', {})


def createBrand(request):
	return render(request, 'common/createBrand.html', {})