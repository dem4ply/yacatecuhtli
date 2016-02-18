import factory
import factory.fuzzy
from .models import (
	Category as Category_model,
	Item as Item_model )
import string
from users.factories import User_factory

class Category( factory.DjangoModelFactory ):
	name        = factory.fuzzy.FuzzyText()
	description = factory.fuzzy.FuzzyText()
	owner       = factory.SubFactory( User_factory )

	class Meta:
		model = Category_model

class Item( factory.DjangoModelFactory ):
	sku         = factory.fuzzy.FuzzyText()
	upc         = factory.fuzzy.FuzzyText( chars=string.digits )
	name        = factory.fuzzy.FuzzyText()
	description = factory.fuzzy.FuzzyText()
	price       = factory.fuzzy.FuzzyDecimal( 1.0, precision=4 )
	category    = factory.SubFactory( Category )

	class Meta:
		model = Item_model
