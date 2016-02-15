import factory
import factory.fuzzy
from person.models import Person as Person_model
from snippet import sp_random

class Person( factory.DjangoModelFactory ):
	#pk = factory.fuzzy.FuzzyInteger( 1000 )
	name = factory.LazyAttribute( lambda t: sp_random.generate_string() )
	last_name = factory.LazyAttribute( lambda t: sp_random.generate_string() )
	dni = factory.LazyAttribute( lambda t: sp_random.generate_string() )
	email = factory.LazyAttribute( lambda t: sp_random.generate_email() )
	status = factory.LazyAttribute( lambda t: sp_random.generate_bool() )

	class Meta:
		model = Person_model
