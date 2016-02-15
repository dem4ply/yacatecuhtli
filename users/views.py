# vim: set fileencoding=utf-8 :
from django.utils.translation import ugettext as _
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (
	User_login as User_login_serializer,
	User as User_serializer )
from .models import User as User_model

from django.contrib.auth import authenticate
from rest_framework.decorators import detail_route, list_route
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from system.exceptions import Http_code_error

class User( viewsets.ModelViewSet ):
	"""
	CRUD para los usuarios
	"""
	#permission_classes = ( IsAuthenticated, )
	serializer_class = User_serializer
	queryset = User_model.objects.all()

	@list_route( methods=[ 'post' ], url_path='login',
		permission_classes=[ AllowAny ], authentication_classes=[ AllowAny ] )
	def login( self, request, format=None ):
		data = User_login_serializer( data=request.data )
		data.is_valid( raise_exception=True )
		user = authenticate( **data.data )
		if user:
			if user.is_active:
				return Response( User_serializer( user ).data )
			else:
				raise Http_code_error( status.HTTP_404_NOT_FOUND,
					_( "El usuario esta desactivado" ) )
		raise Http_code_error( status.HTTP_404_NOT_FOUND,
			_( "No se encontro el usuario" ) )

	
	@authentication_classes( ( AllowAny, ) )
	@permission_classes( ( AllowAny, ) )
	def create( self, request, format=None ):
		data = User_serializer( data=request.data )
		data.is_valid( raise_exception=True )
		user = data.save()
		user.save()
		return Response( User_serializer( user ).data,
			status=status.HTTP_201_CREATED )
