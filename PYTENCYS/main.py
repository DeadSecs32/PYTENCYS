import power_method as pm
import relatorio as rl

'''
	Main.py: Será usado para chamar a matriz fornecida pelo usuário 
	* biblioteca necessária: 
		power_method: biblioteca principal
		função: pm.metodo_das_potencias(prec = 1e-3) #prec: precisão do algoritimo 
	*biblioteca opcional: 
		relatorio: gera o relatório com os dados obtidos
		na biblioteca power_method
		função: rl.relat() #não precisa de argumentos. 
'''

pm.metodo_das_potencias(prec=1e-3)
rl.relat()


