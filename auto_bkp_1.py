# -*- coding: latin-1 -*-

# 1 - Importando biblioteca responsável por manipular arquivos:
import os
import time
import shutil
import re

# 2 - Declarando variáveis:


caminho = r"C:\Users\marcu\OneDrive\Desenv\Python\Automação\PA1\mover" + "\\" # Declarando variável para informar a localização da pasta - Caso seja na mesma pasta do projeto, não precisa
destino = r"C:\Users\marcu\OneDrive\Desenv\Python\Automação\PA1\organizados" + "\\" # Declarando variável para informar a localização da pasta de destino
duplicados= r"C:\Users\marcu\OneDrive\Desenv\Python\Automação\PA1\duplicados" + "\\" # Declarando variável para informar a localização da pasta de duplicatas
lista_arquivos = os.listdir(caminho) # Lista os arquivos da pasta e coloca na variável (list)

# 3 - Criando pasta para cada mês/ano e armazenando o arquivo correspondente dentro dela
for arquivo in lista_arquivos:  # Faz um for já declarando a variável arquivo que assume cada item da lista
    data_modifica = os.path.getmtime(caminho + arquivo)  # pega a data e hora de criação sem formatação
    data_completa = time.ctime(data_modifica)  # Formata data de modificação
    data_completa_lista = (data_completa.split())  # separa os dados da váriável data_completa em uma lista
    mes_ano = data_completa_lista[1] + data_completa_lista[4]  # Seleciona apenas o mês e o ano da lista
    nome_pasta = mes_ano  # Atribui o mês e ano na variável nome_pasta

    if not os.path.isdir(destino + nome_pasta):  # vemos se este diretorio ja existe
        os.mkdir(destino + nome_pasta)  # aqui criamos a pasta caso nao exista

    try:
        os.rename(caminho + "\\" + arquivo,
                  (destino + nome_pasta + "\\" + arquivo))  # verifica se o arquivo já existe na pasta destino
    except:
        agora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # pega a data / hora atual (local) como str
        agora = re.sub("\:", "", agora)  # retira ":" da string para poder servir como nome do arquivo
        os.rename(caminho + "\\" + arquivo, (duplicados + "\\" + arquivo + "_D_" + agora))




