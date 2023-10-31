import streamlit as st
from functions import *

def render_home():
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Calculadora - Oportunidade Habilitações')

    with st.sidebar:
        filiados = st.text_input('Nº de Filiados', value=2000, key='filiados')
        st.text_input('Média por filiado', key='media')
        st.text_input('Participação do Sindicato/Associação', key='percentual')
        curva = st.selectbox('Curva', ['Mais novos', 'Normal', 'Mais velhos'], index=1)
        st.text_input('Previsão para o ano', key='ano')

    if curva == 'Mais novos':
        curva = 30
    elif curva == 'Normal':
        curva = 55
    elif curva == 'Mais velhos':
        curva = 75

    df = criar_df(curva, int(filiados))
    
    st.write(f'A presente distribuição refere-se a {filiados} e uma distribuição {curva}.')
    fig1 = criarBarChart_distribuicao(df)
    st.pyplot(fig=fig1)

    st.write(f'Demonstração da distribuição aprox. dos filiados conforme expectativa de vida.')
    pivot_table = pivotarContagemIdade(df)
    fig2 = criarBarChart_vivos_e_falecidos(pivot_table)

    st.pyplot(fig=fig2)