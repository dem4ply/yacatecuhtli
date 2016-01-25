from .models import Seller
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext as _
from rest_framework import serializers, status
from system.exceptions import Http_code_error
from person.serializers import Person_serializer

class Seller_serializer( serializers.ModelSerializer ):
	person = Person_serializer( read_only=True )
	class Meta:
		model = Seller
		fields = ( 'pk', 'person', )
