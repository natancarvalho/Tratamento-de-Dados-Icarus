import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st
import plotly.offline as py
import plotly.graph_objs as go

#from scipy.special import boxcox1p

teste = pd.read_csv('./1final_comparacaoentrecurvas.csv')
print(teste.shape)

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
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)