import factory
import factory.fuzzy
from users.models import User
from snippet import sp_random

class User_factory( factory.DjangoModelFactory ):
	username = factory.LazyAttribute(lambda t: sp_random.generate_string())
	email = factory.LazyAttribute(lambda t: sp_random.generate_string())
	first_name = factory.LazyAttribute(lambda t: sp_random.generate_string())
	last_name = factory.LazyAttribute(lambda t: sp_random.generate_string())
	id = factory.fuzzy.FuzzyInteger( 1000 )

	class Meta:
		model = User
