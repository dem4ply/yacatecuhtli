from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.db import models
from snippet import sp_random

class User_manager( BaseUserManager ):

	def create_user( self, username, email, password, commit=True ):
		"""
		Crea un usuario sin privilegios especiales
		"""
		from users.models import Token
		validate_email( email )
		user = self.model(
			username=username,
			email=self.normalize_email( email ),
			is_active=True
		)
		user.set_password( password )
		if commit:
			user.save( using = self._db )
			Token.objects.create( user=user )
		return user

	def create_superuser( self, username, email, password ):
		"""
		Crea un superusuario
		"""
		from users.models import Token
		user = self.create_user(
			username=username,
			password=password,
			email=email,
			commit=False )
		user.is_staff = True
		user.is_superuser = True
		user.save( using = self._db )
		Token.objects.create( user=user )
		return user

	def create_user_test( self, username=None, email=None, password=None ):
		"""
		Crea un usuario para pruebas
		"""
		if not username:
			username = sp_random.generate_string()
		if not email:
			email = sp_random.generate_email()
		if not password:
			password = 'password'
		user = self.create_user( username, email, password )
		return user

	def create_superuser_test( self, username=None, email=None, password=None ):
		"""
		Crea un super usuairo para las pruebas
		"""
		if not username:
			username = sp_random.generate_string()
		if not email:
			email = sp_random.generate_email()
		if not password:
			password = 'password'
		user = self.create_superuser( username, email, password )
		return user
