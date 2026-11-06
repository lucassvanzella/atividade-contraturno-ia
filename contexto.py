def carregar_contexto(caminho: str = "contexto.txt") -> str:
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            texto = arquivo.read().strip()
    except FileNotFoundError:
        print(f"Aviso: arquivo '{caminho}' não encontrado. Seguindo sem contexto.")
        return ""