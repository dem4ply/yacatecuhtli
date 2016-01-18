import factory
import factory.fuzzy
from person.models import Country
from snippet import sp_random

class Country_factory( factory.DjangoModelFactory ):
	#pk = factory.fuzzy.FuzzyInteger( 1000 )
	name = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )
	iso = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )

	class Meta:
		model = Country
