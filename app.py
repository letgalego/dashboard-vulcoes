""" Dashboard com informacoes sobre vulcoes """
import streamlit as st
import dados

def montar_tabela(vulcoes):
    """montando a tabela com as colunas entituladas de uma forma mas legível"""
    tabela = []
    for vulcao in vulcoes:
        linha = {
            "Nome": vulcao["nome"],
            "Tipo": vulcao["tipo"],
            "Última Erupção": padronizacao_ultima_erupcao(vulcao["ultima_erupcao"]),
            "País": vulcao["pais"],
            "Região": vulcao["regiao"],
            "Altitude (m)": vulcao["altitude_m"],
            "Faixa de Altitude": vulcao["faixa_altitude"],
            "Latitude": vulcao["latitude"],
            "Longitude": vulcao["longitude"],
        }
        tabela.append(linha)
    return tabela

def padronizacao_ultima_erupcao(erupcao):
    if erupcao != "Desconhecido":
        if erupcao < 0:
            return f"{abs(erupcao)} a.C."

    return erupcao

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
    add_selectbox = st.sidebar.selectbox(
    "Navegação:",
    ("HomePage", "Tipos de Vulcões")
    )

    #SIDEBAR DE TIPOS DE VULCÕES
    if add_selectbox == "Tipos de Vulcões":
        st.title("🌋 Tipos de Vulcões Mais Comuns")
        st.divider()
        
        st.subheader("Top 10 tipos mais comuns nos dados")
        ranking = dados.top_tipos(dados.ler_arquivo())
        st.bar_chart(
            [{"Tipo": tipo, "Quantidade": qtd} for tipo, qtd in ranking],
            x="Tipo",
            y="Quantidade",
        )
        st.divider()
        
        tipos_vulcao = dados.ler_tipos_de_vulcao()
        
        for linha in tipos_vulcao:
           st.header(linha["Tipo de Vulcão"])
           st.image(
               linha["Link da Foto"],
               caption=linha["Exemplo Famoso"]
           )
           st.markdown(f"Formato: {linha["Formato"]}")
           st.markdown(f"Tipo de Erupção: {linha["Tipo de Erupção"]}")
           st.divider()
    
    #SIDEBAR HOMEPAGE
    else:
        st.title("🌋 Dashboard de Vulcões")

        vulcoes = dados.ler_arquivo()

        col1, col2, col3, col4 = st.columns(4)
        
        pais_vulcoes, qtd_vulcoes_pais = dados.pais_com_mais_vulcoes(vulcoes)
        qtd_vulcoes = len(vulcoes)
        vulcao_recente = dados.vulcao_erupcao_mais_recente(vulcoes)

        col1.metric("Total de Vulcões", qtd_vulcoes)
        col2.metric("Países", len(dados.quantidade_vulcoes_por_pais(vulcoes)))
        col3.metric(label="País com mais vulcões", value=pais_vulcoes, delta=f"{qtd_vulcoes_pais} vulcões", delta_arrow="off")
        col4.metric(label="Vulcão com erupção mais recente", value=vulcao_recente["nome"], delta=f"País: {vulcao_recente["pais"]} | Ano: {vulcao_recente["ultima_erupcao"]}", delta_arrow="off")

        col_busca, col_filtro_tipo, col_filtro_regiao = st.columns(3)

        busca_nome = col_busca.text_input(label="🔎 Buscar pelo nome", type="search")
        opcao_tipo = col_filtro_tipo.selectbox("🏷️ Filtrar por tipo", ["Todos"] + listar_tipos(vulcoes))
        opcao_regiao = col_filtro_regiao.selectbox("🌍 Filtrar por região", ["Todas"] + listar_regioes(vulcoes))

        vulcoes_regiao = filtrar_por_regiao(vulcoes, opcao_regiao)
        vulcoes_tipo = filtrar_por_tipo(vulcoes_regiao, opcao_tipo)
        vulcoes_busca = busca_por_nome(vulcoes_tipo, busca_nome)

        if len(vulcoes_busca) == 0:
            st.warning("Nenhum vulcão encontrado!")
        else:
            st.caption(f"{len(vulcoes_busca)} vulcões encontrados")
            st.dataframe(montar_tabela(vulcoes_busca))



if __name__ == "__main__":
    main()