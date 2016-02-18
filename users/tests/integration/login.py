from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from users.models import User
from snippet import sp_random

class test_login( APITestCase ):
	def setUp( self ):
		pass

	def test_login( self ):
		url_login = reverse( 'user:user-login', kwargs={ 'format': 'json' } )
		url_register = reverse( 'user:user-list', kwargs={ 'format': 'json' } )

		email = sp_random.generate_email()
		username = sp_random.generate_string()
		password = sp_random.generate_string()

		response = self.client.post( url_register, {
			'email': email,
			'username': username,
			'password': password,
		}, format='json' )
		self.assertEqual( response.status_code, status.HTTP_201_CREATED,
			"El status code deberia de ser 201 en lugar de {} :: detail {}"\
				.format( response.status_code, response.data ) )
		response = self.client.post( url_login, {
			'username': username,
			'password': password,
		}, format='json' )
		self.assertEqual( response.status_code, status.HTTP_200_OK,
			"El status code deberia de ser 200 en lugar de {} :: detail {}"\
				.format( response.status_code, response.data ) )
		self.assertNotEqual( response.data[ 'token' ], None,
			"El login no regreso el token" )
