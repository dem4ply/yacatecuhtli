from django.db import models
from person.models import Country

class Currency( models.Model ):
	iso = models.CharField( max_length=3, unique=True )
	name = models.CharField( max_length=64 )

class Bank( models.Model ):
	name = models.CharField( max_length=64 )
	ssl_img = models.CharField( max_length=64 )
	country = models.ForeignKey( Country )
