"""
Módulo com funções de depuração.
"""

import pyautogui


def show_mouse_position() -> None:
    """Função de depuração para obter a localização autal do mouse na tela."""
    pos = pyautogui.position()
    print(f"x = {pos.x}, y = {pos.y}")
