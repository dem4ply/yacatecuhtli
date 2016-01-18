import factory
import factory.fuzzy
from person.models import Address
from .country import Country_factory
from .person import Person_factory
from snippet import sp_random

class Address_factory( factory.DjangoModelFactory ):
	#pk = factory.fuzzy.FuzzyInteger( 1000 )
	description = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )
	street = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )
	external_number = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )
	internal_number = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )
	neighbour = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )
	city = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )
	state = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )
	zipcode = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )
	address_type = factory.LazyAttribute( lambda t: sp_random.generate_string( ) )

	country = factory.SubFactory( Country_factory )
	owner = factory.SubFactory( Person_factory )

	class Meta:
		model = Address
