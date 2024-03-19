import pandas as pd
import plotly as py
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import numpy as np



# Lista dos nomes dos arquivos CSV
nomes_arquivos = ['base1.csv', 'base2.csv', 'base3.csv', 'base4.csv', 'base5.csv', 'base6.csv', 'base7.csv']

# Lista para armazenar os DataFrames individuais
dataframes = []

# Iterar sobre cada arquivo CSV, ler e adicionar ao DataFrame
for nome_arquivo in nomes_arquivos:
    df = pd.read_csv(nome_arquivo)
    dataframes.append(df)

# Concatenar os DataFrames em um único DataFrame, empilhando-os verticalmente
results = pd.concat(dataframes, ignore_index=True)



# Criar guias
titulos_guias = ['Introdução', 'Modelagem dos Dados', 'DashBoard']
guia1, guia2, guia3 = st.tabs(titulos_guias)


# Adicionar conteúdo a cada guia
with guia1:
    st.header('PNAD-COVID 19')
    
    st.markdown('<hr style="border-top: 2px solid blue;">', unsafe_allow_html=True)
     
    st.subheader('Introdução')

    st.markdown("""
    
    Bem-vindo a análise dos dados do PNAD-COVID-19, uma pesquisa realizada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) durante a pandemia de COVID-19. Esta análise é de suma importância, pois nos permite compreender melhor o impacto da pandemia na população brasileira.

    Os dados do PNAD-COVID-19 abrangem uma variedade de tópicos, incluindo sintomas de saúde, comportamentos de prevenção, situação de emprego, e muito mais. Ao analisar esses dados, podemos obter insights valiosos sobre como a pandemia afetou diferentes segmentos da população e como as pessoas reagiram a essa crise sem precedentes.

    Convidamos você a se juntar a nós nesta análise. Seja você um pesquisador, estudante, profissional de saúde, ou simplesmente alguém interessado em aprender mais sobre a pandemia de COVID-19, acreditamos que você encontrará esta análise informativa e útil. 
    
    Vamos começar!
    """)

    st.markdown('<hr style="border-top: 2px solid blue;">', unsafe_allow_html=True)
    
    st.subheader('Pós Tech - FIAP')
    
    st.markdown('Created by:')       
    st.markdown('Leandro Castro - RM 350680')
    st.markdown('Mateus Correa - RM 351094')
    st.markdown('Tatiane Gandra - RM 352177' )
    
    
    with guia2:
        st.header('Modelagem dos Dados')
        
        st.markdown("""
    
        Para este trabalho, utilizamos as documentações e informações obtidas no site PNAD - Covid 19 (https://covid19.ibge.gov.br/pnad-covid/).

        A base de dados utilizada se encontra no site:
        https://basedosdados.org/dataset/c747a59f-b695-4d19-82e4-fef703e74c17?table=5894e1ac-dc08-465d-91a3-703683da85ba

        Nosso principal objetivo foi fazer uma análise sobre as informações disponíveis sobre a COVID 19, incluindo características clínicas de sintomas da doença, da população em geral e econômicas  da sociedade.

        Para iniciar a análise, o primeiro passo foi determinar as informações que seriam abordadas, e a partir disso, desenvolver uma query para trazer todas estas informações em uma tabela.

        SELECT 
        DATE(CONCAT(CONCAT(CONCAT(ano, '-'), LPAD(CAST(mes AS STRING), 2, '0')),'-', '01')) as ano_mes
        ,base.sigla_uf
        ,base.a002 as idade
        ,sexo.valor as sexo
        ,raca.valor as raca
        ,aula_p.valor as aula_presencial
        ,febre.valor as febre
        ,tosse.valor as tosse
        ,dor_garg.valor as dor_garganta
        ,olf_pal.valor as perda_olfato_paladar
        ,proc_ajuda.valor as procurou_ajuda 
        ,psa.valor as psa
        ,upa.valor as upa 
        ,hosp_sus.valor as hosp_pub
        ,amb_pvd_for_arm.valor as ambulatorio_pvd
        ,ps_pvd_for_arm.valor as pronto_soc_pvd
        ,hsp_pvd_for_arm.valor as hospital_pvd
        ,internou.valor as internou
        ,tem_plano.valor as tem_plano
        ,diabetes.valor as diabetes
        ,hipertensao.valor as hipertensao
        ,respiratoria.valor as respiratoria
        ,sem_doenca.valor as sem_doenca
        ,cardiaca.valor as cardiaca
        ,depressao.valor as depressao
        ,cancer.valor as cancer
        ,case
            when base.b009b = '1' or base.b009d = '1' or base.b009f = '1' then "Positivo"
            else "Negativo/Inconclusivo/Sem resultado" 
        end as resultado_testes
        ,base.b011 as medida_isolamento
        ,base.c001 as  trabalhou
        ,base.c013 as fez_home_office
        ,sabao.valor as sabao
        ,alcool.valor as alcool
        ,mascara.valor as mascaras
        ,luvas.valor as luvas
        ,agua_sanit_desinf.valor as agua_sanit_desinf
        ,avg(ifnull(base.d0013, 0) + ifnull(base.d0023, 0) + ifnull(base.d0033, 0) + ifnull(base.d0043, 0) + ifnull(base.d0053, 0) + ifnull(base.d0063, 0) + ifnull(base.d0073, 0)) as renda_media_total
        ,count(*) as quantidade
        FROM `basedosdados.br_ibge_pnad_covid.microdados` as base
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as sexo ON base.a003 = sexo.chave
        and sexo.nome_coluna = 'a003'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as raca ON base.a004 = raca.chave
        and raca.nome_coluna = 'a004'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as aula_p ON base.a006b = aula_p.chave
        and aula_p.nome_coluna = 'a006b'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as febre ON base.b0011 = febre.chave
        and febre.nome_coluna = 'b0011'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as tosse ON base.b0012 = tosse.chave
        and tosse.nome_coluna = 'b0012'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as dor_garg ON base.b0013 = dor_garg.chave
        and dor_garg.nome_coluna = 'b0013'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as olf_pal ON base.b00111 = olf_pal.chave
        and olf_pal.nome_coluna = 'b00111'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as proc_ajuda ON base.b002 = proc_ajuda.chave
        and proc_ajuda.nome_coluna = 'b002'                                                                            
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as psa ON base.b0041 = psa.chave
        and psa.nome_coluna = 'b0041'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as upa ON base.b0042 = upa.chave
        and upa.nome_coluna = 'b0042'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as hosp_sus ON base.b0043 = hosp_sus.chave
        and hosp_sus.nome_coluna = 'b0043'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as amb_pvd_for_arm ON base.b0044 = amb_pvd_for_arm.chave
        and amb_pvd_for_arm.nome_coluna = 'b0044'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as ps_pvd_for_arm ON base.b0045 = ps_pvd_for_arm.chave
        and ps_pvd_for_arm.nome_coluna = 'b0045'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as hsp_pvd_for_arm ON base.b0046 = hsp_pvd_for_arm.chave
        and hsp_pvd_for_arm.nome_coluna = 'b0046'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as internou ON base.b005 = internou.chave
        and internou.nome_coluna = 'b005'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as tem_plano ON base.b007 = tem_plano.chave
        and tem_plano.nome_coluna = 'b00111'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as diabetes ON base.b0101 = diabetes.chave
        and diabetes.nome_coluna = 'b0101'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as hipertensao ON base.b0102 = hipertensao.chave
        and hipertensao.nome_coluna = 'b0102'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as respiratoria ON base.b0103 = respiratoria.chave
        and respiratoria.nome_coluna = 'b0103'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as sem_doenca ON base.b0104 = sem_doenca.chave
        and sem_doenca.nome_coluna = 'b0104'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as cardiaca ON base.b0105 = cardiaca.chave
        and cardiaca.nome_coluna = 'b0105'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as depressao ON base.b0106 = depressao.chave
        and depressao.nome_coluna = 'b0106'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as cancer ON base.b0101 = cancer.chave
        and cancer.nome_coluna = 'b0101'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as sabao ON base.f002a1 = sabao.chave
        and sabao.nome_coluna = 'f002a1'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as alcool ON base.f002a2 = alcool.chave
        and alcool.nome_coluna = 'f002a2'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as mascara ON base.f002a3 = mascara.chave
        and mascara.nome_coluna = 'f002a3'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as luvas ON base.f002a4 = luvas.chave
        and luvas.nome_coluna = 'f002a4'
        LEFT JOIN `basedosdados.br_ibge_pnad_covid.dicionario` as agua_sanit_desinf ON base.f002a5 = agua_sanit_desinf.chave
        and agua_sanit_desinf.nome_coluna = 'f002a5'

        WHERE ano = 2020 -- filtra ano de 2020
        and mes in (9, 10, 11) -- filtra meses de setembro a novembro

        GROUP BY
        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35
        

        A tabela `basedosdados.br_ibge_pnad_covid.microdados` representa todas as respostas fornecidas pela população sobre o questionário a respeito da COVID 19, 
        pode ser denominada uma tabela fato (tabela que armazena fatos históricos como vendas, respostas de um questinário, eventos ou outras ações registráveis).
        Já a tabela `basedosdados.br_ibge_pnad_covid.dicionario` é uma tabela dimensão, e como o próprio nome diz, traz o significado ou descrição dos dados da tabela fato, 
        como por exemplo o que cada código de resposta, registrado na coluna chave, representa. A partir disso, podemos fazer JOIN entre as tabelas e trazer o resultado do 
        campo 'valor' para nossa tabela principal. Usamos duas funções de agregação, 'SUM' para trazer uma coluna que representa a quantidade de respostas que se
        enquadram nas condições de resposta do questionário de uma mesma linha de dados, e a função 'AVG' para trazer a média da soma de renda de uma família, que assim como
        na anterior se enquadra nas condições de resposta daquela linha.
        Por fim no filtro 'WHERE' definimos o ano e os meses a serem utilizados na análise e agrupamos as colunas a serem analisadas.
            """)
            
##############################################################################    
    
        with guia3:
            st.header('Dashboard PNAD-COVID 19')
            
            st.markdown('<hr style="border-top: 2px solid blue;">', unsafe_allow_html=True)

            st.subheader("Atendimento e Plano de Saúde")

            # Suponha que você tenha uma coluna 'ano_mes' no DataFrame
            unique_dates_list = results['ano_mes'].unique().tolist()

            # Filtrar os registros para incluir apenas as três datas únicas
            df_filtered = results[results['ano_mes'].isin(unique_dates_list)]

            # Agrupar por 'ano_mes' e somar os valores da coluna 'quantidade' para cada local
            data_counts = df_filtered.groupby('ano_mes').agg(
                psa_sum=('quantidade', lambda x: x[results['psa'] == 'Sim'].sum()),
                upa_sum=('quantidade', lambda x: x[results['upa'] == 'Sim'].sum()),
                hosp_pub_sum=('quantidade', lambda x: x[results['hosp_pub'] == 'Sim'].sum()),
                ambulatorio_pvd_sum=('quantidade', lambda x: x[results['ambulatorio_pvd'] == 'Sim'].sum()),
                pronto_soc_pvd_sum=('quantidade', lambda x: x[results['pronto_soc_pvd'] == 'Sim'].sum()),
                hospital_pvd_sum=('quantidade', lambda x: x[results['hospital_pvd'] == 'Sim'].sum())
            ).reset_index()

            # Criar o gráfico de barras
            fig = go.Figure(data=[
                go.Bar(name='UBS', x=data_counts['ano_mes'], y=data_counts['psa_sum']),
                go.Bar(name='UPA', x=data_counts['ano_mes'], y=data_counts['upa_sum']),
                go.Bar(name='Hospital Público', x=data_counts['ano_mes'], y=data_counts['hosp_pub_sum']),
                go.Bar(name='Ambulatório PVD', x=data_counts['ano_mes'], y=data_counts['ambulatorio_pvd_sum']),
                go.Bar(name='Pronto Socorro PVD', x=data_counts['ano_mes'], y=data_counts['pronto_soc_pvd_sum']),
                go.Bar(name='Hospital PVD', x=data_counts['ano_mes'], y=data_counts['hospital_pvd_sum'])
            ])

            # Adicionar título e rótulos aos eixos
            fig.update_layout(title='Locais de Atendimento por Dia',
                            xaxis_title='Data',
                            yaxis_title='Número de Pessoas',
                            width=800
            )
            # Renderizar o gráfico usando Streamlit
            st.plotly_chart(fig)

            
################################################################################

            # Importar bibliotecas necessárias
            import plotly.graph_objs as go

            # Coletar as datas únicas da coluna 'ano_mes'
            unique_dates_list = results['ano_mes'].unique()

            # Converter as datas para o formato de data para facilitar a manipulação
            unique_dates_list = pd.to_datetime(unique_dates_list)

            # Criar uma lista de datas mensais
            monthly_dates_list = pd.date_range(start=unique_dates_list.min(), end=unique_dates_list.max(), freq='MS').strftime('%Y-%m').tolist()

            # Filtrar as datas únicas para incluir apenas as datas mensais
            unique_dates_list = [date for date in unique_dates_list if date.strftime('%Y-%m') in monthly_dates_list]

            # Filtrar os registros onde a coluna 'procurou_ajuda' é 'Sim' e somar a coluna 'quantidade' agrupados por 'ano_mes'
            data_counts = results[results['procurou_ajuda'] == 'Sim'].groupby('ano_mes')['quantidade'].sum().reset_index()

            # Criar o gráfico de linhas
            fig = go.Figure(data=go.Scatter(x=data_counts['ano_mes'], y=data_counts['quantidade'], mode='lines'))

            # Definir a escala do eixo y para começar em 0
            fig.update_yaxes(range=[0, data_counts['quantidade'].max()])

            # Definir as datas mensais como marcadores do eixo x
            fig.update_xaxes(tickvals=unique_dates_list)

            # Adicionar título e rótulos aos eixos e ajustar a largura do gráfico
            fig.update_layout(title='Número de Pessoas que Procuraram Atendimento por Dia',
                            xaxis_title='Data',
                            yaxis_title='Número de Pessoas',
                            width=800)  # Definir a largura desejada aqui

            # Exiba o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)
            
#######################################################################################

            # Calcular a quantidade total de pessoas com e sem plano de saúde
            proporcao_tem_plano = results.groupby('tem_plano').agg({'quantidade': 'sum'}).reset_index()

            # Calcular a proporção de pessoas com e sem plano de saúde
            proporcao_tem_plano['proporcao'] = proporcao_tem_plano['quantidade'] / proporcao_tem_plano['quantidade'].sum()

            # Criar o gráfico de pizza
            fig = go.Figure(data=[go.Pie(labels=proporcao_tem_plano['tem_plano'], values=proporcao_tem_plano['proporcao'])])

            # Adicionar título ao gráfico
            fig.update_layout(title='Proporção de Pessoas com Plano de Saúde')

            # Exibir o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)         

            st.markdown('<hr style="border-top: 2px solid blue;">', unsafe_allow_html=True)

##############################################################################

            st.subheader("Internações")
      
            # Definir a lista de doenças
            doencas = ['diabetes', 'hipertensao', 'respiratoria', 'sem_doenca', 'cardiaca', 'depressao', 'cancer']

            # Inicializar uma lista para armazenar as internações por doença
            internacoes_por_doenca = []

            # Contar o número de internações para pessoas com e sem cada tipo de doença
            for doenca in doencas:
                internacoes_com_doenca = results[(results[doenca] == 'Sim') & (results['internou'] == 'Sim')]['quantidade'].sum()
                internacoes_sem_doenca = results[(results[doenca] == 'Não') & (results['internou'] == 'Sim')]['quantidade'].sum()
                internacoes_por_doenca.append((internacoes_com_doenca, internacoes_sem_doenca))

            # Criar o DataFrame
            df_internacoes = pd.DataFrame(internacoes_por_doenca, columns=['Com Doença', 'Sem Doença'], index=doencas)

            # Criar o gráfico de barras empilhadas
            fig = go.Figure(data=[
                go.Bar(name='Com Doença', x=df_internacoes.index, y=df_internacoes['Com Doença']),
                go.Bar(name='Sem Doença', x=df_internacoes.index, y=df_internacoes['Sem Doença'])
            ])

            # Adicionar título e rótulos aos eixos
            fig.update_layout(title='Relação entre Doenças Pré-existentes e Internações (Considerando a Quantidade)',
                            xaxis_title='Tipo de Doença',
                            yaxis_title='Número de Internações',
                            barmode='stack',
                            width=800)
            
            # Exibir o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)           

####################################################################

            # Calcular o total de pessoas por UF
            total_pessoas_por_uf = results.groupby('sigla_uf').agg({'quantidade': 'sum'}).reset_index()
            total_pessoas_por_uf.columns = ['sigla_uf', 'total_count']

            # Calcular a contagem de internações por UF
            contagem_internacoes_por_uf = results[results['internou'] == 'Sim'].groupby('sigla_uf').agg({'quantidade': 'sum'}).reset_index()
            contagem_internacoes_por_uf.columns = ['sigla_uf', 'internacao_count']

            # Juntar os dados de contagem de internações e total de pessoas por UF
            contagem_percentual_internacoes_por_uf = pd.merge(contagem_internacoes_por_uf, total_pessoas_por_uf, on='sigla_uf')

            # Calcular o percentual de internações por UF
            contagem_percentual_internacoes_por_uf['percentual_internacoes'] = (contagem_percentual_internacoes_por_uf['internacao_count'] / contagem_percentual_internacoes_por_uf['total_count']) * 100

            # Ordenar por percentual de internações (do maior para o menor)
            contagem_percentual_internacoes_por_uf = contagem_percentual_internacoes_por_uf.sort_values(by='percentual_internacoes', ascending=False)

            # Criar o gráfico de barras
            fig = px.bar(contagem_percentual_internacoes_por_uf, x='sigla_uf', y='percentual_internacoes',
                        title='Percentual de Internações por UF',
                        labels={'sigla_uf': 'UF', 'percentual_internacoes': 'Percentual de Internações'})

            # Exibir o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)


###################################################################

            # Filtrar os registros de internações
            internacoes = results[results['internou'] == 'Sim']

            # Coletar as idades e contar o número de internações para cada idade
            idades_internacoes = internacoes.groupby(internacoes['idade'].astype(int)).agg({'quantidade': 'sum'}).reset_index()
            idades_internacoes.columns = ['idade', 'total_internacoes']

            # Criar o histograma
            fig = go.Figure()

            # Adicionar o histograma
            fig.add_trace(go.Histogram(x=idades_internacoes['idade'], y=idades_internacoes['total_internacoes']))

            # Adicionar título e rótulos aos eixos
            fig.update_layout(title='Número de Internações por Idade (Histograma)',
                            xaxis_title='Idade',
                            yaxis_title='Número de Internações',
                            width=800)

            # Exibir o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)
            
                 
##############################################################################

            # Calcular o total de internações em todo o DataFrame
            total_internacoes = internacoes['quantidade'].sum()

            # Calcular o percentual de internações para cada faixa de idade
            idades_internacoes = internacoes.groupby(internacoes['idade'].astype(int)).agg({'quantidade': 'sum'}).reset_index()
            idades_internacoes.columns = ['idade', 'total_internacoes']
            idades_internacoes['percentual_internacoes'] = (idades_internacoes['total_internacoes'] / total_internacoes) * 100

            # Criar o histograma
            fig = go.Figure()

            # Adicionar o histograma
            fig.add_trace(go.Bar(x=idades_internacoes['idade'], y=idades_internacoes['percentual_internacoes']))

            # Adicionar título e rótulos aos eixos
            fig.update_layout(title='Percentual de Internações por Faixa de Idade',
                            xaxis_title='Idade',
                            yaxis_title='Percentual de Internações',
                            width=800)

            # Exibir o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)

            st.markdown('<hr style="border-top: 2px solid blue;">', unsafe_allow_html=True)
            
###############################################################################
            
            ###### Gráfico 1

            st.subheader("Distribuição Geográfica / Procuraram Ajuda Médica")

            # Defina os bins e labels
            bins = [0, 20, 40, 60, 80, 100]
            labels = ['0-20', '21-40', '41-60', '61-80', '81-100']

            # Converta a coluna 'idade' para inteiros
            results['idade'] = results['idade'].astype(int)

            # Agora, tente criar a coluna 'faixa_etaria' novamente
            results['faixa_etaria'] = pd.cut(results['idade'], bins=bins, labels=labels, right=False)

            # Agrupe por faixa etária e calcule a soma da coluna 'quantidade'
            results_grouped = results.groupby('faixa_etaria')['quantidade'].sum().reset_index()

            # Em seguida, agrupe por faixa etária e 'procurou_ajuda', e calcule a proporção
            results_prop = results.groupby(['faixa_etaria', 'procurou_ajuda'])['quantidade'].sum().unstack(fill_value=0)
            results_prop = results_prop.div(results_prop.sum(axis=1), axis=0) * 100

            # Crie o gráfico de barras lado a lado com cores específicas
            fig = px.bar(results_prop, x=results_prop.index, y=['Não', 'Sim'], barmode='group',
                        labels={'faixa_etaria': 'Faixa etária', 'value': 'Proporção (%)', 'procurou_ajuda': 'Procurou ajuda'},
                        title='Proporção de pessoas que procuraram ajuda médica por faixa etária')

            # Adicione legendas ao gráfico
            fig.update_layout(
                xaxis_title='Faixa etária',
                yaxis_title='Proporção (%)',
            )

            # Exiba o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)
            

    #######################################################################################
            
            ###### Gráfico 2

            
            # Agrupe os dados por 'sigla_uf' e calcule a soma da coluna 'quantidade' para cada estado
            df_grouped = results.groupby('sigla_uf')['quantidade'].sum().reset_index()

            # Crie o gráfico de barras
            fig = px.bar(df_grouped, x='sigla_uf', y='quantidade', labels={'sigla_uf': 'UF', 'quantidade': 'Número total de pessoas que procuraram ajuda médica'}, color_discrete_sequence=['lightblue'])

            # Adicione um título ao gráfico
            fig.update_layout(title='Número de pessoas que procuraram ajuda médica por UF')

            # Exiba o gráfico
            st.plotly_chart(fig)
            
######################################################################################

            # Calcular o total de pessoas por UF
            total_pessoas_por_uf = results.groupby('sigla_uf').agg({'quantidade': 'sum'}).reset_index()
            total_pessoas_por_uf.columns = ['sigla_uf', 'total_count']

            # Calcular a contagem de pessoas que buscaram atendimento por UF
            contagem_atendimento_por_uf = results[results['procurou_ajuda'] == 'Sim'].groupby('sigla_uf').agg({'quantidade': 'sum'}).reset_index()
            contagem_atendimento_por_uf.columns = ['sigla_uf', 'atendimento_count']

            # Juntar os dados de contagem de atendimento e total de pessoas por UF
            contagem_percentual_por_uf = pd.merge(contagem_atendimento_por_uf, total_pessoas_por_uf, on='sigla_uf')

            # Calcular o percentual de pessoas que buscaram atendimento por UF
            contagem_percentual_por_uf['percentual_atendimento'] = (contagem_percentual_por_uf['atendimento_count'] / contagem_percentual_por_uf['total_count']) * 100

            # Ordenar por percentual de atendimento (do maior para o menor)
            contagem_percentual_por_uf = contagem_percentual_por_uf.sort_values(by='percentual_atendimento', ascending=False)

            # Criar o gráfico de barras
            fig = px.bar(contagem_percentual_por_uf, x='sigla_uf', y='percentual_atendimento',
                        title='Percentual de Pessoas que procuraram ajuda médica por UF',
                        labels={'sigla_uf': 'UF', 'percentual_atendimento': 'Percentual de Pessoas que Buscaram Atendimento'})

            # Exibir o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)
            
    #################################################################################

            st.markdown('<hr style="border-top: 2px solid blue;">', unsafe_allow_html=True)

            st.subheader('Análise da Renda Média')

            ##### Gráfico 3

            
            # Agrupe os dados por raça e calcule a média da renda média total para cada raça
            df_grouped = results.groupby('raca')['renda_media_total'].mean().reset_index()

            # Crie o gráfico de barras
            fig = px.bar(df_grouped, x='raca', y='renda_media_total', labels={'raca': 'Raça', 'renda_media_total': 'Renda Média'},
                        title='Renda Média por Raça')

            # Adicione um título ao eixo y
            fig.update_yaxes(title='Renda Média')

            # Exiba o gráfico
            st.plotly_chart(fig)
            
            
    #############################################################################        

                    
            ##### Gráfico 4
    
            # Converta a coluna 'ano_mes' para o formato de data
            results['ano_mes'] = pd.to_datetime(results['ano_mes'])

            # Agrupe os dados por mês e sexo, e calcule a média da renda média total para cada mês e sexo
            df_grouped = results.groupby([results['ano_mes'].dt.strftime('%Y-%m'), 'sexo']).agg(renda_media_total=('renda_media_total', 'mean')).reset_index()

            # Crie o gráfico de barras
            fig = px.bar(df_grouped, x='ano_mes', y='renda_media_total', color='sexo',
                        labels={'ano_mes': 'Mês', 'renda_media_total': 'Renda Média', 'sexo': 'Sexo'},
                        title='Renda Média por Mês e Sexo')

            # Adicione um título ao eixo y
            fig.update_yaxes(title='Renda Média')

            # Exiba o gráfico
            st.plotly_chart(fig)

            
    
    #########################################################################################      
            
            ##### Gráfico 5

            # Primeiro, certifique-se de que 'ano_mes' esteja no formato correto. Se não estiver, converta-o.
            results['ano_mes'] = pd.to_datetime(results['ano_mes'])

            # Crie faixas etárias personalizadas
            bins = [20, 30, 40, 50, 60, 70, 80, float('inf')]
            names = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']

            results['faixa_etaria'] = pd.cut(results['idade'], bins, labels=names)

            # Agora, agrupe os dados por 'faixa_etaria' e calcule a média da renda para cada grupo
            grouped = results.groupby('faixa_etaria')['renda_media_total'].mean().reset_index()

            # Crie o gráfico de barras
            fig = px.bar(grouped, x='faixa_etaria', y='renda_media_total', labels={'faixa_etaria': 'Faixa Etária', 'renda_media_total': 'Renda Média'},
                        title='Renda Média por Faixa Etária')

            # Adicione um título ao eixo y
            fig.update_yaxes(title='Renda Média')

            # Exiba o gráfico
            st.plotly_chart(fig)
            
    ######################################################################################### 

            st.markdown('<hr style="border-top: 2px solid blue;">', unsafe_allow_html=True)

            st.subheader('Sexo e Cor/Raça')       

            ### Gráfico 6

            # Filtrando apenas as colunas relevantes
            df = results[['sexo', 'febre', 'tosse', 'dor_garganta', 'perda_olfato_paladar', 'quantidade']]

            # Convertendo os sintomas para o formato longo
            df_long = pd.melt(df, id_vars=['sexo', 'quantidade'], value_vars=['febre', 'tosse', 'dor_garganta', 'perda_olfato_paladar'], var_name='sintoma', value_name='presente')

            # Convertendo a coluna 'presente' para binário (1 para 'Sim' e 0 para 'Não')
            df_long['presente'] = df_long['presente'].apply(lambda x: 1 if x == 'Sim' else 0)

            # Multiplicando a quantidade pela presença do sintoma
            df_long['quantidade'] = df_long['quantidade'] * df_long['presente']

            # Agrupando por sexo, sintoma e somando a quantidade de pessoas para cada combinação
            df_grouped = df_long.groupby(['sexo', 'sintoma'])['quantidade'].sum().reset_index()

            # Criando o gráfico de barras empilhadas
            fig = px.bar(df_grouped, x='sintoma', y='quantidade', color='sexo', barmode='stack',
                        title='Comparação dos sintomas relatados entre homens e mulheres',
                        labels={'quantidade': 'Quantidade de Pessoas', 'sexo': 'Sexo', 'sintoma': 'Sintoma'})

            # Exibindo o gráfico no Streamlit
            st.plotly_chart(fig)


    #################################################

            ##### Gráfico 7

            # Agrupe os dados por raça e conte o número de pessoas que procuraram ajuda médica
            procurou_ajuda_por_raca = results.groupby('raca')['procurou_ajuda'].value_counts(normalize=True).unstack()

            # Remova a categoria 'Ignorado' se estiver presente nas colunas
            if 'Ignorado' in procurou_ajuda_por_raca.columns:
                procurou_ajuda_por_raca.drop(columns=['Ignorado'], inplace=True)

            # Remova a categoria 'Ignorado' se estiver presente nos índices
            if 'Ignorado' in procurou_ajuda_por_raca.index:
                procurou_ajuda_por_raca = procurou_ajuda_por_raca[procurou_ajuda_por_raca.index != 'Ignorado']

            # Crie o gráfico de barras lado a lado
            fig = go.Figure()

            for procurou_ajuda in ['Sim', 'Não']:
                fig.add_trace(go.Bar(
                    x=procurou_ajuda_por_raca.index,
                    y=procurou_ajuda_por_raca[procurou_ajuda],
                    name=procurou_ajuda
                ))

            # Altere o layout do gráfico
            fig.update_layout(
                barmode='group', 
                title='Proporção de pessoas por grupo racial que procuraram ajuda',
                xaxis_title="Raça",
                yaxis_title="Proporção de pessoas que procuraram ajuda médica",
                legend_title="Procurou ajuda médica"
            )

            # Exiba o gráfico
            st.plotly_chart(fig)
            
    ######################################################################
    
            st.markdown('<hr style="border-top: 2px solid blue;">', unsafe_allow_html=True)

            st.subheader('Resultado e Sintomas')

            # Calcular o total de respostas para cada categoria
            total_procurou_ajuda = results['procurou_ajuda'].eq('Sim').sum()
            total_resultado_testes = results['resultado_testes'].eq('Positivo').sum()
            total_internacao = results['internou'].eq('Sim').sum()

            # Calcular a porcentagem de cada categoria em relação ao total de respostas
            data_counts_4 = results[results['procurou_ajuda'] == 'Sim'].groupby('ano_mes').size().reset_index(name='count')
            data_counts_4['percent_procurou_ajuda'] = data_counts_4['count'] / total_procurou_ajuda

            data_counts_5 = results[results['resultado_testes'] == 'Positivo'].groupby('ano_mes').size().reset_index(name='count')
            data_counts_5['percent_resultado_testes'] = data_counts_5['count'] / total_resultado_testes

            data_counts_6 = results[results['internou'] == 'Sim'].groupby('ano_mes').size().reset_index(name='count')
            data_counts_6['percent_internacao'] = data_counts_6['count'] / total_internacao

            # Unir os DataFrames em um único DataFrame
            combined_data = data_counts_4.merge(data_counts_5, on='ano_mes', how='outer').merge(data_counts_6, on='ano_mes', how='outer')
            combined_data.fillna(0, inplace=True)

            # Criar o gráfico de linhas
            fig = go.Figure()

            # Adicionar cada linha ao gráfico
            fig.add_trace(go.Scatter(x=combined_data['ano_mes'], y=combined_data['percent_procurou_ajuda'], mode='lines', name='Procurou Ajuda'))
            fig.add_trace(go.Scatter(x=combined_data['ano_mes'], y=combined_data['percent_resultado_testes'], mode='lines', name='Resultado Testes'))
            fig.add_trace(go.Scatter(x=combined_data['ano_mes'], y=combined_data['percent_internacao'], mode='lines', name='Internação'))

            # Adicionar título e rótulos aos eixos
            fig.update_layout(title='Comparação de Dados em Percentual',
                            xaxis_title='Data',
                            yaxis_title='Percentual (%)',          
                            width=800)
            
            # Exiba o gráfico dentro do aplicativo Streamlit
            st.plotly_chart(fig)

######################################################################################

            sintomas = ['febre', 'tosse', 'dor_garganta', 'perda_olfato_paladar']
            procurou_ajuda_values = ['Sim', 'Não']  # Definindo explicitamente os valores

            data = []
            for procurou_ajuda_value in procurou_ajuda_values:
                proporcao_data = []
                for sintoma in sintomas:
                    # Filtrar os dados para excluir linhas com valores nulos ou vazios
                    filtered_data = results.dropna(subset=[sintoma, 'procurou_ajuda', 'quantidade'])
                    # Contar o total de pessoas com o sintoma
                    total_sintoma = len(filtered_data[filtered_data[sintoma] == 'Sim'])
                    # Contar o total de pessoas que procuraram ajuda e têm o sintoma
                    total_procurou_ajuda = len(filtered_data[(filtered_data[sintoma] == 'Sim') & (filtered_data['procurou_ajuda'] == procurou_ajuda_value)])
                    # Calcular a proporção
                    proporcao = total_procurou_ajuda / total_sintoma if total_sintoma != 0 else 0
                    proporcao_data.append(proporcao)
                data.append(go.Bar(name=procurou_ajuda_value, x=sintomas, y=proporcao_data))

            fig = go.Figure(data=data)
            fig.update_layout(barmode='group', title='Proporção de Pessoas por Procura de Ajuda e Sintomas',
                            xaxis_title='Sintomas',
                            yaxis_title='Proporção de Pessoas')

            # Mostrar o gráfico no Streamlit
            st.plotly_chart(fig)           

    #########################################################################

            ######### Gráfico 9
    
            sintomas = ['febre', 'tosse', 'dor_garganta', 'perda_olfato_paladar']
            procurou_ajuda_values = ['Sim', 'Não']  # Definindo explicitamente os valores

            data = []
            for procurou_ajuda_value in procurou_ajuda_values:
                procurou_ajuda_data = []
                for sintoma in sintomas:
                    # Filtrar os dados para excluir linhas com valores nulos ou vazios
                    filtered_data = results.dropna(subset=[sintoma, 'procurou_ajuda', 'quantidade'])
                    # Remover espaços em branco
                    filtered_data = filtered_data.replace(r'^\s*$', 'NaN', regex=True)
                    # Somar os valores da coluna 'quantidade' para o sintoma e cada valor da coluna 'procurou_ajuda'
                    total_quantity = filtered_data.loc[(filtered_data['procurou_ajuda'] == procurou_ajuda_value) & (filtered_data[sintoma] == 'Sim'), 'quantidade'].sum()
                    procurou_ajuda_data.append(total_quantity)
                data.append(go.Bar(name=procurou_ajuda_value, x=sintomas, y=procurou_ajuda_data))

            fig = go.Figure(data=data)
            fig.update_layout(barmode='group', title='Quantidade de Pessoas por Procura de Ajuda e Sintomas',
                            xaxis_title='Sintomas',
                            yaxis_title='Quantidade de Pessoas')

            # Mostrar o gráfico no Streamlit
            st.plotly_chart(fig)

           
#############################################################################
            
            # Filtrando apenas as colunas relevantes
            df = results[['resultado_testes', 'fez_home_office', 'quantidade']]

            # Agrupando por resultado de teste e se fez home office e somando a quantidade de pessoas para cada combinação
            df_grouped = df.groupby(['resultado_testes', 'fez_home_office'])['quantidade'].sum().unstack(fill_value=0)

            # Crie o gráfico de barras lado a lado
            fig = go.Figure()

            for fez_home_office in df_grouped.columns:
                fig.add_trace(go.Bar(
                    x=df_grouped.index,
                    y=df_grouped[fez_home_office],
                    name="Fez home office" if fez_home_office == 1 else "Não fez home office"
                ))

            # Altere o layout do gráfico
            fig.update_layout(
                barmode='group', 
                title='Relação entre resultado de testes e home office',
                xaxis_title="Resultado de Testes",
                yaxis_title="Quantidade de pessoas",
                legend_title="Fez home office?"
            )

            # Exiba o gráfico
            st.plotly_chart(fig)
