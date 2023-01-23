import streamlit as st 

#crear el titulo 
st.title("PROYECTO GRUPAL DTS05")


#st.sidebar.markdown("panel de metricas")
#st.siderbar.checkbox("kpi1")
with st.sidebar:
    st.title("PANEL DE METRICAS/KPIS")
    st.checkbox("KPI1")
    st.checkbox("COSTO POR PAQUETE")
    st.checkbox("DEMORA EN ENVIOS")
#st.sidebar()
st.markdown("***********")
#st.markdown()

if st.checkbox("mostrar diagrama er"):
    st.image("https://github.com/lulo76/Proyecto-Final-DTS--05/blob/main/Assets/Diagrama%20Entidad-Relacion.jpg?raw=true")


