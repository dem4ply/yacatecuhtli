from django.utils.translation import ugettext as _
from .models import Currency
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error

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
