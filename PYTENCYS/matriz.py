import pandas as pd
import numpy as np

def matriz(arq = 'input_user.xlsx',sheet = 'Matriz' ):
	'''
		Argumentos (opcionais):
			arq: O nome do arquivo em formato de xlsx.
			sheet: E em qual planilha se encontra
		Restrições:
			Na planilha o usuário deverá usar a partir da 1° coluna
			(B) e 2° linha (2).
	'''
	df = pd.read_excel(arq, sheet_name = sheet)
	Array = df.to_numpy()
	return Array

def Interacao(arq = 'input_user.xlsx',sheet = 'Interacao' ):
	'''
		Argumentos (opcionais):
			arq: O nome do arquivo em formato de xlsx.
			sheet: E em qual planilha se encontra
		Restrições:
			Na planilha o usuário deverá colocar na primeira linha 
			"nomes" que representem o número e colocar os elementos da matriz
			inicial de chute em linha começando a partir da segunda. 
	'''
	df = pd.read_excel(arq, sheet_name = sheet)
	chute = df.to_numpy()
	return chute
