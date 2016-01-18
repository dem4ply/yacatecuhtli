from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.test import TestCase
from snippet import sp_random
import re

class test_sp_random( TestCase ):

	def setUp( self ):
		pass

	def test_generate_string( self ):
		string_test = sp_random.generate_string( 100 )
		self.assertTrue( isinstance( string_test, str ) )
		self.assertEqual( len( string_test ), 100 )

	def test_generate_email( self ):
		email = sp_random.generate_email()
		try:
			validate_email( email )
		except ValidationError:
			self.fail( "El {} no es un email valido".format( email ) )

	def test_generate_domain( self ):
		email = sp_random.generate_email( domain='domain' )
		try:
			validate_email( email )
		except ValidationError:
			self.fail( "El {} no es un email valido".format( email ) )
		regex = re.compile(r'@domain.')
		if regex.search( email ) is None:
			self.fail( "El {} no contine el domino ( 'domain' )".format( email ) )

	def test_generate_email( self ):
		email = sp_random.generate_email( extention='org' )
		try:
			validate_email( email )
		except ValidationError:
			self.fail( "El {} no es un email valido".format( email ) )
		regex = re.compile(r'.org$')
		if regex.search( email ) is None:
			self.fail( "El {} no contine el la extencion ( 'org' )".format( email ) )
