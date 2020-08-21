# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st
import plotly.offline as py
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
teste = pd.read_csv('./1final_comparacaoentrecurvas.csv')
JaguarLap1 = pd.read_csv('./JaguarLap1.csv')
JaguarLap2 = pd.read_csv('./JaguarLap2.csv')
JaguarLap3 = pd.read_csv('./JaguarLap3.csv')
JaguarLap4 = pd.read_csv('./JaguarLap4.csv')
JaguarLap5 = pd.read_csv('./JaguarLap5.csv')
JaguarLap6 = pd.read_csv('./JaguarLap6.csv')
JaguarLap7 = pd.read_csv('./JaguarLap7.csv')

print(teste.shape)

JaguarLap7 = JaguarLap7.drop(JaguarLap7[JaguarLap7.LatAcc < -2].index)

#Gráfico de Graham Bell 31mm
trace1 = go.Scatter(x = teste['rpm'], y = teste['graham_bell_31mm'], name = 'graham_bell_31mm', mode = 'lines')
# Gráfico de Graham Bell 41mm
trace2 = go.Scatter(x = teste['rpm'], y = teste['graham_bell_41mm'], name = 'graham_bell_41mm', mode = 'lines')
# Gráfico de Junções Calculadas
trace3 = go.Scatter(x = teste['rpm'], y = teste['JuncoesCalculadas'], name = 'JuncoesCalculadas', mode = 'lines')
# Gráfico de União 7 graus
trace4 = go.Scatter(x = teste['rpm'], y = teste['uniao_7 graus'], name = 'uniao_7 graus', mode = 'lines')
#Gráfico Final 270mm
trace5 = go.Scatter(x = teste['rpm'], y = teste['final_270mm'], name = 'final_270mm', mode = 'lines')

data = [trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(title = 'Comparação Final',
                   titlefont = {'family': 'Arial',
                                'size': 22,
                                'color': '#7f7f7f'},
                   xaxis = {'title': 'RPM'},
                   yaxis = {'title': 'N*M'},
                   paper_bgcolor = 'rgb(243, 243, 243)',
                   plot_bgcolor = 'rgb(243, 243, 243)')
fig2 = go.Figure(data=data, layout=layout)
py.iplot(fig2)

# Gerando gráficos para casas que tem 1 quarto
trace1 = go.Scatter(x = JaguarLap1['LatAcc'], y = JaguarLap1['LongAcc']*-1, name = 'Volta 1', mode = 'markers')
# Gráfico de caixa para casas com 2 quartos
trace2 = go.Scatter(x = JaguarLap2['LatAcc'], y = JaguarLap2['LongAcc']*-1, name = 'Volta 2', mode = 'markers')
# Gráfico de caixa para casas com 3 quartos
trace3 = go.Scatter(x = JaguarLap3['LatAcc'], y = JaguarLap3['LongAcc']*-1, name = 'Volta 3', mode = 'markers')
# Gráfico para casas de quatro quartos
trace4 = go.Scatter(x = JaguarLap4['LatAcc'], y = JaguarLap4['LongAcc']*-1, name = 'Volta 4', mode = 'markers')
# Gráfico para casas de quatro quartos
trace5 = go.Scatter(x = JaguarLap5['LatAcc'], y = JaguarLap5['LongAcc']*-1, name = 'Volta 5', mode = 'markers')
# Gráfico para casas de quatro quartos
trace6 = go.Scatter(x = JaguarLap6['LatAcc'], y = JaguarLap6['LongAcc']*-1, name = 'Volta 6', mode = 'markers')
# Gráfico para casas de quatro quartos
trace7 = go.Scatter(x = JaguarLap7['LatAcc'], y = JaguarLap7['LongAcc']*-1, name = 'Volta 7', mode = 'markers')

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]
layout = go.Layout(title = 'Grafico GG Volta a Volta',
                   titlefont = {'family': 'Arial',
                                'size': 22,
                                'color': '#7f7f7f'},
                   xaxis = {'title': 'Aceleração Lateral'},
                   yaxis = {'title': 'Aceleração Longitudinal'},
                   paper_bgcolor = 'rgb(243, 243, 243)',
                   plot_bgcolor = 'rgb(243, 243, 243)')
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

app.layout = html.Div(children=[
    html.H1(children='Teste de atualização'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example2-graph',
        figure=fig2
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)