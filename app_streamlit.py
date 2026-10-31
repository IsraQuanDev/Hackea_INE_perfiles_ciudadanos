import os
import json
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HACKEA LA PARTICIPACIÓN — Plataforma CCPC 2009–2024 (INE)",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Reducir márgenes superiores de Streamlit para que luzca como Web App nativa
st.markdown("""
<style>
  .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; max-width: 100% !important; }
  header[data-testid="stHeader"] { background: transparent !important; }
</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, "dashboard_ccpc_ine.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

# Reemplazar el script interno de gstatic por CDN público de Tailwind para que funcione en cualquier navegador externo también
html_for_browser = html_content.replace(
    'https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js',
    'https://cdn.tailwindcss.com'
)

# Asegurar variables CSS por defecto cuando se abre fuera de Antigravity en un navegador estándar
fallback_css = """
<style>
  :root {
    --background: #F8F7FC;
    --foreground: #181326;
    --card: #FFFFFF;
    --border: #E4DFEC;
    --muted-foreground: #5C5470;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --background: #0F0B1A;
      --foreground: #F4F0FF;
      --card: #1A1429;
      --border: #2E2545;
      --muted-foreground: #A39BB5;
    }
  }
</style>
"""
html_for_browser = html_for_browser.replace("</head>", fallback_css + "\n</head>")

# Guardar index.html listo para cualquier servidor web o hosting (Netlify/Vercel/GitHub Pages/Local)
with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_for_browser)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_for_browser)

components.html(html_for_browser, height=1350, scrolling=True)
