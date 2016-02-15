from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from person.serializers import (
	Country as Country_serializer,
	Country_nested as Country_nested_serializer,
	Address as Address_serializer,
	Person as Person_serializer )
from person.factories import (
	Country as Country_factory,
	Address as Address_factory,
	Person as Person_factory )
from person.models import (
	Country as Country_model,
	Person as Person_model,
	Address as Address_model )
from system.exceptions import Http_code_error
from unittest.mock import patch, MagicMock

class Test_country( TestCase ):
	"""
	"""
	def test_create( self ):
		country = Country_factory.build()
		serializer = Country_serializer( country )
		data = serializer.data
		serializer = Country_serializer( data=data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		country_result = serializer.save()
		self.assertTrue( isinstance( country_result, Country_model ) )

class Test_country_nested( TestCase ):
	"""
	"""
	@patch( 'person.models.Country.objects.filter' )
	def test_validate( self, country_nested_filter ):
		exists = MagicMock()
		exists.exists.return_value = True
		country_nested_filter.return_value = exists
		country = Country_factory.build()
		serializer = Country_nested_serializer( country )
		data = serializer.data
		serializer = Country_nested_serializer( data=data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )

	@patch( 'person.models.Country.objects.filter' )
	def test_validate_fail( self, country_nested_filter ):
		"""
		Prueba para cuando el pais no existe en la base de datos
		deberia de regresar el serializar no deberia de ser valido
		"""
		exists = MagicMock()
		exists.exists.return_value = False
		country_nested_filter.return_value = exists
		country = Country_factory.build()
		serializer = Country_nested_serializer( country )
		data = serializer.data
		serializer = Country_nested_serializer( data=data )
		is_valid = serializer.is_valid()
		self.assertFalse( is_valid, "deberia de regresar el error que no existe"
			" en el iso en la base de datos" )

class Test_person_serializer( TestCase ):
	def test_create( self ):
		person = Person_factory.build()

		serializer = Person_serializer( person )
		data = serializer.data
		serializer = Person_serializer( data=data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		person_result = serializer.save()
		self.assertTrue( isinstance( person_result, Person_model ) )

	def test_update( self, *args ):
		person = Person_factory.build()

		serializer = Person_serializer( person )
		serializer = Person_serializer( person, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		person_result = serializer.save()
		self.assertTrue( isinstance( person_result, Person_model ) )

class Test_address_serializer( APITestCase ):

	@patch( "person.models.Country.objects.get" )
	@patch( 'person.models.Country.objects.filter' )
	def test_create( self, country_nested_filter, country_get ):
		exists = MagicMock()
		exists.exists.return_value = True
		country_nested_filter.return_value = exists
		country_get.return_value = Country_model( iso='ttt' )

		address = Address_factory.build()
		address.country = Country_model( iso='ttt' )

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

		self.assertEqual( address_result.country.iso, country_get.return_value.iso )

	@patch( "person.models.Country.objects.get" )
	@patch( 'person.models.Country.objects.filter' )
	def test_create_country_not_exists( self, country_nested_filter, country_get ):
		exists = MagicMock()
		exists.exists.return_value = False
		country_nested_filter.return_value = exists
		country_get.return_value = Country_model( iso='ttt' )

		address = Address_factory.build()
		address.country = Country_model( iso='ttt' )

		serializer = Address_serializer( address )
		serializer = Address_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertFalse( is_valid, serializer.errors )
		self.assertEqual( serializer.errors['country']['iso'],
			["No se encontro el pais con el iso 'ttt'"] )

	@patch( "person.models.Country.objects.get" )
	@patch( 'person.models.Country.objects.filter' )
	def test_update_country( self, country_nested_filter, country_get ):
		exists = MagicMock()
		exists.exists.return_value = True
		country_nested_filter.return_value = exists
		country_get.return_value = Country_model( iso='tex' )

		address = Address_factory.build()
		address.country = Country_model( iso='ttt' )

		serializer = Address_serializer( address )
		data = serializer.data
		data[ 'country' ] = { 'iso': 'tex' }
		serializer = Address_serializer( address,  data=data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		address_result = serializer.save()
		self.assertEqual( address_result.country.iso, country_get.return_value.iso )

	@patch( "person.models.Country.objects.get" )
	@patch( 'person.models.Country.objects.filter' )
	def test_update_country_not_exists( self, country_nested_filter, country_get ):
		exists = MagicMock()
		exists.exists.return_value = False
		country_nested_filter.return_value = exists
		country_get.return_value = Country_model( iso='tex' )

		address = Address_factory.build()
		address.country = Country_model( iso='ttt' )

		serializer = Address_serializer( address )
		data = serializer.data
		data[ 'country' ] = { 'iso': 'tex' }
		serializer = Address_serializer( address,  data=data )
		is_valid = serializer.is_valid()
		self.assertFalse( is_valid, serializer.errors )
		self.assertEqual( serializer.errors['country']['iso'],
			["No se encontro el pais con el iso 'tex'"] )
