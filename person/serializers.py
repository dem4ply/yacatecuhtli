from .models import (
	Person as Person_model,
	Country as Country_model,
	Address as Address_model )
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error
from django.db.models import Q

class Country( serializers.ModelSerializer ):
	class Meta:
		model = Country_model
		fields = ( '__all__' )

	def create( self, validate_data ):
		return Country_model( **validate_data )

	def update( self, instance, validate_data ):
		instance.iso = validate_data.get( 'iso', instance.iso )
		instance.name = validate_data.get( 'name', instance.name )

		return instance

class Country_nested( serializers.Serializer ):
	"""
	Este serializador se utiliza cuando se agrega anidado a otro serializador
	solo valida que el pais exista
	"""
	iso = serializers.CharField( max_length=3 )

	def validate_iso( self, iso ):
		country = Country_model.objects.filter( iso=iso )
		if country.exists():
			return iso
		else:
			raise serializers.ValidationError(
				_( "No se encontro el pais con el iso '%s'" ) % ( iso )
			)

class Person( serializers.ModelSerializer ):
	class Meta:
		model = Person_model
		fields = '__all__'
		read_only_fields = ( 'pk', )

	def create( self, validate_data ):
		return Person_model( **validate_data )
	
	def update( self, instance, validate_data ):
		instance.name = validate_data.get( 'name', instance.name )
		instance.last_name = validate_data.get( 'last_name', instance.last_name )
		instance.dni = validate_data.get( 'dni', instance.dni )
		instance.email = validate_data.get( 'email', instance.email )
		instance.status = validate_data.get( 'status', instance.status )

		return instance
	
class Address( serializers.ModelSerializer ):
	country = Country_nested()

	class Meta:
		model = Address_model
		fields = ( '__all__' )
		read_only_fields = ( 'pk', 'person' )

	def create( self, validate_data ):
		country = validate_data.pop( 'country' )
		country = Country_model.objects.get( **country )
		address = Address_model( **validate_data )
		address.country = country
		return address

	def update( self, instance, validate_data ):
		country = validate_data.pop( 'country' )
		if country:
			country = Country_model.objects.get( **country )
			instance.country = country

		instance.description = validate_data.get( 'description',
			instance.description )
		instance.street = validate_data.get( 'street',
			instance.street )
		instance.external_number = validate_data.get( 'external_number',
			instance.external_number )
		instance.internal_number = validate_data.get( 'internal_number',
			instance.internal_number )
		instance.neighbour = validate_data.get( 'neighbour',
			instance.neighbour )
		instance.city = validate_data.get( 'city', instance.city )
		instance.state = validate_data.get( 'state', instance.state )
		instance.zipcode = validate_data.get( 'zipcode',
			instance.zipcode )

		return instance
