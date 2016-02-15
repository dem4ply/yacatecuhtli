from .models import User as User_model, Token as Token_model
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error

class User_login( serializers.ModelSerializer ):
	username = serializers.CharField( max_length=64 )
	password = serializers.CharField( max_length=128 )
	class Meta:
		model = User_model
		fields = ( 'username', 'password' )

class Token( serializers.ModelSerializer ):
	class Meta:
		model = Token_model
		fields = ( 'public_key', 'private_key', 'test_public_key',
			'test_private_key' )

class User( serializers.ModelSerializer ):
	token = Token( required=False )

	class Meta:
		model = User_model
		fields = ( 'username', 'email', 'token', 'password' )
		only_read_field = ( 'pk', 'token', )
		only_write_field = ( 'password' )

	def create( self, validate_data ):
		user = User_model( **validate_data )
		user.set_password( validate_data[ 'password' ] )
		return user
