	# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse	
from django.db import models
import os
from django.db.models.signals import pre_save, post_save
from django.db.models.fields.files import ImageField
import base64
# from .storage import BlobStoreStorage

from django.utils.text import slugify

def upload_location(instance, filename):
	f,e=os.path.splitext(filename)
	# print ("%s/%s%s" %(instance.category, instance.name,e))
	return ("%s/%s%s" %(instance.category, instance.name,e))

CAT_CHOICES = (
    ('Cleaning Accessories','CLEANING ACCESSORIES'),
    ('Plastic Ware','PLASTIC WARE'),
    ('Electrical','ELECTRICAL '),
    ('Stationary','STATIONARY'),
    ('Utensils','UTENSILS '),
    ('Biscuit and Snacks','BISCUIT AND SNACKS '),
    ('Cereals and Grains','CEREALS AND GRAINS '),
    ('Groceries','GROCERIES '),
    ('Personal Care','PERSONAL CARE  '),
    ('Beverages','BEVERAGES '),
    ('Bags','BAGS '),
    ('Others','OTHERS'),
)

BRAND_CHOICES = (
    ('Patanjali','PATANJALI'),
    ('Haldiram', 'HALDIRAM'),
    ('HUL','HUL'),
    ('Nestle','NESTLE'),
    ('Dabur','DABUR'),
    ('ITC','ITC'),
    ('Others','OTHERS'),
)

# Create your models here.
class Product(models.Model):
	name=models.CharField(max_length=120)
	image=models.ImageField(upload_to=upload_location, null=True, blank=True)
	raw_image=models.BinaryField(null=True, blank=True)
	slug = models.SlugField(unique=True, null=True, blank=True)
	# quantity=models.IntegerField(default=0)
	# quantity=models.IntegerField(default=0)
	category=models.CharField(max_length=120, choices=CAT_CHOICES, default="Others")
	brand=models.CharField(max_length=120, choices=BRAND_CHOICES, default="Others")
	rate=models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	quantity=models.IntegerField(default=1)
	description=models.TextField(null=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("products:detail", kwargs={"slug":self.slug})

	# tell something more about the model	
	class Meta:
		ordering= ["-updated", "-timestamp"]

	def add_to_cart(self):
		return "%s?item=%s&qty=1" %(reverse("cart"), self.id)

	def remove_from_cart(self):
		return "%s?item=%s&qty=1&delete=True" %(reverse("cart"), self.id)

	def get_title(self):
		return "%s" %(self.name)

	def get_quantity(self):
		return "%d" %(self.quantity)
			
	def get_price(self):
		# if self.sale_price is not None:
		# 	return self.sale_price
		# else:
		return self.rate	


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

def post_save_product_receiver(sender, instance, *args, **kwargs):
	if not instance.raw_image:
		image = open("../media_cdn/"+str(instance.image), 'rb')
		image_read = image.read()
		image_64_encode = base64.encodestring(image_read)
		# image_64_decode = base64.decodestring(image_64_encode) 
		# print "hello"
		instance.raw_image = image_64_encode
		instance.save()
	# image_result = open('deer_decode.gif', 'wb') # create a writable image and write the decoding result
	# image_result.write(image_64_decode)
	



pre_save.connect(pre_save_product_receiver, sender=Product)
post_save.connect(post_save_product_receiver, sender=Product)
