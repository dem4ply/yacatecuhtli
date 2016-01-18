REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	],
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
		'rest_framework_xml.renderers.XMLRenderer',
	),
	'DEFAULT_PARSER_CLASSES': (
		'rest_framework.parsers.JSONParser',
		'rest_framework_xml.parsers.XMLParser',
	),
	'EXCEPTION_HANDLER': 'system.exceptions.generic_exception_handler',
	'NON_FIELD_ERRORS_KEY': 'detail',
}
