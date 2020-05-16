import sys

def main():
	 size = int(input("Enter the size of the matrix: "))
	 i = 0
	 j = 0
	 A = []
	 while i < size:
	 	l = []
	 	while j < size:
	 		print "Entry ", i, j
	 		l.append(int(input()))
	 		j += 1
	 	A.append(l)
	 	i += 1
	 	j = 0
	 	
	 i = 0
	 j = 0
	 k = 0
	 L = []
	 U = []
	 while i < size:
	 	l = []
	 	while j < size:
	 		l.append(0)
	 		j += 1
	 	L.append(l)
	 	U.append(l)
	 	i += 1
	 	j = 0
	 print L
	 print U
	 	
	 while i < size:
	 	while k < size:
	 		s = 0
	 		while j <= i:
	 			s += L[i][j] * U[j][k]
	 


if __name__ == '__main__':
	main()
