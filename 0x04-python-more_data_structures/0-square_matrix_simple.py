#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new_matrix = [row[:] for row in matrix]
	sq_matrix = map(lambda x: [i**2 for i in x], new_matrix)
	return sq_matrix
