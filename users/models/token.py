import binascii
import os
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from rest_framework.authtoken.models import Token as Token_legacy

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

@python_2_unicode_compatible
class Token( models.Model ):

	user = models.OneToOneField( AUTH_USER_MODEL, related_name='token' )
	public_key = models.CharField( unique=True, max_length=64 )
	private_key = models.CharField( unique=True, max_length=64 )
	test_public_key = models.CharField( unique=True, max_length=64 )
	test_private_key = models.CharField( unique=True, max_length=64 )

	def save( self, *args, **kwargs ):
		if not self.public_key:
			self.public_key = self.generate_keys()
		if not self.private_key:
			self.private_key = self.generate_keys()
		if not self.test_public_key:
			self.test_public_key = self.generate_keys()
		if not self.test_private_key:
			self.test_private_key = self.generate_keys()
		return super( Token, self ).save( *args, **kwargs )

	def generate_keys( self ):
		return binascii.hexlify( os.urandom( 20 ) ).decode()

	def __str__( self ):
		result = "tput: {} :: tprv: {}".format( self.test_public_key,
			self.test_private_key )
		return result

