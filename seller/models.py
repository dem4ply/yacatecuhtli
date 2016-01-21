from django.db import models
from person.models import Person
from item.models import Item
from person.models import Country
from currency.models import Currency

class Reconcilation( models.Model ):
	created = models.DateTimeField( auto_now_add=True )

class Transfer( models.Model ):
	created = models.DateTimeField( auto_now_add=True )
	date_transfered = models.DateTimeField()
	amount = models.DecimalField( max_digits=14, decimal_places=4 )
	status = models.BooleanField( default=True )
	deposit_account = models.ForeignKey( Seller_bank_account )
	payer = models.ForeignKey( Payer )
	currency = models.ForeignKey( Currency )

class Payment( models.Model ):
	created = models.DateTimeField( auto_now_add=True )
	approved = models.DateTimeField()
	updated = models.DateTimeField()
	transfered = models.DateTimeField()
	reconcilated = models.DateTimeField()
	external_reference = models.CharField( max_length=64 )
	description = models.CharField( max_length=128 )
	amount = models.DecimalField( max_digits=14, decimal_places=4 )
	fee_transsaction_amount = models.DecimalField( max_digits=14, decimal_places=4 )
	fee_rate = models.DecimalField( max_digits=14, decimal_places=4 )
	statement_descriptor = models.CharField( max_length=64 )
	installments = models.IntegerField()
	notification_url = models.CharField( max_length=256 )
	success_url = models.CharField( max_length=256 )
	failure_url = models.CharField( max_length=256 )
	user_agent = models.CharField( max_length=256 )
	ip_address = models.CharField( max_length=64 )
	cookie = models.CharField( max_length=1024 )
	device_session_id = models.CharField( max_length=64 )
	status = models.CharField( max_length=16 )
	seller = models.ForeignKey( Seller )
	payer = models.ForeignKey( Payer )
	payment_method = models.ForeignKey( Payment_method )
	currency = models.ForeignKey( Currency )

	shipping_address = models.ForeignKey( Address )
	billing_address = models.ForeignKey( Address )
	payment_country = models.ForeignKey( Country )
	transfer = models.ForeignKey( Transfer )
	reconcilation = models.ForeignKey( Reconcilation )
	items = models.ManyToManyField( Item )

class Payment_method( models.Model ):
	code = models.CharField( max_length=32 )
	name = models.CharField( max_length=64 )
	type = models.CharField( max_length=128 )
	ssl_img = models.CharField( max_length=128 )
	country = models.ForeignKey( Country )

class Payment_transaction( models.Model ):
	token = models.CharField( max_length=64 )
	cc_token = models.CharField( max_length=64 )
	masked_cc = models.CharField( max_length=16 )
	authorization = models.CharField( max_length=16 )
	status = models.CharField( max_length=16 )
	payment = models.ForeignKey( Payment )
	payment_method = models.ForeignKey( Payment )
	error_code = models.IntegerField()
	error_message = models.CharField( max_length=128 )

class Processor( models.Model ):
	name = models.CharField( max_length=64 )
	country = models.ForeignKey( Country )

class Terminal( models.Model ):
	name = models.CharField( max_length=128 )
	params = models.CharField( max_length=128 )
	status = models.CharField( max_length=128 )
	processor = models.ForeignKey( Processor )

class Fee( models.Model ):
	rate = models.DecimalField( max_digits=14, decimal_places=2 )
	transaction = models.DecimalField( max_digits=14, decimal_places=2 )
	terminal = models.ForeignKey( Terminal, null=True, blank=True )
	payment_menthod = models.Model( Payment_method )

class Seller( Person ):
	items = models.ManyToManyField( Item )
	shares = models.ManyToManyField( Fee )

class Bin( models.Model ):
	bin = models.CharField( max_length=16 )
	seller = models.ForeignKey( Seller )
	terminal = models.ForeignKey( Terminal )

