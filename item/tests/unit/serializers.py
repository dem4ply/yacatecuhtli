from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from item.serializers import Item_serializer, Category_serializer
from item.factories import Item_factory, Category_factory
from system.exceptions import Http_code_error

class Test_Item_serializer( TestCase ):
	"""
	"""
	def test_create( self ):
		item = Item_factory.build()

		serializer = Item_serializer( item )
		serializer = Item_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		item_result = serializer.save()
		self.assertEqual( item.sku, item_result.sku )

	@patch( "item.models.Item.save" )
	def test_update( self, *args ):
		item = Item_factory.build()

		serializer = Item_serializer( item )
		serializer = Item_serializer( item, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		item_result = serializer.save()
		self.assertEqual( item.sku, item_result.sku )

class Test_category_serializer( TestCase ):
	"""
	"""
	def test_create( self ):
		category = Category_factory.build()

		serializer = Category_serializer( category )
		serializer = Category_serializer( data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		category_result = serializer.save()
		self.assertEqual( category.name, category_result.name )

	@patch( "item.models.Category.save" )
	def test_update( self, *args ):
		category = Category_factory.build()

		serializer = Category_serializer( category )
		serializer = Category_serializer( category, data=serializer.data )
		is_valid = serializer.is_valid()
		self.assertTrue( is_valid, serializer.errors )
		category_result = serializer.save()
		self.assertEqual( category.name, category_result.name )
