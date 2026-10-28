"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_CSV = PASTA / "vulcoes.csv"
CAMINHO_CSV2 = PASTA / "tipos.csv"

def converter_numero(valor):
    """Converte texto do CSV em número. Retorna None se estiver vazio ou inválido."""
    try:
        return float(valor)
    except (TypeError, ValueError):
        return None


def classificar_altitude(altitude):
    """Devolve a faixa de altitude de um vulcão."""
    if altitude is None:
        return "Sem dados"
    if altitude < 1000:
        return "Baixa (< 1000 m)"
    if altitude < 3000:
        return "Média (1000 a 2999 m)"
    return "Alta (≥ 3000 m)"


def converter_colunas(vulcoes):
    """Converte as colunas e cria a faixa de altitude."""
    for vulcao in vulcoes:
        vulcao["altitude_m"] = converter_numero(vulcao["altitude_m"])
        vulcao["latitude"] = converter_numero(vulcao["latitude"])
        vulcao["longitude"] = converter_numero(vulcao["longitude"])
        vulcao["faixa_altitude"] = classificar_altitude(vulcao["altitude_m"])
        vulcao["tipo"] = padronizar_tipo(vulcao["tipo"])
        vulcao["ultima_erupcao"] = padronizar_erupcao(vulcao["ultima_erupcao"])
    return vulcoes

def ler_arquivo():
    vulcoes = []
    with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            vulcoes.append(linha)
    return converter_colunas(vulcoes)

def ler_tipos_de_vulcao():
    tipos = []
    with open(CAMINHO_CSV2, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        for linha in leitor:
            tipos.append(linha)
    return tipos

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

def pais_com_mais_vulcoes(vulcoes):
    """Retorna o nome do país com maior quantidade de vulcões, e também, sua quantidade."""
    contagem = quantidade_vulcoes_por_pais(vulcoes)

    pais_mais_vulcoes = max(contagem, key=contagem.get) # pega o pais com a > quantidade de vulcoes, o max() compara 
                                                        # todos os valores da contagem e retorna a chave com o maior valor
    return pais_mais_vulcoes, contagem[pais_mais_vulcoes]

def padronizar_tipo(tipo):
    tipos = {
        "Stratovolcano(es)": "Stratovolcano",
        "Shield(s)": "Shield",
        "Caldera(s)": "Caldera",
        "Complex(es)": "Complex",
        "Lava cone(es)": "Lava cone",
        "Lava cone(s)": "Lava cone",
        "Lava dome(s)": "Lava dome",
        "Pyroclastic cone(s)": "Pyroclastic cone",
        "Tuff cone(s)": "Tuff cone",
    }
    if tipo in tipos:
        return tipos[tipo]

    return tipo

def padronizar_erupcao(erupcao):
    if erupcao == "Unknown":
        return "Desconhecido"

    return int(erupcao)

def vulcao_erupcao_mais_recente(vulcoes):
    vulcao_recente = vulcoes[0]

    for vulcao in vulcoes:
        if vulcao["ultima_erupcao"] != "Desconhecido":
            if vulcao["ultima_erupcao"] > vulcao_recente["ultima_erupcao"]:
                vulcao_recente = vulcao

    return vulcao_recente

if __name__ == "__main__":

    vulcoes = ler_arquivo()

    pais_mais_vulcoes, quantidade_maior_pais = pais_com_mais_vulcoes(vulcoes)

    print(pais_mais_vulcoes, quantidade_maior_pais)

    print(type(vulcoes[0]["ultima_erupcao"]))
    print(ler_tipos_de_vulcao())