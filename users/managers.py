from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.db import models

class User_manager( BaseUserManager ):

	def create_user( self, username, email, password,
		first_name='', last_name='', commit=True ):
		"""
		Crea un usuario sin privilegios especiales
		"""

		user = self.model( username = username,
			email = self.normalize_email( email ),
			first_name = first_name,
			last_name = last_name )
		validate_email( email )
		user.is_active = True
		user.set_password( password )
		if commit:
			user.save( using = self._db )
		return user

	def create_superuser( self, username, email, password,
		first_name='', last_name='' ):
		"""
		Crea un superusuario
		"""
		user = self.create_user( username = username,
			password = password,
			email = email,
			first_name = first_name,
			last_name = last_name,
			commit = False )
		user.is_staff = True
		user.is_superuser = True
		user.save( using = self._db )
		return user
