from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Dashboard MPP 2026",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

dashboard_path = Path(__file__).with_name("index_compartible.html")

if not dashboard_path.exists():
    st.error("No se encontró index_compartible.html junto a esta aplicación.")
    st.stop()

html = dashboard_path.read_text(encoding="utf-8")

# El dashboard es autocontenido; Streamlit solo lo hospeda dentro de un iframe.
components.html(html, height=2200, scrolling=True)
