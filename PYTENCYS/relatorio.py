import matriz as mat
import power_method as pm

M0 = mat.matriz()
X0 = mat.Interacao()
X_final, Lambd_final = pm.metodo_das_potencias(prec = 1e-3)

with open('arquivo.txt','w') as arq:
	arq.write('PYTENCYS'.center(60, '#')+'\n')
	arq.write(f'Matriz do usuário: \n{M0}')
	arq.write(f'\nChute inicial: \n{X0}\n')
	arq.write(f'O autovetor final é: \n{X_final}\n')
	arq.write(f'O autovalor final é: \n{Lambd_final}\n')
	arq.write('#'*60)
