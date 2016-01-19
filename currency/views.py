# vim: set fileencoding=utf-8 :
from .models import Currency, Bank
from .serializers import Currency_serializer, Bank_serializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class Currency_view( viewsets.ModelViewSet ):
	"""
	CRUD para la moneda
	"""
	authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Currency_serializer
	queryset = Currency.objects.all()

class Bank_view( viewsets.ModelViewSet ):
	"""
	CRUD para la moneda
	"""
	authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Bank_serializer
	queryset = Bank.objects.all()
