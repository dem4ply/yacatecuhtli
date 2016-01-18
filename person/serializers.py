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
		read_only_fields = ( 'pk' )

	def create( self, validate_person ):
		return Person( **validate_person )

class Country_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Country
		fields = ( '__all__' )
		read_only_fields = ( 'pk' )

	def create( self, validate_country ):
		return Country( **validate_country )

class Address_country_serializer( Country_serializer ):
	iso = serializers.CharField( required=False, allow_null=True )
	pk = serializers.IntegerField( required=False, allow_null=True )

	class Meta( Country_serializer.Meta ):
		fields = ( 'pk', 'iso' )
		read_only_fields = None

	def validate( self, data ):
		"""
		revisa que almenos se haya mandado el iso o el pk
		"""
		if data.get( 'pk' ):
			return data
		elif ( data.get( 'iso' ) ):
			return data
		raise serializers.ValidationError( ( "Se debe de mandar "
			"almenos un parametro pk o iso" ) )

class Address_serializer( serializers.ModelSerializer ):
	country = Address_country_serializer()

	class Meta:
		model = Address
		fields = ( '__all__' )
		read_only_fields = ( 'pk', 'owner' )

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
