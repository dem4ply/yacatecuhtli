from django.db import models
from seller.models import Seller

class Category( models.Model ):
	name = models.CharField( max_length=128 )
	seller = models.ForeignKey( Seller )

class Item( models.Model ):
	name = models.CharField( max_length=128 )
	sku = models.CharField( max_length=64 )
	category = models.ForeignKey( Category )
