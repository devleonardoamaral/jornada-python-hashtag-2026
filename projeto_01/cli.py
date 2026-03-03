"""
Módulo com funções utilitárias para CLI.
"""


def mostrar_ajuda() -> None:
    print(
        "\n".join(
            [
                "Registra os produtos no site da empresa através de automação.",
                "   -h, --help                      Exibe este texto de ajuda.",
                "   -n, --navegador <navegador>     Define qual navegador será utilizado.",
            ]
        )
    )


def mostrar_uso() -> None:
    print("Uso: python -m projeto_01 [OPÇÃO]... [ARGUMENTO]")
