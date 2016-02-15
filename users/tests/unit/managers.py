from django.test import TestCase
from users.models import User
from users.factories import User_factory
from unittest.mock import patch

class Test_user_manager( TestCase ):
	@patch( "users.models.User.save" )
	@patch( "users.models.Token.save" )
	def test_create_user( self, user_save, token_save ):
		user = User.objects.create_user( 'test', 'email@email.email',
			'password' )
		self.assertTrue( user_save.called )
		self.assertTrue( token_save.called )
		self.assertEqual( user.username, "test" )
		self.assertEqual( user.email, "email@email.email" )
		self.assertNotEqual( user.password, "password" )
		self.assertTrue( user.is_active )
		self.assertFalse( user.is_staff )


	@patch( "users.models.User.save" )
	@patch( "users.models.Token.save" )
	def test_create_user_no_commit( self, user_save, token_save ):
		user = User.objects.create_user( 'test', 'email@email.email',
			'password', commit=False )
		user_save.assert_not_called()
		token_save.assert_not_called()

	@patch( "users.models.User.save" )
	@patch( "users.models.Token.save" )
	def test_create_superuser( self, user_save, token_save):
		user = User.objects.create_superuser( 'test', 'email@email.email',
			'password' )
		self.assertTrue( user.is_staff )
		self.assertTrue( user.is_superuser )
		self.assertTrue( user_save.called )
		self.assertTrue( token_save.called )

	@patch( "users.models.User.save" )
	@patch( "users.models.Token.save" )
	def test_create_superuser_test( self, user_save, token_save ):
		user = User.objects.create_superuser_test()
		self.assertTrue( user.is_staff )
		self.assertTrue( user.is_superuser )
		self.assertTrue( user_save.called )
		self.assertTrue( token_save.called )

	@patch( "users.models.User.save" )
	@patch( "users.models.Token.save" )
	def test_create_user_test( self, user_save, token_save ):
		user = User.objects.create_user_test()
		self.assertFalse( user.is_staff )
		self.assertFalse( user.is_superuser )
		self.assertTrue( user_save.called )
		self.assertTrue( token_save.called )
