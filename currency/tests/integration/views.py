from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from unittest.mock import patch
from users.tests import get_user_test_with_token

class Test_api_currency_no_autentificate( APITestCase ):
	"""
	prueba del api para los paises cuadno el usuario no esta autentificado
	"""

	def test_retrieve( self, *args ):
		url = reverse( 'currency:currency-list', kwargs={
			'format': 'json',
		} )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.get( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 401 en lugar de {}"\
				.format( response.status_code ) )

	def test_detail( self, *args ):
		url = reverse( 'currency:currency-detail', kwargs={
			'format': 'json',
			'pk': 1,
		} )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.get( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 401 en lugar de {}"\
				.format( response.status_code ) )

	def test_create( self, *args ):
		url = reverse( 'currency:currency-list', kwargs={
			'format': 'json',
		} )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.post( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 401 en lugar de {}"\
				.format( response.status_code ) )

	def test_update( self, *args ):
		url = reverse( 'currency:currency-detail', kwargs={
			'format': 'json',
			'pk': 1,
		} )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.put( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 401 en lugar de {}"\
				.format( response.status_code ) )

class Test_api_currency_authorize( APITestCase ):
	"""
	Prueba del api para los paises para comprobar que si entra
	cuando esta autorizado el usuario
	"""
	def setUp( self ):
		self.user_test, self.user_test_token = get_user_test_with_token()

	def test_retrieve( self, *args ):
		url = reverse( 'currency:currency-list', kwargs={
			'format': 'json',
		} )
		self.client.credentials( http_authorization='token ' +
			self.user_test_token.key )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.get( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 200 en lugar de {}"\
				.format( response.status_code ) )

	def test_detail( self, *args ):
		url = reverse( 'currency:currency-detail', kwargs={
			'format': 'json',
			'pk': 1,
		} )
		self.client.credentials( http_authorization='token ' +
			self.user_test_token.key )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.get( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 404 en lugar de {}"\
				.format( response.status_code ) )

	def test_create( self, *args ):
		url = reverse( 'currency:currency-list', kwargs={
			'format': 'json',
		} )
		self.client.credentials( http_authorization='token ' +
			self.user_test_token.key )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.post( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 400 en lugar de {}"\
				.format( response.status_code ) )

	def test_update( self, *args ):
		url = reverse( 'currency:currency-detail', kwargs={
			'format': 'json',
			'pk': 1,
		} )
		self.client.credentials( http_authorization='token ' +
			self.user_test_token.key )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.put( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 400 en lugar de {}"\
				.format( response.status_code ) )

class Test_api_bank_no_autentificate( APITestCase ):
	"""
	prueba del api para los paises cuadno el usuario no esta autentificado
	"""

	def test_retrieve( self, *args ):
		url = reverse( 'currency:bank-list', kwargs={
			'format': 'json',
		} )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.get( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 401 en lugar de {}"\
				.format( response.status_code ) )

	def test_detail( self, *args ):
		url = reverse( 'currency:bank-detail', kwargs={
			'format': 'json',
			'pk': 1,
		} )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.get( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 401 en lugar de {}"\
				.format( response.status_code ) )

	def test_create( self, *args ):
		url = reverse( 'currency:bank-list', kwargs={
			'format': 'json',
		} )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.post( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 401 en lugar de {}"\
				.format( response.status_code ) )

	def test_update( self, *args ):
		url = reverse( 'currency:bank-detail', kwargs={
			'format': 'json',
			'pk': 1,
		} )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.put( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 401 en lugar de {}"\
				.format( response.status_code ) )

class Test_api_bank_authorize( APITestCase ):
	"""
	Prueba del api para los paises para comprobar que si entra
	cuando esta autorizado el usuario
	"""
	def setUp( self ):
		self.user_test, self.user_test_token = get_user_test_with_token()

	def test_retrieve( self, *args ):
		url = reverse( 'currency:bank-list', kwargs={
			'format': 'json',
		} )
		self.client.credentials( http_authorization='token ' +
			self.user_test_token.key )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.get( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 200 en lugar de {}"\
				.format( response.status_code ) )

	def test_detail( self, *args ):
		url = reverse( 'currency:bank-detail', kwargs={
			'format': 'json',
			'pk': 1,
		} )
		self.client.credentials( http_authorization='token ' +
			self.user_test_token.key )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.get( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 404 en lugar de {}"\
				.format( response.status_code ) )

	def test_create( self, *args ):
		url = reverse( 'currency:bank-list', kwargs={
			'format': 'json',
		} )
		self.client.credentials( http_authorization='token ' +
			self.user_test_token.key )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.post( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 400 en lugar de {}"\
				.format( response.status_code ) )

	def test_update( self, *args ):
		url = reverse( 'currency:bank-detail', kwargs={
			'format': 'json',
			'pk': 1,
		} )
		self.client.credentials( http_authorization='token ' +
			self.user_test_token.key )
		# no deberia de ser valido porque no se a autentificado el usuario
		response = self.client.put( url, format='json' )
		self.assertEqual( response.status_code, status.HTTP_401_UNAUTHORIZED,
			"el status code deberia de ser 400 en lugar de {}"\
				.format( response.status_code ) )
