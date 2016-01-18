from django.conf import settings
from django.test import TestCase
from snippet.regex import whatapp
import re

class test_regex_whatapp( TestCase ):
	def test_should_validate_regex_codes_of_register_whatapp( self ):
		list_test_ok = ( '123456', '123-456' )
		regex = re.compile( whatapp.registration_code )
		for l in list_test_ok:
			self.assertTrue( regex.search( l ),
				"El codigo ( %s ) deberia de ser valido" % l )

	def test_should_invalidate_regex_codes_of_register_whatapp( self ):
		list_test_fail = ( 'asdfgh', '12345q', '123/456' )
		regex = re.compile( whatapp.registration_code )
		for l in list_test_fail:
			self.assertFalse( regex.search( l ),
				"El codigo ( %s ) deberia de ser invalido" % l )

	def test_should_validate_codes_of_register_whatapp( self ):
		list_test_ok = ( '123456', '123-456' )
		for l in list_test_ok:
			self.assertTrue( whatapp.is_whatapp_registration_code( l ),
				"El codigo ( %s ) deberia de ser valido" % l )

	def test_should_invalidate_codes_of_register_whatapp( self ):
		list_test_fail = ( 'asdfgh', '12345q', '123/456' )
		for l in list_test_fail:
			self.assertFalse( whatapp.is_whatapp_registration_code( l ),
				"El codigo ( %s ) deberia de ser invalido" % l )

