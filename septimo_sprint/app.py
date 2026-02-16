import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header("Análisis de anuncios de venta de vehículos en Estados Unidos")

build_histogram = st.button("Construir histograma")

if build_histogram:
    st.write("Creando un histograma para el conjunto de datos de anuncios de venta de vehículos en Estados Unidos")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
build_scatter = st.button("Construir gráfico de dispersión")

if build_scatter:
    st.write("Creando un gráfico de dispersión: Precio vs Odómetro")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
       