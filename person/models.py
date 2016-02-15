from django.db import models

class Country( models.Model ):
	iso = models.CharField( max_length=3, primary_key=True )
	name = models.CharField( max_length=64 )

class Person( models.Model ):
	name = models.CharField( max_length=128 )
	last_name = models.CharField( max_length=128 )
	dni = models.CharField( max_length=128 )
	email = models.CharField( max_length=128 )
	status = models.BooleanField( default=True )


class Address( models.Model ):
	description = models.CharField( max_length=128 )
	street = models.CharField( max_length=128 )
	external_number = models.CharField( max_length=128 )
	internal_number = models.CharField( max_length=129, blank=True, default="" )
	neighbour = models.CharField( max_length=128 )
	city = models.CharField( max_length=128 )
	state = models.CharField( max_length=128 )
	zipcode = models.CharField( max_length=10 )
	address_type = models.CharField( max_length=10, default="1" )

	country = models.ForeignKey( Country, related_name='address' )
	person = models.ForeignKey( Person, related_name='address' )

