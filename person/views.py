# vim: set fileencoding=utf-8 :
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ( Country_serializer, Address_serializer,
	Person_serializer )
from .models import Country, Person, Address

class Country_view( viewsets.ModelViewSet ):
	"""
	CRUD para los paises
	"""
	#authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Country_serializer
	queryset = Country.objects.all()

class Address_view( viewsets.ModelViewSet ):
	"""
	CRUD para las direciones
	"""
	#authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Address_serializer
	queryset = Address.objects.all()

	def list( self, request, person_pk=None, format=None ):
		if person_pk:
			try:
				address = Person.objects.get( pk=person_pk ).address
			except Person.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la persona" ) )
		else:
			address = self.get_queryset()
		return Address_serializer( address, many=True )

	def retrieve( self, request, pk, person_pk=None, format=None ):
		if person_pk:
			try:
				address = Person.objects.get( pk=person_pk ).address
			except Person.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la persona" ) )
		else:
			address = self.get_queryset()
		address = address.get( pk=pk )
		return Address_serializer( address )

	def create( self, request, person_pk=None, format=None ):
		serializer = Address_serializer( **request.data )
		serializer.is_valid( raise_exception=True )

		address = serializer.save()
		if person_pk:
			try:
				person = Person.objects.get( pk=person_pk )
				address.save()
				person.address.add( address )
			except Person.DoesNotExist:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la persona" ) )
		else:
			address.save()
		Response( Address_serializer( address ).data )
	
	def update( self, request, pk, person_pk=None, format=None ):
		if person_pk:
			try:
				address = Person.objects.get( pk=person_pk ).address
				address = address.get( pk=pk )
			except Person.DoesNotExit:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la persona" ) )
			except Address.DoesNotExit:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la direccion" ) )
		else:
			try:
				address = Address.objects.get( pk=pk )
			except Address.DoesNotExit:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "No se encontro la direccion" ) )
				
		serializer = Address_serializer( address, data=request.data )
		serializer.is_valid( raise_exception=True )
		address = serializer.save()
		Response( Address_serializer( address ).data )

class Person_view( viewsets.ModelViewSet ):
	"""
	CRUD para las personas
	"""
	#authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Person_serializer
	queryset = Person.objects.all()
