def lower_keys( obj ):
	"""
	TODO: make test
	Transforma todas las keys de un dicionario a minusculas de manaera recursiva

	en caso de de que se pase un array lo que hara sera recorerlo de manera recursiba buscando dicts
	para aplicarles la funcion

	Parameters
	----------
	obj: dict, list
		el objeto que se quiere pasar sus keys a minuscula
		en caso de ser array lo recorrera en busca de objetos dict

	Returns
	-------
		'dict': si el parametro es un ditc
		'array': si el parametro es un list
	
	"""
	if isinstance( obj, list ):
		return [ lower_keys( v ) for v in obj ]
	elif isinstance( obj, dict ):
		return dict( ( k.lower(), lower_keys( v )) for k, v in obj.iteritems() )
	else:
		return obj
