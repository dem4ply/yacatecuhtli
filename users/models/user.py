from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import User_manager

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
	first_name =  models.CharField( max_length=128, null=True, blank=True )
	last_name =   models.CharField( max_length=128, null=True, blank=True )
	date_joined = models.DateTimeField( auto_now_add=True )
	is_active =   models.BooleanField( default=True, null=False )
	is_staff =    models.BooleanField( default=False, null=False )

	objects = User_manager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = [ 'email', ]

	class Meta:
		app_label = 'users'
		db_table = 'users_user'

	def get_full_name( self ):
		"""
		Optiene el nombre completo del usuario
		"""
		fullname = self.first_name + " " + self.last_name
		return fullname

	def get_short_name( self ):
		"""
		Obtiene el nombre corto del usaurio
		"""
		return self.username

	def get_token( self ):
		"""
		TODO: make test
		Obtiene el token del usuario

		Return
		------

		Token
			token del usuario

		Raises
		------

		Token.DoesNotExist:
			EL usuario no tiene token
		"""
		from .token import Token
		return Token.objects.get( user=self )

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
			token = self.get_token()
			token.delete()
		except Token.DoesNotExist:
			pass
		finally:
			return Token.objects.create( user=self )

	def __str__( self ):
		return "{} - {} # {}".format( self.id, self.username, self.get_full_name() )
