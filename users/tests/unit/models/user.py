from django.test import TestCase
from users.models import User
from users.factories import User_factory

user_latest = User_factory.build()
def user_manager_latest( cosa ):
	return user_latest

class test_user( TestCase ):
	def test_get_full_name( self ):
		user = User( username='user_name',
			first_name='first',
			last_name='last' )
		self.assertEqual( user.get_full_name(), "first last" );
		self.assertEqual( str( user ), "user_name" );

	def test_get_full_name( self ):
		user = User( username='user_name',
			first_name='first',
			last_name='last' )
		self.assertEqual( user.get_short_name(), "user_name" );
		self.assertEqual( str( user ), "user_name" );

	def test_get_full_name( self ):
		user = User( username='user_name',
			first_name='first',
			last_name='last' )
		full = user.get_full_name()
		short = user.get_short_name()
		self.assertEqual( str( user ),
			"None - user_name # first last" );
