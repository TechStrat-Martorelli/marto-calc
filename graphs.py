import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def valor_oportunidade(df, media, percentual):
    return df['falecidos'].sum() * media * percentual

def barchart_vivos_e_falecidos(df):

    pivot_table = df.pivot_table(index='faixa', values=['falecidos', 'vivos'], aggfunc='sum')

    # Reorder the columns in the desired order
    faixas_ordenadas = ['até 30', '31 a 50', '51 a 70', '71 a 90']
    pivot_table = pivot_table.loc[faixas_ordenadas]

    fig = px.bar(pivot_table, x=pivot_table.index, y=['falecidos', 'vivos'],
                 title='Relação vivos e falecidos por Faixa Etária',
                 labels={'value': 'Faixa Etária', 'value': 'Quantidade'},
                 color_discrete_map={'falecidos': 'red', 'vivos': 'blue'},
                 #text=[pivot_table['falecidos'], pivot_table['vivos']],
                 category_orders={'faixa': faixas_ordenadas}
                )

    fig.update_layout(
        xaxis_title_text='Faixa Etária',
        yaxis_title_text='Quantidade',
        legend_title_text='Legenda',
        font=dict(color='white'),
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)'
    )

    fig.update_traces(textposition='outside')
    fig.update_xaxes(tickangle=45)

    return fig

def piechart_vivos_falecidos(df):
    # Calculate the total number of 'vivos' and 'falecidos'
    total_vivos = df['vivos'].sum()
    total_falecidos = df['falecidos'].sum()

    # Create a 3D pie chart
    labels = ['Vivos', 'Falecidos']
    sizes = [total_vivos, total_falecidos]
    colors = ['blue', 'red']

    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, pull=[0, 0.1], textinfo='percent+label', 
                                 marker=dict(colors=colors))])

    fig.update_layout({
        'title':'Distribuição de Filiados',
        'title_font_color':'white',
        'paper_bgcolor':'rgba(0, 0, 0, 0)',
        'scene': dict(
            xaxis=dict(showticklabels=False, showgrid=False, title=''),
            yaxis=dict(showticklabels=False, showgrid=False, title=''),
            zaxis=dict(showticklabels=False, showgrid=False, title='')
        )
    })

    return fig