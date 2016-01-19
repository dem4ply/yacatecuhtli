from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from users.tests import get_user_test_with_token
from currency.serializers import Currency_serializer, Bank_serializer
from currency.factories import Currency_factory, Bank_factory
from system.exceptions import Http_code_error
from person.models import Country

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

class Test_bank_serializer( APITestCase ):
	"""
	"""

	@patch( "person.models.Country.objects.get" )
	def test_validate( self, country_get ):
		bank = Bank_factory.build()

		country_get.return_value = bank.country

		serializer = Bank_serializer( bank )
		data = serializer.data
		serializer = Bank_serializer( data=data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		serializer.save()
		country_get.assert_called_with( iso=bank.country.iso )

	@patch( "person.models.Country.objects.get" )
	def test_create_bank_by_pk( self, country_get ):
		bank = Bank_factory.build()
		bank.country = Country( pk=100 )
		country_get.return_value = Country( pk=100, iso='qwe' )

		serializer = Bank_serializer( bank )
		serializer = Bank_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		bank_result = serializer.save()
		self.assertEqual( bank.name, bank_result.name )
		self.assertEqual( bank.ssl_img, bank_result.ssl_img )

		self.assertEqual( bank_result.country.pk, country_get.return_value.pk )
		self.assertEqual( bank_result.country.iso, country_get.return_value.iso )

	@patch( "person.models.Country.objects.get" )
	def test_create_bank_by_pk_doest_not_exist( self, country_get ):
		bank = Bank_factory.build()
		bank.country = Country( pk=100 )
		country_get.side_effect = Country.DoesNotExist

		serializer = Bank_serializer( bank )
		serializer = Bank_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		with self.assertRaises( Http_code_error ):
			serializer.save()

	@patch( "person.models.Country.objects.get" )
	def test_create_bank_by_iso( self, country_get ):
		bank = Bank_factory.build()
		bank.country = Country( iso='ttt' )
		country_get.return_value = Country( pk=100, iso='ttt' )

		serializer = Bank_serializer( bank )
		serializer = Bank_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		bank_result = serializer.save()
		self.assertEqual( bank.name, bank_result.name )
		self.assertEqual( bank.ssl_img, bank_result.ssl_img )

		self.assertEqual( bank_result.country.pk, country_get.return_value.pk )
		self.assertEqual( bank_result.country.iso, country_get.return_value.iso )

	@patch( "person.models.Country.objects.get" )
	def test_create_bank_by_iso_doest_not_exist( self, country_get ):
		bank = Bank_factory.build()
		bank.country = Country( iso='ttt' )
		country_get.side_effect = Country.DoesNotExist

		serializer = Bank_serializer( bank )
		serializer = Bank_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		with self.assertRaises( Http_code_error ):
			serializer.save()

	@patch( "person.models.Country.objects.get" )
	@patch( "currency.models.Bank.save" )
	def test_update_country_pk( self, bank_save, country_get):
		bank = Bank_factory.build()
		bank.country = Country( pk=100 )
		country_get.return_value = Country( pk=100, iso='ttt' )

		serializer = Bank_serializer( bank )
		serializer = Bank_serializer( bank, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		bank_result = serializer.save()

		self.assertEqual( bank.name, bank_result.name )
		self.assertEqual( bank.ssl_img, bank_result.ssl_img )

	@patch( "person.models.Country.objects.get" )
	@patch( "currency.models.Bank.save" )
	def test_update_country_iso( self, bank_save, country_get):
		bank = Bank_factory.build()
		bank.country = Country( iso='ttt' )
		country_get.return_value = Country( pk=100, iso='ttt' )

		serializer = Bank_serializer( bank )
		serializer = Bank_serializer( bank, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		bank_result = serializer.save()

		self.assertEqual( bank.name, bank_result.name )
		self.assertEqual( bank.ssl_img, bank_result.ssl_img )

	@patch( "person.models.Country.objects.get" )
	@patch( "currency.models.Bank.save" )
	def test_update_country_pk_not_found( self, bank_save, country_get):
		bank = Bank_factory.build()
		bank.country = Country( pk=100 )
		country_get.side_effect = Country.DoesNotExist

		serializer = Bank_serializer( bank )
		serializer = Bank_serializer( bank, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		with self.assertRaises( Http_code_error ):
			serializer.save()

	@patch( "person.models.Country.objects.get" )
	@patch( "currency.models.Bank.save" )
	def test_update_country_iso( self, bank_save, country_get):
		bank = Bank_factory.build()
		bank.country = Country( iso='ttt' )
		country_get.side_effect = Country.DoesNotExist

		serializer = Bank_serializer( bank )
		serializer = Bank_serializer( bank, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		with self.assertRaises( Http_code_error ):
			serializer.save()
