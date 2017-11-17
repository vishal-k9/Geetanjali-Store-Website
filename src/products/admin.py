# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["name", "updated", "timestamp"]
	list_display_links = ["name"]
	# list_editable = ["name"]
	list_filter = ["category", "brand"]

	search_fields = ["name", "description"]
	class Meta:
		model = Product


admin.site.register(Product,ProductModelAdmin)
