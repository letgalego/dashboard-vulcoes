""" Dashboard com informacoes sobre vulcoes
"""
import streamlit as st
import dados

vulcoes = dados.ler_arquivo()

def montar_tabela(vulcoes):
    """montando a tabela com as colunas entituladas de uma forma mas legível"""
    tabela = []
    for vulcao in vulcoes:
        linha = {
            "Nome": vulcao["nome"],
            "Tipo": vulcao["tipo"],
            "Última Erupção": vulcao["ultima_erupcao"],
            "País": vulcao["pais"],
            "Região": vulcao["regiao"],
            "Altitude Média": vulcao["altitude_m"],
            "Latitude": vulcao["latitude"],
            "Longitude": vulcao["longitude"],
        }
        tabela.append(linha)
    return tabela

st.title("🌋 Dashboard de Vulcões")

vulcoes = dados.ler_arquivo()

col1, col2, col3, col4 = st.columns(4)

qtd_vulcoes = len(vulcoes)
col1.metric("Total de Vulcões", qtd_vulcoes)

st.dataframe(montar_tabela(vulcoes))