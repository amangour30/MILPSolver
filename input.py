from pulp import *

n1 = raw_input("Please enter number of integer variables: ")
print "N1: ", n1

n2 = raw_input("Please enter number of continuous variables: ")
print "N2: ", n2

print "Please enter the wegihts of the objective function C1 \n"
C = []

for i in range(int(n1)):
    n = raw_input("c %d:"%(i+1))
    C.append(int(n))
    
for i in range(int(n2)):
    n = raw_input("c %d:"%(i+1))
    C.append(int(n))

numm = raw_input("Please enter number of equations: ")
print "M: ", numm

b = []
A = []
G = []

for i in range(int(numm)):
	print "Add %d th equation:"%(i+1)
	temp = []
	temp2 = []
	for j in range(int(n1)):
		aij = raw_input("a %d %d:"%(i+1, j+1))
		temp.append(aij)
	for j in range(int(n2)):
		aij = raw_input("g %d %d:"%(i+1, j+1))
		temp2.append(aij)
	bi = raw_input("b %d:"%(i+1))
	A.append(temp)
	G.append(temp2)
	b.append(bi)
