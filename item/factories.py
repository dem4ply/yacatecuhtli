import factory
import factory.fuzzy
from .models import Item, Category
from snippet import sp_random

class Item_factory( factory.DjangoModelFactory ):
	sku = factory.LazyAttribute( lambda t: sp_random.generate_string() )
	name = factory.LazyAttribute( lambda t: sp_random.generate_string() )

	class Meta:
		model = Item

class Category_factory( factory.DjangoModelFactory ):
	name = factory.LazyAttribute( lambda t: sp_random.generate_string() )

	class Meta:
		model = Category
