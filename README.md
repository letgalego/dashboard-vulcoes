# dashboard-vulcoes

# Nome do app

**Membros:** Bruna Steffens, Leticia Galego, Nathany Ferreira
**Dataset:** vulcoes.csv + volcano.si.edu
**App publicado:** https://...streamlit.app
## Funcionalidades
- [] Leitura do CSV
- [] Conversão das colunas
- [] Mostrar no mínimo 3 métricas sobre o dataset
- [] Classificar os registros em faixas a partir de uma coluna numérica e mostrar a faixa na tabela
- [] Uma tabela com os dados e nomes de coluna legíveis
- [] Uma busca por texto que não diferencie maiúsculas de minúsculas
- [] Um filtro por categoria, com as opções dos próprios dados (sem escrever à mão) e uma opção para
mostrar todos
- [] Busca e filtro funcionando juntos
- [] Uma mensagem quando nenhum resultado for encontrado
- [] Código organizado em funções e módulos, com nomes que façam sentido no tema do grupo
- [] App publicado no Streamlit Community Cloud
## Funcionalidade extra
Menu lateral com uma nova página com os tipos de vulcões mais comuns (top 10)
## Como rodar
Clique em Fork (canto superior direito) para criar a sua cópia deste repositório.
No VS Code: Ctrl+Shift+P → Git: Clone → cole o link do seu fork.
No terminal do VS Code (PowerShell), dentro da pasta do repositório:
´´´
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # libera o script de ativação só nesta janela
.venv\Scripts\Activate.ps1
pip install -r dashboard-vulcoes/requirements.txt
streamlit run dashboard-vulcoes/app.py
´´´