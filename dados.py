"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_CSV = PASTA / "vulcoes.csv"

def ler_arquivo():
    vulcoes = []
    with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            vulcoes.append(linha)
    return vulcoes

def quantidade_vulcoes_por_pais(vulcoes):
    """Retorna um dicionário com a quantidade de vulcões por país."""
    contagem = {}
    for vulcao in vulcoes:
        pais = vulcao["pais"]
        if pais in contagem:
            contagem[pais] += 1
        else:
            contagem[pais] = 1
    return contagem
