from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from users.tests import get_user_test_with_token
from person.serializers import ( Address_country_serializer,
	Address_serializer )
from person.factories import ( Address_factory,
	Country_factory, Person_factory )

class Test_address_country_serializer( APITestCase ):
	"""
	"""

	def test_validate_with_pk( self ):
		serializer = Address_country_serializer( data={ 'pk': 1, } )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )

	def test_validate_with_iso( self ):
		serializer = Address_country_serializer( data={ 'iso': 'iso', } )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )

	def test_validate_with_both( self ):
		serializer = Address_country_serializer( data={
			'pk': 1,
			'iso': 'iso',
		} )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )

	def test_validate_with_void( self ):
		serializer = Address_country_serializer( data={} )
		is_valid = serializer.is_valid()
		self.assertFalse( is_valid )

class Test_address_serializer( APITestCase ):
	"""
	"""

	@patch( "person.models.Country.objects.get" )
	def test_validate( self, country_get ):
		address = Address_factory.build()

		country_get.return_value = address.country

		serializer = Address_serializer( address )
		data = serializer.data
		serializer = Address_serializer( data=data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		serializer.save()
		country_get.assert_called_with( iso=address.country.iso )
