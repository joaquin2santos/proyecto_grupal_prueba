import streamlit as st
import pandas as pd 

df_order_items= pd.read_csv('https://raw.githubusercontent.com/lulo76/Proyecto-Final-DTS--05/main/Week%201/Datasets/olist_order_items_dataset.csv')

if st.checkbox("Mostrar dataframe"):
    st.dataframe(df_order_items)

if st.button("Mostrar una fila al azar"):
    st.write(df_order_items.sample())
#st.radio('dimension que queresmos mostrar', (filas, columnas)) #se agrega en una tupla