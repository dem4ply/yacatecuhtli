import factory
import factory.fuzzy
from users.models import Token
from snippet import sp_random

class Token_factory( factory.DjangoModelFactory ):
	public_key = factory.LazyAttribute(lambda t: sp_random.generate_string())
	private_key = factory.LazyAttribute(lambda t: sp_random.generate_string())
	test_public_key = factory.LazyAttribute(lambda t: sp_random.generate_string())
	test_private_key = factory.LazyAttribute(lambda t: sp_random.generate_string())

	class Meta:
		model = Token
