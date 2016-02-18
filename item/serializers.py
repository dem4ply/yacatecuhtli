from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error
from django.db.models import Q

from .models import (
	Category as Category_model,
	Item as Item_model )

class Category( serializers.ModelSerializer ):
	class Meta:
		model = Category_model
		fields = ( '__all__' )
		read_only_fields = ( 'owner', )
	
	def create( self, validate_data ):
		owner = validate_data.pop( 'owner' )
		category =  Category_model( **validate_data )
		category.owner = owner
		return category

	def update( self, instance, validate_data ):
		instance.name = validate_data.get( 'name', instance.name )
		instance.description = validate_data.get( 'description', instance.description )

		return instance

class Category_nested( Category ):

	class Meta:
		model = Category_model
		fields = ( 'pk', 'name', )
		read_only_fields = ( 'name', )

class Item( serializers.ModelSerializer ):
	category = Category_nested( required=False )

	class Meta:
		model = Item_model
		fields = ( '__all__' )
	
	def create( self, validate_data ):
		category = validate_data.pop( 'category' )
		try:
			category = Category_model.objects.get( **category )
		except Category_model.DoesNotExist:
			owner = validate_data.pop( 'owner' )
			category = Category_model( **category, owner=owner )
		item = Item_model( **validate_data )
		item.category = category
		return item

	def update( self, instance, validate_data ):
		instance.sku = validate_data.get( 'sku', instance.sku )
		instance.upc = validate_data.get( 'upc', instance.upc )
		instance.name = validate_data.get( 'name', instance.name )
		instance.description = validate_data.get( 'description', instance.description )
		instance.price = validate_data.get( 'price', instance.price )

		return instance
