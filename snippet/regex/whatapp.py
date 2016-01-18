import re

# ddd-ddd
# dddddd
registration_code = r'^\d{3}-?\d{3}$'

def is_whatapp_registration_code( code ):
	return re.search( registration_code, code ) != None
