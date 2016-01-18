import factory
import factory.fuzzy
from .models import Currency
from snippet import sp_random

class Currency_factory( factory.DjangoModelFactory ):
	name = factory.LazyAttribute( lambda t: sp_random.generate_string() )
	iso = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )

	class Meta:
		model = Currency
