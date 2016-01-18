from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import exception_handler

class Http_code_error( Exception ):

	def __init__( self,
		status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
		context=None
	):
		# si el contexto es una cadena regresa el context en formato
		# detail
		if isinstance( context, ( str ) ):
			context = { 'detail': context }
		self.status_code = status_code
		self.context = context
		

def generic_exception_handler( exc, context ):
	"""
	maneja las exceptciones esperadas de la api como los codigos 404
	"""
	# Call REST framework's default exception handler first,
	# to get the standard error response.
	response = exception_handler( exc, context )

	# Now add the HTTP status code to the response.
	if response is not None:
		if isinstance( exc, serializers.ValidationError ):
			data = response.data
			if 'detail' in data:
				if len( data[ 'detail' ] ) == 1:
					data[ 'detail' ] = data[ 'detail' ][0]
	elif isinstance( exc, Http_code_error ):
		response = Response( exc.context, status=exc.status_code )

	return response
