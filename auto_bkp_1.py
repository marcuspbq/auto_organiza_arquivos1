# -*- coding: latin-1 -*-

# 1 - Importando biblioteca respons�vel por manipular arquivos:
import os
import time
import shutil
import re

# 2 - Declarando vari�veis:


caminho = r"C:\Users\marcu\OneDrive\Desenv\Python\Automa��o\PA1\mover" + "\\" # Declarando vari�vel para informar a localiza��o da pasta - Caso seja na mesma pasta do projeto, n�o precisa
destino = r"C:\Users\marcu\OneDrive\Desenv\Python\Automa��o\PA1\organizados" + "\\" # Declarando vari�vel para informar a localiza��o da pasta de destino
duplicados= r"C:\Users\marcu\OneDrive\Desenv\Python\Automa��o\PA1\duplicados" + "\\" # Declarando vari�vel para informar a localiza��o da pasta de duplicatas
lista_arquivos = os.listdir(caminho) # Lista os arquivos da pasta e coloca na vari�vel (list)

# 3 - Criando pasta para cada m�s/ano e armazenando o arquivo correspondente dentro dela
for arquivo in lista_arquivos:  # Faz um for j� declarando a vari�vel arquivo que assume cada item da lista
    data_modifica = os.path.getmtime(caminho + arquivo)  # pega a data e hora de cria��o sem formata��o
    data_completa = time.ctime(data_modifica)  # Formata data de modifica��o
    data_completa_lista = (data_completa.split())  # separa os dados da v�ri�vel data_completa em uma lista
    mes_ano = data_completa_lista[1] + data_completa_lista[4]  # Seleciona apenas o m�s e o ano da lista
    nome_pasta = mes_ano  # Atribui o m�s e ano na vari�vel nome_pasta

    if not os.path.isdir(destino + nome_pasta):  # vemos se este diretorio ja existe
        os.mkdir(destino + nome_pasta)  # aqui criamos a pasta caso nao exista

    try:
        os.rename(caminho + "\\" + arquivo,
                  (destino + nome_pasta + "\\" + arquivo))  # verifica se o arquivo j� existe na pasta destino
    except:
        agora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # pega a data / hora atual (local) como str
        agora = re.sub("\:", "", agora)  # retira ":" da string para poder servir como nome do arquivo
        os.rename(caminho + "\\" + arquivo, (duplicados + "\\" + arquivo + "_D_" + agora))




