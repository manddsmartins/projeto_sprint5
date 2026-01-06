import streamlit as st
import pandas as pd 
import plotly.express as px

#Dados        
car_data = pd.read_csv('/home/mandsmartins/Documentos/Projeto sprint 5/projeto_sprint5/vehicles.csv') 

#Cabeçalho
st.header('Dashboard de Análise de Veículos')

#Botão Histograma
hist_button = st.button('Criar histograma')

#Ação do botão  
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')         
    fig = px.histogram(car_data, x="odometer")    
    st.plotly_chart(fig, use_container_width=True)

#Botão Gráfico de Dispersão
scatter_button = st.button('Criar gráfico de dispersão')

#Ação do botão
if scatter_button:
    st.write('Criando um gráfico de dispersão')
    fig_scatter = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )
    st.plotly_chart(fig_scatter, use_countainer_width=True)

    