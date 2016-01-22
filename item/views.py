# vim: set fileencoding=utf-8 :
from .models import Item, Category
from .serializers import Item_serializer, Category_serializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import list_route
from django.shortcuts import get_object_or_404
from system.exceptions import Http_code_error

class Item_view( viewsets.ModelViewSet ):
	"""
	CRUD para los items
	"""
	#authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Item_serializer
	queryset = Item.objects.all()

	def create( self, request, pk, category_pk=None, format=None ):
		if category_pk:
			try:
				category = Category.objects.get( pk=category_pk )
			except Category.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la categoria con el id %d" )\
						% ( category_pk ) )
		else:
			category = None

		serializer = Item_serializer( data=request.data )
		serializer.is_valid( raise_exception=True )
		item = serializer.save()
		item.save()
		if category:
			category.items.add( item )
		return Response( item, status=status.HTTP_201_CREATED )

	def list( self, request, category_pk=None, format=None ):
		if category_pk:
			try:
				category = Category.objects.get( pk=category_pk )
				items = category.items.all()
			except Category.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la categoria con el id %d" )\
						% ( category_pk ) )
		else:
			items = self.get_queryset()
		return Response( Item_serializer( items ).data, status=status.HTTP_200_OK )

	def retrieve( self, request, pk, category_pk=None, format=None ):
		if category_pk:
			try:
				category = Category.objects.get( pk=category_pk )
				item = get_object_or_404( category.items.all(), pk=pk )
			except Category.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la categoria con el id %d" )\
						% ( category_pk ) )
		else:
			item = get_object_or_404( self.get_queryset(), pk=pk )
		return Response( Item_serializer( item ).data, status=status.HTTP_200_OK )

	def update( self, request, pk, category_pk=None, format=None ):
		if category_pk:
			try:
				category = Category.objects.get( pk=category_pk )
				item = get_object_or_404( category.items.all(), pk=pk )
			except Category.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la categoria con el id %d" )\
						% ( category_pk ) )
		else:
			item = get_object_or_404( self.get_queryset(), pk=pk )
		serializer = Item_serializer( item, data=request.data )
		item = serializer.save()
		return Response( serializer.data, status=status.HTTP_200_OK )


	def destroy( self, request, pk, category_pk=None, format=None ):
		if category_pk:
			try:
				category = Category.objects.get( pk=category_pk )
				item = get_object_or_404( category.items.all(), pk=pk )
			except Category.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la categoria con el id %d" )\
						% ( category_pk ) )
		else:
			item = get_object_or_404( self.get_queryset(), pk=pk )
		item.delete()
		return Response( status=status.HTTP_204_NO_CONTENT )

class Category_view( viewsets.ModelViewSet ):
	"""
	CRUD para los items
	"""
	#authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Category_serializer
	queryset = Category.objects.all()
