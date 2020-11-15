import numpy as np

L = int(input('numero de linhas da sua matriz: '))
C = int(input('numero de colunas da sua matriz: '))

input_user = list(map(int,input('Digite os elementos da matriz: ').split()))
mA= np.array(input_user).reshape(L,C)
print(mA)

def autovalor_autovetor():
	Lambda = 0
	count = 0
	while xxx:
		X0 = list(map(int,input('Digite os elementos da matriz inicial de mesma dimensão: ').split()))
		m0 = np.array(X0)
		print(m0)
		b = mA.dot(m0)
		print(b)
		count += 1
