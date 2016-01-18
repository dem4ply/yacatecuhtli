from django import http
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer
import json

def server_error(request, template_name='500.html'):
	"""
	500 error handler.
	Templates: :template:`500.html`
	Context: None
	"""
	format = request.META.get( 'CONTENT_TYPE', 'application/json' )
	result = {
		'detail': _( "Error inesperado" )
	}
	if 'application/xml' in format:
		result = JSONRenderer().render( result )
		result = json.loads( result )
		result = XMLRenderer().render( result )
	else:
		result = JSONRenderer().render( result )
		#result = json.dumps( result )

	return http.HttpResponseServerError( result )
