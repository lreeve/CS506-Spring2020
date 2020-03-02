import numpy as np
import copy

def det(A):
	#assuming nxn matrix
	size = len(A[0])**2
	if (size == 4):
		# return ad-bc
		return ((A[0][0] * A[1][1]) - (A[1][0] * A[0][1]))
	else:
		d = 0
		for i in range(len(A[0])):
			# make deep copy of matrix so you aren't changing A
			new_matrix = copy.deepcopy(A[1:])
			for j in range(len(new_matrix)):
				del new_matrix[j][i]
			# check if you should add or sub
			if (i%2 == 0):
				d += A[0][i] * det(new_matrix)
			else:
				d -= A[0][i] * det(new_matrix)
		return d

print(det([[1,2,3],[4,5,6],[7,8,9]]))