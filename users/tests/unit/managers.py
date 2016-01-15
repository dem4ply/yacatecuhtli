from django.test import TestCase
from users.models import User
from users.factories import User_factory
from unittest.mock import patch

user_latest = User_factory.build()
def user_manager_latest( cosa ):
	return user_latest

class Test_user_manager( TestCase ):

	@patch( "users.models.User.save" )
	def test_create_user( self, *args ):
		user = User.objects.create_user( 'test', 'email@email.email', 'password',
			'first_name', 'last_name' )
		self.assertTrue( user.save.called )
		self.assertEqual( user.username, "test" )
		self.assertEqual( user.email, "email@email.email" )
		self.assertNotEqual( user.password, "password" )
		self.assertEqual( user.first_name, "first_name" )
		self.assertEqual( user.last_name, "last_name" )
		self.assertTrue( user.is_active )
		self.assertFalse( user.is_staff )

	@patch( "users.models.User.save" )
	def test_create_user_no_commit( self, *args ):
		user = User.objects.create_user( 'test', 'email@email.email', 'password',
			'first_name', 'last_name', commit=False )
		user.save.assert_not_called()

	@patch( "users.models.User.save" )
	def test_create_superuser( self, *args ):
		user = User.objects.create_superuser( 'test', 'email@email.email', 'password',
			'first_name', 'last_name' )
		self.assertTrue( user.is_staff )
		self.assertTrue( user.is_superuser )
		self.assertTrue( user.save.called )
