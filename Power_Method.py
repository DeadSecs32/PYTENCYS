import numpy as np

L = int(input('numero de linhas da sua matriz: '))
C = int(input('numero de colunas da sua matriz: '))

input_user = list(map(int,input('\nDigite os elementos da matriz: ').split()))
A= np.array(input_user).reshape(L,C) #matriz A
print(A)
X = list(map(int,input('\nDigite os elementos da matriz inicial de mesma dimensão: ').split())) #Chute inicial
prec = 1e-3 #prec
X_novo = np.array(X)
Y = A.dot(X_novo.T)
lambd = max(Y)
X_novo = (1/lambd)*Y
lambd_anterior = lambd + 1 #pra rodar
erro = abs(lambd - lambd_anterior)
prec = 1e-3
print(Y)
print(X)

while erro > prec:
    Y = A.dot(X_novo.T)
    lambd_anterior = lambd
    lambd = max(Y)
    X_novo = (1 / lambd) * Y
    erro = abs(lambd - lambd_anterior)
    print(Y)
    print(X_novo)
    print(lambd)
    print('--------------')
