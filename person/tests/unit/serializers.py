from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from users.tests import get_user_test_with_token
from person.serializers import ( Address_country_serializer,
	Address_serializer, Person_serializer, Country_serializer )
from person.factories import ( Address_factory,
	Country_factory, Person_factory )
from person.models import Address, Person, Country
from system.exceptions import Http_code_error

class Test_person_serializer( TestCase ):
	"""
	"""
	def test_create( self ):
		person = Person_factory.build()

		serializer = Person_serializer( person )
		serializer = Person_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		person_result = serializer.save()
		for field in person._meta.get_all_field_names():
			if field != 'address' and field != 'seller' and field != 'payer':
				self.assertEqual( getattr( person_result, field ),
					getattr( person, field ) )

	@patch( "person.models.Person.save" )
	def test_update( self, *args ):
		person = Person_factory.build()

		serializer = Person_serializer( person )
		serializer = Person_serializer( person, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		person_result = serializer.save()
		for field in person._meta.get_all_field_names():
			if field != 'address' and field != 'seller' and field != 'payer':
				self.assertEqual( getattr( person_result, field ),
					getattr( person, field ) )

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

	def test_create( self ):
		country = Country_factory.build()

		serializer = Country_serializer( country )
		serializer = Country_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		country_result = serializer.save()
		self.assertEqual( country_result.pk, country.pk )
		self.assertEqual( country_result.iso, country.iso )
		self.assertEqual( country_result.name, country.name)

	@patch( "person.models.Country.save" )
	def test_update( self, *args ):
		country = Country_factory.build()

		serializer = Country_serializer( country )
		serializer = Country_serializer( country, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		country_result = serializer.save()
		self.assertEqual( country_result.pk, country.pk )
		self.assertEqual( country_result.iso, country.iso )
		self.assertEqual( country_result.name, country.name)

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

	@patch( "person.models.Country.objects.get" )
	def test_create_address_by_pk( self, country_get ):
		address = Address_factory.build()
		address.country = Country( pk=100 )
		country_get.return_value = Country( pk=100, iso='qwe' )

		serializer = Address_serializer( address )
		serializer = Address_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		address_result = serializer.save()
		self.assertEqual( address.pk, address_result.pk )
		self.assertEqual( address.description, address_result.description )
		self.assertEqual( address.street, address_result.street )
		self.assertEqual( address.external_number, address_result.external_number )
		self.assertEqual( address.internal_number, address_result.internal_number )
		self.assertEqual( address.neighbour, address_result.neighbour )
		self.assertEqual( address.city, address_result.city )
		self.assertEqual( address.state, address_result.state )
		self.assertEqual( address.zipcode, address_result.zipcode )
		self.assertEqual( address.address_type, address_result.address_type )

		self.assertEqual( address_result.country.pk, country_get.return_value.pk )
		self.assertEqual( address_result.country.iso, country_get.return_value.iso )

	@patch( "person.models.Country.objects.get" )
	def test_create_address_by_pk_doest_not_exist( self, country_get ):
		address = Address_factory.build()
		address.country = Country( pk=100 )
		country_get.side_effect = Country.DoesNotExist

		serializer = Address_serializer( address )
		serializer = Address_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		with self.assertRaises( Http_code_error ):
			serializer.save()

	@patch( "person.models.Country.objects.get" )
	def test_create_address_by_iso( self, country_get ):
		address = Address_factory.build()
		address.country = Country( iso='ttt' )
		country_get.return_value = Country( pk=100, iso='ttt' )

		serializer = Address_serializer( address )
		serializer = Address_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		address_result = serializer.save()
		self.assertEqual( address.pk, address_result.pk )
		self.assertEqual( address.description, address_result.description )
		self.assertEqual( address.street, address_result.street )
		self.assertEqual( address.external_number, address_result.external_number )
		self.assertEqual( address.internal_number, address_result.internal_number )
		self.assertEqual( address.neighbour, address_result.neighbour )
		self.assertEqual( address.city, address_result.city )
		self.assertEqual( address.state, address_result.state )
		self.assertEqual( address.zipcode, address_result.zipcode )
		self.assertEqual( address.address_type, address_result.address_type )

		self.assertEqual( address_result.country.pk, country_get.return_value.pk )
		self.assertEqual( address_result.country.iso, country_get.return_value.iso )

	@patch( "person.models.Country.objects.get" )
	def test_create_address_by_iso_doest_not_exist( self, country_get ):
		address = Address_factory.build()
		address.country = Country( iso='ttt' )
		country_get.side_effect = Country.DoesNotExist

		serializer = Address_serializer( address )
		serializer = Address_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		with self.assertRaises( Http_code_error ):
			serializer.save()

	@patch( "person.models.Country.objects.get" )
	@patch( "person.models.Address.save" )
	def test_update_country_pk( self, address_save, country_get):
		address = Address_factory.build()
		address.country = Country( pk=100 )
		country_get.return_value = Country( pk=100, iso='ttt' )

		serializer = Address_serializer( address )
		serializer = Address_serializer( address, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		address_result = serializer.save()

		self.assertEqual( address.description, address_result.description )
		self.assertEqual( address.street, address_result.street )
		self.assertEqual( address.external_number, address_result.external_number )
		self.assertEqual( address.internal_number, address_result.internal_number )
		self.assertEqual( address.neighbour, address_result.neighbour )
		self.assertEqual( address.city, address_result.city )
		self.assertEqual( address.state, address_result.state )
		self.assertEqual( address.zipcode, address_result.zipcode )
		self.assertEqual( address.address_type, address_result.address_type )

	@patch( "person.models.Country.objects.get" )
	@patch( "person.models.Address.save" )
	def test_update_country_iso( self, address_save, country_get):
		address = Address_factory.build()
		address.country = Country( iso='ttt' )
		country_get.return_value = Country( pk=100, iso='ttt' )

		serializer = Address_serializer( address )
		serializer = Address_serializer( address, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		address_result = serializer.save()

		self.assertEqual( address.description, address_result.description )
		self.assertEqual( address.street, address_result.street )
		self.assertEqual( address.external_number, address_result.external_number )
		self.assertEqual( address.internal_number, address_result.internal_number )
		self.assertEqual( address.neighbour, address_result.neighbour )
		self.assertEqual( address.city, address_result.city )
		self.assertEqual( address.state, address_result.state )
		self.assertEqual( address.zipcode, address_result.zipcode )
		self.assertEqual( address.address_type, address_result.address_type )

	@patch( "person.models.Country.objects.get" )
	@patch( "person.models.Address.save" )
	def test_update_country_pk_not_found( self, address_save, country_get):
		address = Address_factory.build()
		address.country = Country( pk=100 )
		country_get.side_effect = Country.DoesNotExist

		serializer = Address_serializer( address )
		serializer = Address_serializer( address, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		with self.assertRaises( Http_code_error ):
			serializer.save()

	@patch( "person.models.Country.objects.get" )
	@patch( "person.models.Address.save" )
	def test_update_country_iso( self, address_save, country_get):
		address = Address_factory.build()
		address.country = Country( iso='ttt' )
		country_get.side_effect = Country.DoesNotExist

		serializer = Address_serializer( address )
		serializer = Address_serializer( address, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		with self.assertRaises( Http_code_error ):
			serializer.save()
