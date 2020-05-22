'''Computers usually solve square systems of linear equations using the LU decomposition. Write a program to compute LU decomposition.'''
import sys

def lu(a, n) :
	l = [[0 for x in range(n)] for y in range(n)]
	u = [[0 for x in range(n)] for y in range(n)] 
	for i in range(n):
		for k in range(i, n):
			sum_l = 0
			for j in range(i):
				sum_l += (l[i][j] * u[j][k])
			u[i][k] = a[i][k] - sum_l

		for k in range(i, n):
			if k == i:
				l[k][k] = 1
			else:
				sum_u = 0
				for j in range(i):
					sum_u += (l[k][j] * u[j][i])
				l[k][i] = (a[k][i] - sum_u) // u[i][i]
	print_mat(l, u, n)
				
def print_mat(l, u, n) :
	print('Lower triangular matrix :')
	for i in range(n) :
		for j in range(n) :
			print(str(l[i][j]), end = '\t') 
		print('\n')
			
	print('Upper triangular matrix :')
	for i in range(n) :
		for j in range(n) :
			print(str(u[i][j]), end = '\t') 
		print('\n')
	
if __name__ == '__main__' :
	n = int(input('Enter the order of the matrix : '))
	print('Enter the matrix A :')
	a = [[0 for x in range(n)] for y in range(n)]
	for i in range(n) :
		for j in range(n) :
			a[i][j] = (int(input()))
	lu(a, len(a))
