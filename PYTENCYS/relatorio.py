import matriz as mat
import power_method as pm

def relat():
	'''
	relat --> gera o relatório com a matriz de input 
	o autovalor e autovetor de maor módulo.
	** sem argumentos opcionais ou obrigatórios.
	'''
	M0 = mat.matriz() #chama o módulo matriz inicial 
	X0 = mat.Interacao() # chama o módulo do chute incial 
	X_final, Lambd_final = pm.metodo_das_potencias(prec = 1e-3)

	with open('PYTENCYS.txt','w') as arq: #cria o arquivo; w: write 
		arq.write('PYTENCYS'.center(60, '#')+'\n') 
		arq.write(f'Matriz do usuário: \n{M0}')
		arq.write(f'\nChute inicial: \n{X0}\n')
		arq.write(f'O autovetor final é: \n{X_final}\n')
		arq.write(f'O autovalor final é: \n{Lambd_final}\n')
		arq.write('#'*60)
