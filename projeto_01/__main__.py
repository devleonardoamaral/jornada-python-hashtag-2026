"""
Projeto 01 - Automação com Python

Script de automação para registrar dados do arquivo CSV no banco de dados do site da
HashtagTreinamentos.

Obs.:
    1. Não foi utilizado o comando `pyautogui.click()` ao obter o foco do HTML para evitar
    incompatibilidades com diferentes resoluções de telas, já que o próprio site aceita
    TAB para focar no primeiro campo de texto.

    2. Não foi utlizado o comando `pyautogui.scroll()` já que é possível voltar para o
    inicio repetindo o hotkey para retornar ao item anterior SHIFT + TAB; evitando,
    também, problemas com diferentes resoluções de tela.

    3. Os tempos de time.sleep são curtos com propósitos de demonstração do funcionamento
    do script, pois em um cenário de produção é levado em conta possíveis atrasos no
    servidor ou na rede para carregar completamente o site.
"""

import os
import time

import pandas
import pyautogui

LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
USERNAME = "pythonimpressionador@gmail.com"
PASSWORD = "umasenhaextremamentesegura"

# Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
time.sleep(0.5)  # Nem sempre o sistema foca a barra de pesquisa instantaneamente
pyautogui.write("firefox")
time.sleep(0.5)  # Aguarda para garantir que o navegador seja selecionado
pyautogui.press("enter")
time.sleep(2)  # Aguarda o navegador abrir

# Passo 2: Fazer o login
pyautogui.write(LINK)
pyautogui.press("enter")
pyautogui.sleep(3)  # Aguarda o site carregar
pyautogui.press("tab")
pyautogui.write(USERNAME)
pyautogui.press("tab")
pyautogui.write(PASSWORD)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)  # Aguarda a conclusão do login e a atualização da página

# Passo 3: Abrir a base de dados
tabela = pandas.read_csv(f"{os.getcwd()}/projeto_01/produtos.csv")
tabela.index

# Passo 5: Repetir o passo 4 até acabar a lista de produtos
pyautogui.press("tab")
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])

    # Passo 4: Cadastrar um produto
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    pyautogui.write(custo)
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    for n in range(7):
        pyautogui.hotkey("shift", "tab")

    time.sleep(0.5)  # Aguarda a página atualizar por segurança
