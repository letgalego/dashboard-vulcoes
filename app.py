""" Dashboard com informacoes sobre vulcoes
"""
import streamlit as st
import dados

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
            "Altitude (m)": vulcao["altitude_m"],
            "Faixa de Altitude": vulcao["faixa_altitude"],
            "Latitude": vulcao["latitude"],
            "Longitude": vulcao["longitude"],
        }
        tabela.append(linha)
    return tabela

def listar_tipos(vulcoes):
    """Junta todos os tipos de vulcoes em uma lista"""
    tipos = []
    for vulcao in vulcoes:
        if vulcao["tipo"] not in tipos:
            tipos.append(vulcao["tipo"])

    tipos.sort()
    return tipos

def listar_regioes(vulcoes):
    """Junta todos as regioes de vulcoes em uma lista"""
    regioes = []
    for vulcao in vulcoes:
        if vulcao["regiao"] not in regioes:
            regioes.append(vulcao["regiao"])

    regioes.sort()
    return regioes

def busca_por_nome(vulcoes, busca):
    """Retorna vulcões que tem a busca no nome."""
    vulcoes_encontrados = []
    for vulcao in vulcoes:
        if busca.lower() in vulcao["nome"].lower():
            vulcoes_encontrados.append(vulcao)

    return vulcoes_encontrados

def filtrar_por_tipo(vulcoes, tipo):
    """Filtra os vulcoes e seleciona os vulcoes de acordo com o tipo pedido."""
    if tipo == "Todos":
        return vulcoes

    vulcoes_encontrados = []

    for vulcao in vulcoes:
        if tipo == vulcao["tipo"]:
            vulcoes_encontrados.append(vulcao)
    return vulcoes_encontrados


def filtrar_por_regiao(vulcoes, regiao):
    """Filtra os vulcoes e seleciona os vulcoes de acordo com a regiao pedida."""
    if regiao == "Todas":
        return vulcoes

    vulcoes_encontrados = []

    for vulcao in vulcoes:
        if regiao == vulcao["regiao"]:
            vulcoes_encontrados.append(vulcao)
    return vulcoes_encontrados

def main():
    st.set_page_config(page_title="Dashboard de Vulcões", page_icon="🌋", layout="wide")
    st.title("🌋 Dashboard de Vulcões")

    vulcoes = dados.ler_arquivo()

    col1, col2, col3, col4 = st.columns(4)

    pais_vulcoes, qtd_vulcoes_pais = dados.pais_com_mais_vulcoes(vulcoes)

    qtd_vulcoes = len(vulcoes)
    col1.metric("Total de Vulcões", qtd_vulcoes)
    col2.metric("Países", len(dados.quantidade_vulcoes_por_pais(vulcoes)))
    col3.metric("País com mais vulcões", pais_vulcoes, f"{qtd_vulcoes_pais} vulcões")

    col_busca, col_filtro_tipo, col_filtro_regiao = st.columns(3)

    busca_nome = col_busca.text_input(label="🔎 Buscar pelo nome", type="search")
    opcao_tipo = col_filtro_tipo.selectbox("Filtrar por tipo", ["Todos"] + listar_tipos(vulcoes))
    opcao_regiao = col_filtro_regiao.selectbox("Filtrar por região", ["Todas"] + listar_regioes(vulcoes))

    vulcoes_regiao = filtrar_por_regiao(vulcoes, opcao_regiao)
    vulcoes_tipo = filtrar_por_tipo(vulcoes_regiao, opcao_tipo)
    vulcoes_busca = busca_por_nome(vulcoes_tipo, busca_nome)

    if len(vulcoes_busca) == 0:
        st.warning("Nenhum vulcão encontrado!")
    else:
        st.caption(f"{len(vulcoes_busca)} livros encontrados")
        st.dataframe(montar_tabela(vulcoes_busca))



if __name__ == "__main__":
    main()