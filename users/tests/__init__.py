from rest_framework.authtoken.models import Token
from snippet import sp_random
from users.models import User

def get_user_test_with_token( ):
	user_test = User.objects.create_user(
		username="mortal_{}".format( sp_random.generate_string() ),
		email=sp_random.generate_email(),
		password=sp_random.generate_string() )
	user_test.save();

	return ( user_test, user_test.refresh_token() )

def get_superuser_test_with_token( dns='promolog2' ):
	user_test = User.objects.create_superuser(
		username="super_{}".format( sp_random.generate_string() ),
		email=sp_random.generate_email(),
		password=sp_random.generate_string() )
	user_test.save();

	return ( user_test, user_test.refresh_token() )
