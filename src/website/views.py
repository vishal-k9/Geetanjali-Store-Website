# from django.shortcuts import render
from __future__ import unicode_literals

from products.models import Product

# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from django.db import connection

import MySQLdb


# hostname = 'localhost'
# username = 'root'
# password = 'boss'
# database = 'geetanjali_store_rawsql'

# conn = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )

def admin_func(request):
	return redirect('/admin')


# Create your views here.
def home_page(request):
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

    
	# cur = conn.cursor()
	# cur.execute( "SELECT * FROM product_products" )
	# queryset_list=cur.fetchall()#.order_by("-updated")
	# cur.close()
	# cur=connection.cursor()
	# cur.execute( "SELECT * FROM products_product" )
	# queryset_list=cur.fetchall()
	# cur.close()

	queryset_list=Product.objects.raw('SELECT * FROM products_product')#.order_by("-updated")
	cat1=Product.objects.raw('SELECT * FROM products_product as p where p.category="Biscuit and Snacks" ')
	cat2=Product.objects.all().raw('SELECT * FROM products_product as p where p.category="Groceries" ')
	cat3=Product.objects.all().raw('SELECT * FROM products_product as p where p.category="Plastic Ware" ')
	cat4=Product.objects.raw('SELECT * FROM products_product as p where p.category="Personal Care" ')
	
	paginator = Paginator(list(queryset_list), 2) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	# for obj in queryset:
	# 	print obj[3]	
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
	return render(request,"index.html",context)


# conn.close()

