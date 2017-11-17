# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q



def product_detail(request,slug=None): #retrieve
	#instance = Post.objects.get(id=1)
	cat_list=(
	'Cleaning Accessories' ,
	'Plastic Ware',
	'Electrical',
	'Stationary',
	'Utensils',
	'Biscuit and Snacks',
	'Cereals and Grains',
	'Groceries',
	'Personal Care',
	'Beverages',
	'Bags ',
	'Others'
	)

	brand_list=(
	'Patanjali',
	'Haldiram',
	'HUL',
	'Nestle',
	'Dabur',
	'ITC',
	'Others'
	)
	instance = get_object_or_404(Product, slug=slug)
	context = {
		# "title": instance.title,
		"instance": instance,
		"cat_list": cat_list,
		"brand_list": brand_list
	}
	return render(request, "product-details.html", context)

def product_list(request):
	cat_list=(
	'Cleaning Accessories' ,
	'Plastic Ware',
	'Electrical',
	'Stationary',
	'Utensils',
	'Biscuit and Snacks',
	'Cereals and Grains',
	'Groceries',
	'Personal Care',
	'Beverages',
	'Bags ',
	'Others'
	)

	brand_list=(
	'Patanjali',
	'Haldiram',
	'HUL',
	'Nestle',
	'Dabur',
	'ITC',
	'Others'
	)
	queryset_list=Product.objects.all()
	sql_q= "SELECT * FROM products_product "
	sql_q2=""
	# queryset_list=Product.objects.raw('SELECT * FROM products_product')#.order_by("-updated")
	cat1=Product.objects.raw('SELECT * FROM products_product as p where p.category="Biscuit and Snacks" ')
	cat2=Product.objects.all().raw('SELECT * FROM products_product as p where p.category="Groceries" ')
	cat3=Product.objects.all().raw('SELECT * FROM products_product as p where p.category="Plastic Ware" ')
	cat4=Product.objects.raw('SELECT * FROM products_product as p where p.category="Personal Care" ')
	
	query=request.GET.get('q')
	cat=request.GET.get('cat')
	brand=request.GET.get('b')
	if query:
		# django Q lookups
		sql_q2+=" where (lower(name) LIKE '%%"+query+"%%' OR "
		sql_q2+="lower(description) LIKE '%%"+query+"%%' OR "
		sql_q2+="lower(category) LIKE '%%"+query+"%%' OR "
		sql_q2+="lower(brand) LIKE '%%"+query+"%%') "
		# queryset_list = queryset_list.filter(
		# 		Q(name__icontains=query)|
		# 		Q(description__icontains=query)|
		# 		Q(category__icontains=query) |
		# 		Q(brand__icontains=query)
		# 		).distinct() # no duplicates
		# queryset_list= Product.objects.raw('SELECT * FROM queryset_list where name="abc" ')
	if cat:
		# django Q lookups
		if sql_q2=="":
			sql_q2+="where (lower(category)='"+cat+"') "
		else:
			sql_q2+="and (lower(category)='"+cat+"') "	
		# queryset_list = queryset_list.filter(
		# 		Q(category__icontains=cat)
		# 		).distinct()

	if brand:
		# django Q lookups
		if sql_q2=="":
			sql_q2+="where (lower(brand)='"+brand+"') "
		else:
			sql_q2+="and (lower(brand)='"+brand+"') "
		# queryset_list = queryset_list.filter(
		# 		Q(brand__icontains=brand)
		# 		).distinct()	
	# print queryset_list.query	

	sql_q+=sql_q2
	print sql_q
	queryset_list=Product.objects.raw(sql_q)

	paginator = Paginator(list(queryset_list), 2) # Show 12 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context={
		"object_list":queryset,
		"cat_list": cat_list,
		"brand_list": brand_list,
		"all_object_list": queryset_list,
		"cat1":cat1,
		"cat2":cat2,
		"cat3":cat3,
		"cat4":cat4

	}
	return render(request,"shop.html",context)





