from django.test import TestCase
from snippet import sp_random

class test_graph( TestCase ):

	def setUp( self ):
		pass

	def test_array_of_dict( self ):
		string_test = sp_random.generate_string( 100 )
		self.assertTrue( isinstance( string_test, str ) )
		self.assertEqual( len( string_test ), 100 )
