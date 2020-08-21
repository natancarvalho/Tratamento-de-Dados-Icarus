# Importando bibliotecas para análise
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go

#Importando os dados para os dataframes
aceleracao1 = pd.read_csv('./RaceStudio_15_03_20_Manha_Aceleracao1_F19_Bigode.csv')
aceleracao2 = pd.read_csv('./RaceStudio_15_03_20_Manha_Aceleracao2_F19_Bigode.csv')

#Mostrando a quantidade de linhas o colunas dos dataframes
print(aceleracao1.shape)
print(aceleracao2.shape)

#Removendo dados de RPM com velocidade abaixo de 10Km/h
#aceleracao1 = aceleracao1.drop(aceleracao1[(aceleracao1.GPS_Speed < 10)].index)
#aceleracao2 = aceleracao2.drop(aceleracao2[(aceleracao2.GPS_Speed < 10)].index)

#Removendo dados de RPM com velocidade abaixo de 20Km/h
aceleracao1 = aceleracao1.drop(aceleracao1[(aceleracao1.GPS_Speed < 20)].index)
aceleracao2 = aceleracao2.drop(aceleracao2[(aceleracao2.GPS_Speed < 20)].index)

#Montando o histograma
fig = go.Figure()
fig.add_trace(go.Histogram(x=aceleracao1['RPM'], name = 'Aceleração 1'))
fig.add_trace(go.Histogram(x=aceleracao2['RPM'], name = 'Aceleração 2'))

# Overlay both histograms
fig.update_layout(barmode='overlay')
# Reduce opacity to see both histograms
fig.update_traces(opacity=0.75)
fig.show()