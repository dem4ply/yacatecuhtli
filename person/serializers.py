from .models import Person, Country, Address
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error
from django.db.models import Q

class Country_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Country
		fields = ( '__all__' )
		read_only_fields = ( 'pk' )

	def create( self, validate_country ):
		return Country( **validate_country )

	def update( self, instance, validate_country ):
		instance.iso = validate_country.get( 'iso', instance.iso )
		instance.name = validate_country.get( 'name', instance.name )

		instance.save()
		return instance

class Country_nested_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Country
		fields = ( 'pk', 'iso', 'name', )
		read_only_fields = ( 'name', )

	def validate( self, data ):
		pk = data.get( 'pk', 0 )
		iso = data.get( 'iso', '' )
		if int( pk ) > 0 or iso != '':
			country = Country.objects.filter( Q( pk=pk ) | Q( iso=iso ) ):
			if country.exists():
				return data
			else:
				raise serializers.ValidationError(
					"No se encontro el pais en la base de datos"
				)
				
		raise serializers.ValidationError(
			"Se debe de mandar almenos un parametro pk o iso"
		)
	
class Address_serializer( serializers.ModelSerializer ):
	country = Country_nested_serializer()

	class Meta:
		model = Address
		fields = ( '__all__' )
		read_only_fields = ( 'pk', 'person' )

	def create( self, validate_data ):
		country = validate_address.pop( 'country' )
		country = Country.objects.get( **country )
		address = Address( **validate_data )
		address.country = country
		
		return address

	def update( self, instance, validate_address ):
		country = validate_address.pop( 'country' )
		country = Country.objects.get( **country )

		instance.description = validate_address.get( 'description',
			instance.description )
		instance.street = validate_address.get( 'street',
			instance.street )
		instance.external_number = validate_address.get( 'external_number',
			instance.external_number )
		instance.internal_number = validate_address.get( 'internal_number',
			instance.internal_number )
		instance.neighbour = validate_address.get( 'neighbour',
			instance.neighbour )
		instance.city = validate_address.get( 'city', instance.city )
		instance.state = validate_address.get( 'state', instance.state )
		instance.zipcode = validate_address.get( 'zipcode',
			instance.zipcode )

		instance.save()
		return instance

class Person_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Person
		fields = '__all__'
		read_only_fields = ( 'pk', )

	def create( self, validate_person ):
		return Person( **validate_person )
	
	def update( self, instance, validate_person ):
		instance.name = validate_person.get( 'name', instance.name )
		instance.last_name = validate_person.get( 'last_name', instance.last_name )
		instance.dni = validate_person.get( 'dni', instance.dni )
		instance.email = validate_person.get( 'email', instance.email )
		instance.status = validate_person.get( 'status', instance.status )

		instance.save()
		return instance
