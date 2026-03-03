"""
Módulo que disponibiliza funções para carregar arquivos.
"""

import pandas


def carregar_tabela(path) -> pandas.DataFrame:
    return pandas.read_csv(path)
