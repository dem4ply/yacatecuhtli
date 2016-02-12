from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import User_manager

from person.models import Person

class User( AbstractBaseUser, PermissionsMixin ):
	"""
	Modelo de usuarios para personalisar los campos
	"""
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$',
		message = "Only alphanumeric characters are allowed." )

	### redefine los campos del modelo user
	username =    models.CharField( unique=True, max_length=64,
							validators=[ alphanumeric ] )
	email =       models.EmailField( verbose_name='email address',
							max_length=255, blank=False, null=False )
	date_joined = models.DateTimeField( auto_now_add=True )
	is_active =   models.BooleanField( default=True, null=False )
	is_staff =    models.BooleanField( default=False, null=False )
	person =      models.ForeignKey( Person, null=True, blank=True )

	objects = User_manager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = [ 'email', ]

	class Meta:
		app_label = 'users'
		db_table = 'users_user'

	def refresh_token( self ):
		"""
		TODO: make test
		Refresca el token el usuario o lo crea

		Returns
		-------

		Token
			token que se genero para el usuario
		"""
		from .token import Token
		try:
			if self.token:
				token.delete()
		except Token.DoesNotExist:
			pass
		finally:
			return Token.objects.create( user=self )

	def __str__( self ):
		from .token import Token
		try:
			token = self.token
		except Token.DoesNotExist:
			token = ''
		return "{} - {}, {}".format( self.pk, self.username, token )
