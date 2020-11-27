'''
    Power Method:
        método das potências:
            --> Descobrir o maior autovalor e o maior autovalor
            de uma matriz quadrada diagonalizável
        Funções:
            --> método_das_potências: calcula os maiores
            autovalores e autovetores de maior módulo
'''

import numpy as np
import matriz as mat

def metodo_das_potencias(prec):
	'''
    Cálculo dos valores de maior módulo pelo método
    das potências.
	    Argumentos:
	        - obrigatórios:
	            prec - o usuário deverá colocar a precisão que a interação
	            deverá ter.
	    Restrições:
	        O usuário deverá colocar matrizes quadradas n dimensionais
	        diagonalizáveis.
	'''
	A = mat.matriz()
	print(A)
	X = list(map(int,input('\nDigite os elementos da matriz inicial de mesma dimensão: ').split())) # Chute inicial
	X_novo = np.array(X) #transforma a lista X em um array
	Y = A.dot(X_novo.T) # multiplica a matriz A pela transposta de X
	lambd = max(Y) # separa o valor de maior módulo
	X_novo = (1/lambd)*Y # calcula o autovetor
	lambd_anterior = lambd + 1 #pra rodar
	erro = abs(lambd - lambd_anterior)
	print(Y)
	print(X)
	
	while erro > prec: #laço de interações
		Y = A.dot(X_novo.T)
		lambd_anterior = lambd
		lambd = max(Y)
		X_novo = (1 / lambd) * Y
		erro = abs(lambd - lambd_anterior)
		print(Y)
		print(f'autovetor:{X_novo}')
		print(f'autovalor: {lambd}')
		print('--------------')

metodo_das_potencias(prec = 1e-10)
