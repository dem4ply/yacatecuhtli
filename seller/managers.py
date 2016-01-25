from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.db import models
from system.exceptions import Http_code_error
from snippet import sp_random
from users.models import User
from person.models import Person

class Seller_manager( BaseUserManager ):

	def create_test( self, user ):
		"""
		Crea un vendedor de pruebas
		"""
		person = Person(
			name=sp_random.generate_string(),
			last_name=sp_random.generate_string(),
			dni=sp_random.generate_string(),
			email=user.email,
			status=True
		)
		person.save()
		seller = self.model( user=user, person=person )
		seller.save()
		return seller
