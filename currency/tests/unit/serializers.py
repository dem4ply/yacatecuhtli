from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from users.tests import get_user_test_with_token
from currency.serializers import Currency_serializer
from currency.factories import Currency_factory
from system.exceptions import Http_code_error

class Test_currency_serializer( TestCase ):
	"""
	"""
	def test_create( self ):
		currency = Currency_factory.build()

		serializer = Currency_serializer( currency )
		serializer = Currency_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		currency_result = serializer.save()
		self.assertEqual( currency.iso, currency_result.iso )
		self.assertEqual( currency.name, currency_result.name )

	@patch( "currency.models.Currency.save" )
	def test_update( self, *args ):
		currency = Currency_factory.build()

		serializer = Currency_serializer( currency )
		serializer = Currency_serializer( currency, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		currency_result = serializer.save()
		self.assertEqual( currency.iso, currency_result.iso )
		self.assertEqual( currency.name, currency_result.name )
