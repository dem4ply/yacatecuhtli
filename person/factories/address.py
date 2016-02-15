import factory
import factory.fuzzy
from person.models import Address
from .country import Country
from snippet import sp_random

class Address( factory.DjangoModelFactory ):
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

	country = factory.SubFactory( Country )
	class Meta:
		model = Address
