"""
Módulo __main__: executa o módulo.
"""

import os
import sys

from . import arquivo, automacao, cli

LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
USERNAME = "pythonimpressionador@gmail.com"
PASSWORD = "umasenhaextremamentesegura"
TABELA_FILE = f"{os.getcwd()}/projeto_01/produtos.csv"
navegador = "firefox"

# Processa argumentos CLI
for index in range(len(sys.argv)):
    cli_cmd = sys.argv[index]

    if cli_cmd in ("--help", "-h"):
        cli.mostrar_uso()
        cli.mostrar_ajuda()
        exit()
    elif cli_cmd in ("-n", "--navegador"):
        if (index + 1) >= len(sys.argv):
            cli.mostrar_uso()
            raise ValueError("Navegador não especificado.")

        navegador = sys.argv[index + 1]

# Passo 1: Abrir o navegador
automacao.abrir_navegador(navegador)

# Passo 2: Fazer o login
automacao.abrir_link_no_navegador(LINK)
automacao.realizar_login(USERNAME, PASSWORD)

# Passo 3: Conectar ao banco de dados
tabela = arquivo.carregar_tabela(TABELA_FILE)

# Passo 4: Registrar produtos
automacao.carregar_produtos_da_tabela(tabela)
