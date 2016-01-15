"""
funciones para generar randoms
"""
import random
import string

def generate_string( length=10 ):
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
		random.choice(
			string.ascii_letters
		) for x in range( length )
	)
