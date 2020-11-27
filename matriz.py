import pandas as pd
import numpy as np

def matriz(arq = 'input_user.xlsx',sheet = 'Matriz' ):
	'''
	Argumentos (opcionais): 
        O nome do arquivo em formato de xlsx.
        E em qual planilha se encontra 
    Restrições: 
        Na planilha o usuário deverá usar a partir da 2° coluna
        (B) e 2° linha (2). 
	'''
	df = pd.read_excel(arq, sheet_name = sheet)
	Array = df.to_numpy()
	return Array
