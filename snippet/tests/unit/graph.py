from django.test import TestCase
from snippet import graph

class test_graph( TestCase ):

	def setUp( self ):
		self.t_array_1 = [
			{
				'id': 1,
				'name': 'uno',
			},
			{
				'id': 3,
				'name': 'tres',
			},
			{
				'id': 6,
				'name': 'seis',
			},
		]

		self.t_array_2 = [ { 'id_2': d[ 'id' ], 'name': d[ 'name' ] }
			for d in self.t_array_1 ]

		self.t_array_3 = [
			{
				'id': 1,
				'id_2': 1,
				'id_3': 1,
				'name': 'uno',
			},
			{
				'id': 3,
				'id_2': 3,
				'id_3': 3,
				'name': 'tres',
			},
			{
				'id': 6,
				'id_2': 6,
				'id_3': 6,
				'name': 'seis',
			},
		]

		self.t_array_duplicate_1 = self.t_array_1 + self.t_array_1

	def test_array_of_dict( self ):
		m = graph.array_of_dict( self.t_array_1 )
		self.assertEqual( m, {
			1: self.t_array_1[0],
			3: self.t_array_1[1],
			6: self.t_array_1[2],
		} )

	def test_array_of_dict_with_another_name( self ):
		m = graph.array_of_dict( self.t_array_2, 'id_2' )
		self.assertEqual( m, {
			1: self.t_array_2[0],
			3: self.t_array_2[1],
			6: self.t_array_2[2],
		} )

	def test_array_of_dict_with_many( self ):
		m = graph.array_of_dict( self.t_array_duplicate_1, many=True )
		self.assertEqual( m, {
			1: [ self.t_array_duplicate_1[0], self.t_array_duplicate_1[3] ],
			3: [ self.t_array_duplicate_1[1], self.t_array_duplicate_1[4] ],
			6: [ self.t_array_duplicate_1[2], self.t_array_duplicate_1[5] ],
		} )

	def test_tree_array_of_dict( self ):
		m = graph.tree_array_of_dict( self.t_array_3, [ 'id', 'id_2', 'id_3' ] )
		self.assertEqual( m, {
			1: { 1: { 1: self.t_array_3[0] } },
			3: { 3: { 3: self.t_array_3[1] } },
			6: { 6: { 6: self.t_array_3[2] } },
		} )

