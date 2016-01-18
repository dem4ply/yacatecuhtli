# vim: set fileencoding=utf-8 :
from .models import Currency
from .serializers import Currency_serializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class Currency_view( viewsets.ModelViewSet ):
	"""
	CRUD para los paises
	"""
	authentication_classes = ( TokenAuthentication, )
	permission_classes = ( IsAuthenticated, )
	serializer_class = Currency_serializer
	queryset = Currency.objects.all()