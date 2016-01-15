from django.utils.translation import ugettext as _
from rest_framework import serializers
from .models import Person, Country, Address

class Person_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Person
		fields = '__all__'
		read_only_fields = ( 'pk' )

class Country_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Country
		fields = '__all__'
		read_only_fields = ( 'pk' )

class Address_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Address
		fields = '__all__'
		read_only_fields = ( 'pk' )
