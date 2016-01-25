from django.test import TestCase
from users.models import User
from users.factories import User_factory, Token_factory
from unittest.mock import patch

class Test_user_model( TestCase ):

	@patch( 'users.models.Token.delete' )
	@patch( 'users.models.Token.save' )
	def test_refresh_token( self, token_delete, token_save ):
		user = User( pk=1, username='test' )
		user.token = Token_factory.build()
		token = user.refresh_token()
		user.token.delete.assert_not_called()
		token_save.assert_not_called()
		self.assertEqual( token.user.pk, user.pk )

	def test_str( self ):
		user = User( pk=1, username='test' )
		user.token = Token_factory.build()
		user_str = str( user )
		self.assertEqual( user_str, "{} - {}, {}".format(
			user.pk, user.username, user.token )
		)

	def test_str_no_token( self ):
		user = User( pk=1, username='test' )
		user_str = str( user )
		self.assertEqual( user_str, "{} - {}, ".format(
			user.pk, user.username )
		)
