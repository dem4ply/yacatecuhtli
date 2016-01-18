from django.db import models

class Currency( models.Model ):
	iso = models.CharField( max_length=3, unique=True )
	name = models.CharField( max_length=64 )
