"""
snippet para grenerar mapas de listas de dicionarios

el motivo del porque se llama graph( grafo ) es por la palabra
reservada de python **map**
TODO:
	convertir esto a una clase y permitir que tambien pueda usar objects
	y no solo dicts
"""

def array_of_dict( array, key='id', many=False ):
	"""
	genera un dicionario que funciona como mapa del array

	el mapa usa el arguemto key para generar la clave

	Arguments
	---------
		array: list
			lista de dicionarios que se desean mapear
		key: string
			define el nombre de la clave de los dicionarios por la
			cual se generara el mapa
		many: bool
			define si las claves se repiten
			si el True regresara un dicionario de listas
			si es False regresara un dicionario de dicionarios
	
	Returns
	-------
		dict
			dicionario que representa un mapa donde sus clave es
			el valor de la key del objeto
	"""
	if many:
		result = {}
		for a in array:
			if a[ key ] in result:
				result[ a[ key ] ].append( a )
			else:
				result[ a[ key ] ] = [ a ]
		return result
	else:
		return { a[ key ]: a for a in array }

def tree_array_of_dict( array, keys=[ 'id' ], many=False ):
	"""
	genera un dicionario que funciona como mapa del array

	el mapa usa el argumento key para generar la clave
	el mapa que forma es un arbol, las hojas del mismo representan
	los objetos del argumento array

	Arguments
	---------
		array: list
			lista de dicionarios que se desean mapear
		keys: array
			lista de claves de los dicionarios por las que se mapeara
		many: bool
			define si las claves se repiten
			si el True regresara un dicionario de listas
			si es False regresara un dicionario de dicionarios
	
	Returns
	-------
		dict
			dicionario que representa un mapa donde cada key que se le paso
			se usara como clave subsecunete del mapa
	"""
	result = {}
	l_keys = len( keys )
	for a in array:
		aux_map = result
		for i in range( l_keys ):
			if a[ keys[i] ] in aux_map:
				aux_map = aux_map[ a[ keys[i] ] ]
				if i == l_keys-1:
					aux_map[ a[ keys[i] ] ] = a
				else:
					if a[ keys[i] ] not in aux_map:
						aux_map[ a[ keys[i] ] ] = {}
						
			else:
				aux_map[ a[ keys[i] ] ] = {}
	return result
