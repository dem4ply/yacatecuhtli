from __future__ import unicode_literals

from django.middleware.csrf import CsrfViewMiddleware
from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from users.models import Token

from rest_framework.authentication import get_authorization_header, BaseAuthentication

class Token_keys_authentication( BaseAuthentication ):
	model = Token

	def authenticate( self, request ):
		auth = get_authorization_header( request ).split()
		if not auth:
			return None
		token_type = auth[0].decode().lower()
		if token_type == 'test_token':
			token_type = 'test'
		elif token_type == 'token':
			token_type = ''
		else:
			return None

		if len( auth ) == 1:
			msg = _( 'Invalid token header. No credentials provided.' )
			raise exceptions.AuthenticationFailed( msg )
		elif len( auth ) > 2:
			msg = _( 'Invalid token header. Token string should not contain spaces.' )
			raise exceptions.AuthenticationFailed( msg )

		try:
			token = auth[1].decode()
		except UnicodeError:
			msg = _( 'Invalid token header. Token string should not contain invalid characters.' )
			raise exceptions.AuthenticationFailed( msg )

		return self.authenticate_credentials( token, token_type )

	def authenticate_credentials( self, key, token_type ):
		params_key = { 'public_key': key }
		try:
			token = self.model.objects.select_related( 'user' ).get( **params_key )
		except self.model.DoesNotExist:
			raise exceptions.AuthenticationFailed( _( 'Invalid token.' ) )

		if not token.user.is_active:
			raise exceptions.AuthenticationFailed( _( 'User inactive or deleted.' ) )

		return ( token.user, token )
	
	def authenticate_header(self, request):
		return 'Token'
