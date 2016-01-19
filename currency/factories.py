import factory
import factory.fuzzy
from .models import Currency, Bank
from person.factories import Country_factory
from snippet import sp_random

class Currency_factory( factory.DjangoModelFactory ):
	name = factory.LazyAttribute( lambda t: sp_random.generate_string() )
	iso = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )

	class Meta:
		model = Currency

class Bank_factory( factory.DjangoModelFactory ):
	name = factory.LazyAttribute( lambda t: sp_random.generate_string() )
	ssl_img = factory.LazyAttribute( lambda t: sp_random.generate_string( 3 ) )
	country = factory.SubFactory( Country_factory )

	class Meta:
		model = Bank
