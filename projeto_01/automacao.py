"""
Módulo que disponibiliza métodos que realizam automações utilizando PyAutoGui.
"""

import time

import pandas
import pyautogui


def abrir_navegador(navegador: str) -> None:
    pyautogui.press("win")
    time.sleep(0.5)  # Nem sempre o sistema foca a barra de pesquisa instantaneamente
    pyautogui.write(navegador)
    time.sleep(0.5)  # Aguarda para garantir que o navegador seja selecionado
    pyautogui.press("enter")
    time.sleep(2)  # Aguarda o navegador abrir


def abrir_link_no_navegador(link: str) -> None:
    pyautogui.write(link)
    pyautogui.press("enter")
    pyautogui.sleep(3)  # Aguarda o site carregar


def realizar_login(username: str, password: str) -> None:
    pyautogui.press("tab")
    pyautogui.write(username)
    pyautogui.press("tab")
    pyautogui.write(password)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)  # Aguarda a conclusão do login e a atualização da página


def carregar_produto(index: int, tabela: pandas.DataFrame) -> None:
    codigo = str(tabela.loc[index, "codigo"])
    marca = str(tabela.loc[index, "marca"])
    tipo = str(tabela.loc[index, "tipo"])
    categoria = str(tabela.loc[index, "categoria"])
    preco_unitario = str(tabela.loc[index, "preco_unitario"])
    custo = str(tabela.loc[index, "custo"])
    obs = str(tabela.loc[index, "obs"])

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


def carregar_produtos_da_tabela(tabela: pandas.DataFrame) -> None:
    pyautogui.press("tab")

    for index in tabela.index:
        carregar_produto(index, tabela)

        for _ in range(7):
            pyautogui.hotkey("shift", "tab")

        time.sleep(0.5)  # Aguarda a página atualizar por segurança
