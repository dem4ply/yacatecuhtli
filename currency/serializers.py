from django.utils.translation import ugettext as _
from .models import Currency, Bank
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error
from person.serializers import Address_country_serializer as Bank_country_serializer
from person.models import Country

class Currency_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Currency
		fields = '__all__'
		read_only_fields = ( 'pk', )

	def create( self, validate_currency ):
		return Currency( **validate_currency )
	
	def update( self, instance, validate_currency ):
		instance.name = validate_currency.get( 'name', instance.name )
		instance.iso= validate_currency.get( 'iso', instance.iso )

		instance.save()
		return instance

class Bank_serializer( serializers.ModelSerializer ):
	country = Bank_country_serializer()

	class Meta:
		model = Bank
		fields = '__all__'
		read_only_fields = ( 'pk', )

	def create( self, validate_bank ):
		country = validate_bank.pop( 'country' )
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
		return Bank( country=country, **validate_bank )
	
	def update( self, instance, validate_bank ):
		country = validate_bank.pop( 'country' )
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
		instance.name = validate_bank.get( 'name', instance.name )
		instance.ssl_img = validate_bank.get( 'ssl_img', instance.ssl_img )

		instance.save()
		return instance
