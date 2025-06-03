import streamlit as st
import pandas
import folium
from streamlit_folium import st_folium

st.title("🎈 folium 테스트")

m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)
st_folium(m, width=700)
