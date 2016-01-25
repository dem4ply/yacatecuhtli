from .models import User, Token
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error
from seller.serializers import Seller_serializer

class User_login_serializer( serializers.ModelSerializer ):
	username = serializers.CharField( max_length=64 )
	password = serializers.CharField( max_length=128 )
	class Meta:
		model = User
		fields = ( 'username', 'password' )

class Token_serializer( serializers.ModelSerializer ):
	class Meta:
		model = Token
		fields = ( 'public_key', 'private_key', 'test_public_key',
			'test_private_key' )

class User_serializer( serializers.ModelSerializer ):
	token = Token_serializer()
	seller = Seller_serializer()

	class Meta:
		model = User
		fields = ( 'username', 'email', 'token', 'seller' )
		only_read_field = ( 'pk' )
