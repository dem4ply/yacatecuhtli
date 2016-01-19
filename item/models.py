from django.db import models

class Item( models.Model ):
	name = models.CharField( max_length=128 )
	sku = models.CharField( max_length=64 )

class Category( models.Model ):
	name = models.CharField( max_length=128 )
	items = models.ManyToManyField( Item )
