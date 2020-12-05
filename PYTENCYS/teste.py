import numpy as np

L = int(input('numero de linhas da sua matriz: '))
C = int(input('\nnumero de colunas da sua matriz: '))

input_user = list(map(int,input('\nDigite os elementos da matriz: ').split()))
mA= np.array(input_user).reshape(L,C) #matriz A
print(mA)

X0 = list(map(int,input('\nDigite os elementos da matriz inicial de mesma dimensão: ').split())) #Chute inicial
prec = 1e-3 #prec
erro = abs(Lambdak - labdak1)

while erro < prec:
	m0 = np.array(X0)
	y_1 = mA.dot(m0.T)
	print(f'\n{mA} * {m0} = {y_1}')
	np.array([y_1]).tolist()

	lamb=max(int(number) for number in y_1) # Pegando o maior valor da matriz

	m1 = np.array(lamb) # Transformando lambda em matriz
	l=(1/m1) # Divisão da matriz por 1
	x_1 = y_1.dot(l.T) # Multiplicação das matrizes para encontrar X1

print(f'\n(1/{lamb}) * {y_1} = {x_1}')
print('\ny_1 =',y_1) # Resultado de Y1
print('\nx_1 =',x_1) # Resultado de X1
print('\nλ = ',lamb) # Resultado de lambda1
