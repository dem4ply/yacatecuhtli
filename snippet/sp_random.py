"""
funciones para generar randoms
"""
import random
import string

def generate_string( length=10, letters=string.ascii_letters ):
	"""
	Genera una cadena aleatoria usando las letras de ascii

	Arguments
	---------
	length: int
		longitud del la cadena a generar
	
	Returns
	-------
	string
		una cedena aleatoria
	"""
	return u''.join(
		random.choice(	letters ) for x in range( length )
	)


def generate_email( domain=None, extention=None ):
	"""
	Genera un email aleatorio

	Arguments
	---------
	domain: string
		nombre del dominio del email, si no se manda uno se genera
		uno alazar
	extention: string
		nombre de la extencion del email, si no se manda uno se
		genera uno alazar

	Returns
	-------
	string
		un email generado de manera aleatoria
	"""
	if not domain:
		domain = generate_string( 10 )
	if not extention:
		extention = generate_string( 10 )
	return "{name}@{domain}.{extention}".format(**{
		'name': generate_string( 10 ),
		'domain': domain,
		'extention': extention,
	})

def generate_string_numeric( self, length=10, numbers=string.digits ):
	"""
	Genera una cadena de numeros
	
	Arguments
	---------
	length: int
		longitud de la cadena
	numbers: string
		lista de numeros que se utilizaran
	
	Returns
	-------
	string
		una cadena de numeros aleatoria
	"""
	return generate_string( length=length, letters=numbers )

def generate_bool():
	"""
	Genera un booleano aleatorio
	
	Returns
	-------
	bool
		booleano random
	"""
	return bool( random.getrandbits(1) )
