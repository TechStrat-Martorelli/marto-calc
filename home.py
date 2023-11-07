import streamlit as st
from df import *
from graphs import *
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def render_home():
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Calculadora - Oportunidade Habilitações')
    
    st.write('')
    st.write('')

    with st.sidebar:
        filiados = st.text_input('Nº de Filiados', value=2000, key='filiados')
        media = st.text_input('Média por filiado', value=200000, key='media')
        percentual = st.text_input('Participação do Sindicato/Associação', value=0.05, key='percentual')
        curva = st.selectbox('Curva', ['Mais novos', 'Normal', 'Mais velhos'], index=1)

    filiados = int(filiados)
    media = int(media)
    percentual = float(percentual)

    df = criar_df(curva, filiados)

    def parseBRL(valor):
        return locale.currency(valor, grouping=True, symbol='R$ ')

    col1, col2, col3 = st.columns(3)
    
    col1.metric('Média por filiado', value=parseBRL(media))
    col2.metric('Participação', value= f'{percentual:.2%}')
    col3.metric('Oportunidade', value=parseBRL(valor_oportunidade(df,media,percentual)))

    st.write('')
    st.write('')

    r2c1, r2c2 = st.columns((6,4))
    r2c1.plotly_chart(barchart_vivos_e_falecidos(df))
    r2c2.plotly_chart(piechart_vivos_falecidos(df))


    st.write(f'A presente distribuição refere-se a {filiados} e uma distribuição {curva}.')
    #fig1 = criarBarChart_distribuicao(df)
    #st.pyplot(fig=fig1)
