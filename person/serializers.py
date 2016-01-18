from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from .models import Person, Country, Address
from system.exceptions import Http_code_error
from django.utils.translation import ugettext as _

class Person_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Person
		fields = '__all__'
		read_only_fields = ( 'pk', 'address' )

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

class Address_country_serializer( Country_serializer ):
	iso = serializers.CharField( required=False, allow_null=True, allow_blank=True )
	pk = serializers.IntegerField( required=False, allow_null=True )

	class Meta( Country_serializer.Meta ):
		fields = ( 'pk', 'iso' )
		read_only_fields = None

	def validate( self, data ):
		"""
		revisa que almenos se haya mandado el iso o el pk
		"""
		pk = data.get( 'pk', 0 )
		iso = data.get( 'iso' )
		if pk and int( pk ) > 0:
			return data
		elif iso and iso != '':
			return data
		raise serializers.ValidationError( ( "Se debe de mandar "
			"almenos un parametro pk o iso" ) )

class Address_serializer( serializers.ModelSerializer ):
	country = Address_country_serializer()

	class Meta:
		model = Address
		fields = ( '__all__' )
		read_only_fields = ( 'pk' )

	def create( self, validate_address ):
		country = validate_address.pop( 'country' )
		pk = country.get( 'pk' )
		iso = country.get( 'iso' )
		if pk:
			try:
				country = Country.objects.get( pk=pk )
			except Country.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro el pais con el id %d" ) % ( pk ) )
		elif iso:
			try:
				country = Country.objects.get( iso=iso )
			except Country.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro el pais con el iso %s" ) % ( iso ) )
		else:
			raise Http_code_error( status.HTTP_400_BAD_REQUEST,
				_( "No se envio el pais" ) )

		address = Address( **validate_address )
		address.country = country
		
		return address

	def update( self, instance, validate_address ):
		country = validate_address.pop( 'country' )
		pk = country.get( 'pk' )
		iso = country.get( 'iso' )
		if pk:
			try:
				country = Country.objects.get( pk=pk )
				instance.country = country
			except Country.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro el pais con el id %d" ) % ( pk ) )
		elif iso:
			try:
				country = Country.objects.get( iso=iso )
				instance.country = country
			except Country.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro el pais con el iso %s" ) % ( iso ) )
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
		instance.address_type = validate_address.get( 'address_type',
			instance.address_type )

		instance.save()
		return instance
