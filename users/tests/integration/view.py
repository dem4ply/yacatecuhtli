from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from users.models import User
from snippet import sp_random

class test_api_credential( APITestCase ):
	def setUp( self ):
		self.user_test = User.objects.create_user_test()

	def test_login( self ):
		url = reverse( 'user:user-login', kwargs={
			'format': 'json',
		} )
		data = {
			'username': self.user_test.username,
			'password': 'password',
		}
		response = self.client.post( url, data, format='json' )
		self.assertEqual( response.status_code, status.HTTP_200_OK,
			"el status code deberia de ser 200 en lugar de {} :: detail {}"\
				.format( response.status_code, response.data ) )

	def test_login_inactive( self ):
		url = reverse( 'user:user-login', kwargs={
			'format': 'json',
		} )
		self.user_test.is_active = False
		self.user_test.save()
		data = {
			'username': self.user_test.username,
			'password': 'password',
		}
		response = self.client.post( url, data, format='json' )
		self.assertEqual( response.status_code, status.HTTP_404_NOT_FOUND,
			"el status code deberia de ser 404 en lugar de {} :: detail {}"\
				.format( response.status_code, response.data ) )

	def test_login_fail( self ):
		url = reverse( 'user:user-login', kwargs={
			'format': 'json',
		} )
		self.user_test.is_active = False
		self.user_test.save()
		data = {
			'username': self.user_test.username,
			'password': 'sadf',
		}
		response = self.client.post( url, data, format='json' )
		self.assertEqual( response.status_code, status.HTTP_404_NOT_FOUND,
			"el status code deberia de ser 404 en lugar de {} :: detail {}"\
				.format( response.status_code, response.data ) )

	def test_register( self ):
		url = reverse( 'user:user-list', kwargs={
			'format': 'json',
		} )
		self.user_test.is_active = False
		self.user_test.save()
		email = sp_random.generate_email()
		password = sp_random.generate_string()
		data = {
			'username': email,
			'email': email,
			'password': password,
		}
		response = self.client.post( url, data, format='json' )
		self.assertEqual( response.status_code, status.HTTP_201_CREATED,
			"el status code deberia de ser 201 en lugar de {} :: detail {}"\
				.format( response.status_code, response.data ) )
