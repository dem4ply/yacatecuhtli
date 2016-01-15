# vim: set fileencoding=utf-8 :
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ( Country_serializer, Address_serializer,
	Person_serializer )
from .models import Country, Person, Address

class Country_view( viewsets.ModelViewSet ):
	"""
	CRUD para los paises
	"""
	authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Country_serializer
	queryset = Country.objects.all()

class Address_view( viewsets.ModelViewSet ):
	"""
	CRUD para las direciones
	"""
	authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Address_serializer
	queryset = Address.objects.all()

class Person_view( viewsets.ModelViewSet ):
	"""
	CRUD para las personas
	"""
	authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Person_serializer
	queryset = Person.objects.all()
