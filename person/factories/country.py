import factory
import factory.fuzzy
from person.models import Country as Country_model
from snippet import sp_random

class Country( factory.DjangoModelFactory ):
	iso = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )
	name = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )

	class Meta:
		model = Country_model
