from django.utils.translation import ugettext as _
from .models import Item, Category
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error

class Item_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Item
		fields = '__all__'
		read_only_fields = ( 'pk', )

	def create( self, validate_item ):
		return Item( **validate_item )
	
	def update( self, instance, validate_item ):
		instance.name = validate_item.get( 'name', instance.name )
		instance.iso= validate_item.get( 'sku', instance.sku )

		instance.save()
		return instance

class Category_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Category
		fields = '__all__'
		read_only_fields = ( 'pk', 'items' )

	def create( self, validate_category ):
		return Category( **validate_category )
	
	def update( self, instance, validate_category ):
		instance.name = validate_category.get( 'name', instance.name )

		instance.save()
		return instance
