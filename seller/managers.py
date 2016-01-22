from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.db import models
from system.exceptions import Http_code_error
from snippet import sp_random
from users.models import User
from person.models import Person

class Seller_manager( BaseUserManager ):

	def create_test( self, email, password ):
		"""
		Crea un vendedor de pruebas
		"""
		user = User.objects.create_user(
			username="test_{}".format( sp_random.generate_string() ),
			email=sp_random.generate_email(),
			password=sp_random.generate_string()
		)
		user.set_password( password )
		person = Person(
			name=sp_random.generate_string(),
			last_name=sp_random.generate_string(),
			dni=sp_random.generate_string(),
			email=email,
			status=True
		)
		user.save();
		person.save()
		seller = self.model( user=user, person=person )
		seller.save()
		return seller
