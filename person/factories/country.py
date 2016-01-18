import factory
import factory.fuzzy
from person.models import Country
from snippet import sp_random

class User_factory( factory.DjangoModelFactory ):
	name = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )
	iso = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )

	class Meta:
		model = Country
