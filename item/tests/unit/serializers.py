from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from item.serializers import (
	Category as Category_serializer,
	Category_nested as Category_nested_serializer,
	Item as Item_serializer )
from item.factories import (
	Item as Item_factory,
	Category as Category_factory )
from item.models import (
	Category as Category_model,
	Item as Item_model )
from users.factories import User_factory
from system.exceptions import Http_code_error
from unittest.mock import patch, MagicMock

class Test_category( TestCase ):
	"""
	"""
	def test_create( self ):
		owner = User_factory.build()
		category = Category_factory.build()
		data = Category_serializer( category ).data
		category_result = Category_serializer( data=data )
		is_valid = category_result.is_valid()
		self.assertTrue( is_valid, category_result.errors )
		category = category_result.save( owner=owner )
		self.assertTrue( isinstance( category, Category_model ) )
		self.assertEqual( category.owner.username, owner.username )
	
	def test_create_no_send_owner( self ):
		"""
		Cuano no se manda el owner de la categorua deberia de fallar
		con una exception de KeyError porque los datos no traiana
		el owner
		"""
		category = Category_factory.build()
		data = Category_serializer( category ).data
		category_result = Category_serializer( data=data )
		is_valid = category_result.is_valid()
		self.assertTrue( is_valid, category_result.errors )
		with self.assertRaises( KeyError ):
			category_result.save()
	
	def test_update( self ):
		category = Category_factory.build()
		data = Category_serializer( category ).data
		category_result = Category_serializer( category, data=data )
		is_valid = category_result.is_valid()
		self.assertTrue( is_valid, category_result.errors )
		category = category_result.save()
		self.assertTrue( isinstance( category, Category_model ) )

class Test_cateogory_nested( TestCase ):

	def test_validate( self ):
		category = Category_factory.build()
		data = Category_nested_serializer( category ).data
		result = Category_nested_serializer( data=data )
		is_valid = result.is_valid()
		self.assertTrue( is_valid, result.errors )

class Test_item( TestCase ):

	@patch( "item.models.Category.objects.get" )
	def test_create( self, category_get ):
		category = Category_factory.build()
		category_get.return_value = category
		category = Category_serializer( category ).data
		item = Item_factory.build()
		data = Item_serializer( item ).data
		result = Item_serializer( data=data )
		is_valid = result.is_valid()
		self.assertTrue( is_valid, result.errors )
		item = result.save( category=category )
		self.assertTrue( isinstance( item, Item_model ) )
		self.assertEqual( category[ 'name' ], item.category.name )
		category_get.assert_called_with( **category )

	@patch( 'item.models.Category.objects.get' )
	def test_create_new_category( self, category_get ):
		category_get.side_effect = Category_model.DoesNotExist
		owner = User_factory.build()
		category = Category_factory.build()
		category = Category_serializer( category ).data
		category.pop( 'owner' )
		item = Item_factory.build()
		data = Item_serializer( item ).data
		result = Item_serializer( data=data )
		is_valid = result.is_valid()
		self.assertTrue( is_valid, result.errors )
		item = result.save( category=category, owner=owner )
		self.assertTrue( isinstance( item, Item_model ) )
