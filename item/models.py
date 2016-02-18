from django.db import models
from django.core.validators import RegexValidator
from users.models import User as User_model

class Category( models.Model ):
	name        = models.CharField( max_length=64 )
	description = models.TextField( null=True, blank=True )
	owner       = models.ForeignKey( User_model )

class Item( models.Model ):
	numeric = RegexValidator(r'^[0-9]*$',
		message = "Only alphanumeric characters are allowed." )

	sku         = models.CharField( max_length=64 )
	upc         = models.CharField( max_length=13, validators=[ numeric ],
						null=True, blank=True )
	name        = models.CharField( max_length=64 )
	description = models.TextField( blank=True, null=True )
	price       = models.DecimalField( max_digits=14, decimal_places=4 )
	category    = models.ForeignKey( Category )
