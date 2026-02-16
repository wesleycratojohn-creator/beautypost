import streamlit as st
import random
import base64
from PIL import Image
import os
import pandas as pd
from datetime import datetime

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(
    page_title="Lu Bezerra | Global Trichology & Luxury Spa",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTILIZAÇÃO CSS ULTRA-SOFISTICADA =================
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@200;400;600&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

        /* Reset e Fontes Globais */
        html, body, [class*="st-"] {
            font-family: 'Montserrat', sans-serif;
            color: #2C2C2C;
        }
        h1, h2, h3, .luxury-title {
            font-family: 'Cinzel', serif;
            letter-spacing: 2px;
            color: #1A1A1A;
        }
        .italic-subtitle {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            color: #8C7355;
        }

        /* Background e Container */
        .stApp {
            background-color: #FFFFFF;
        }

        /* Sidebar Elegante */
        [data-testid="stSidebar"] {
            background-color: #0F0F0F;
            color: #FFFFFF;
            border-right: 1px solid #2C2C2C;
        }
        [data-testid="stSidebar"] .stRadio label {
            color: #D4AF37 !important;
            font-weight: 200;
        }

        /* Botões de Luxo */
        .stButton>button {
            background-color: #1A1A1A;
            color: #D4AF37;
            border: 1px solid #D4AF37;
            border-radius: 0px;
            padding: 0.8rem 2.5rem;
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 2px;
            transition: all 0.4s ease;
        }
        .stButton>button:hover {
            background-color: #D4AF37;
            color: #1A1A1A;
            border: 1px solid #1A1A1A;
        }

        /* Cards de Artigos e Estudos */
        .article-card {
            background-color: #F9F9F9;
            padding: 30px;
            border-left: 5px solid #D4AF37;
            margin-bottom: 20px;
            transition: all 0.3s;
        }
        .article-card:hover {
            background-color: #F0F0F0;
            box-shadow: 10px 10px 20px rgba(0,0,0,0.05);
        }

        /* Banner Global */
        .global-hero {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1560066984-138dadb4c035?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            padding: 120px 40px;
            color: white;
            text-align: center;
            margin-bottom: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

local_css()

# ================= SISTEMA DE AUTENTICAÇÃO =================
# Em um sistema real, usaríamos um banco de dados. Aqui simulamos a estrutura.
CREDENCIAIS = {
    "admin": {"user": "LUCIENE", "pass": "LuBezerra520", "role": "Diretoria"},
    "staff": {"user": "EQUIPE", "pass": "Staff2026", "role": "Especialista"},
    "client": {"user": "CLIENTE", "pass": "Vip2026", "role": "Membro VIP"}
}

def check_login(u, p):
    for role, cred in CREDENCIAIS.items():
        if u == cred["user"] and p == cred["pass"]:
            return cred["role"]
    return None

# ================= CONTEÚDO CIENTÍFICO (ARTIGOS & ESTUDOS) =================
ARTIGOS_CIENTIFICOS = [
    {
        "titulo": "Avanços na Fotobioestimulação Capilar",
        "autor": "Dr. Alessandro Silva",
        "resumo": "Estudo sobre a eficácia do Laser de Baixa Intensidade (LLLT) na regeneração do folículo piloso.",
        "categoria": "Estudo Clínico"
    },
    {
        "titulo": "Microbioma do Couro Cabeludo e Alopecia",
        "autor": "Dra. Elena Rossi",
        "resumo": "Análise da disbiose capilar e sua relação direta com processos inflamatórios crônicos.",
        "categoria": "Pesquisa Científica"
    },
    {
        "titulo": "Nutracêuticos na Terapia Capilar Moderna",
        "autor": "Prof. Jean-Louis",
        "resumo": "Como a suplementação direcionada potencializa os resultados dos tratamentos tópicos.",
        "categoria": "Artigo Técnico"
    }
]

# ================= NAVEGAÇÃO PRINCIPAL =================
with st.sidebar:
    st.markdown("<h1 style='color: #D4AF37; text-align: center;'>LU BEZERRA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.7rem; letter-spacing: 3px;'>GLOBAL TRICHOLOGY</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    if "user_role" not in st.session_state:
        st.session_state.user_role = "Visitante"

    menu_options = ["The Experience", "Scientific Library", "Global Services", "Portal de Acesso"]
    
    # Adiciona opções extras baseadas no cargo
    if st.session_state.user_role == "Diretoria":
        menu_options.insert(3, "Admin Dashboard")
    elif st.session_state.user_role == "Especialista":
        menu_options.insert(3, "Staff Panel")
    elif st.session_state.user_role == "Membro VIP":
        menu_options.insert(3, "My VIP Journey")

    menu = st.radio("SELECT DESTINATION", menu_options)
    st.markdown("---")
    st.caption(f"Status: {st.session_state.user_role}")
    if st.session_state.user_role != "Visitante":
        if st.button("LOGOUT"):
            st.session_state.user_role = "Visitante"
            st.rerun()

# ================= PÁGINA: THE EXPERIENCE (HOME) =================
if menu == "The Experience":
    st.markdown("""
        <div class="global-hero">
            <h1 style="font-size: 4rem; color: #D4AF37;">The Art of Trichology</h1>
            <p class="italic-subtitle" style="font-size: 1.5rem; color: #F5F5F5;">Where Science Meets Luxury</p>
            <p style="max-width: 800px; margin: 30px auto; font-weight: 200; line-height: 1.8;">
                Welcome to the global standard of hair health. Led by Luciene Bezerra, our institute combines 
                cutting-edge clinical research with the most sophisticated spa experience in the world.
            </p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 🔬 Science")
        st.write("Evidence-based protocols developed through international clinical studies.")
    with c2:
        st.markdown("### 💎 Luxury")
        st.write("An environment designed for total sensory immersion and absolute privacy.")
    with c3:
        st.markdown("### 🌍 Global")
        st.write("Techniques and technologies sourced from the world's leading hair research centers.")

# ================= PÁGINA: SCIENTIFIC LIBRARY =================
elif menu == "Scientific Library":
    st.markdown("<h1 class='luxury-title'>Scientific Library</h1>", unsafe_allow_html=True)
    st.markdown("<p class='italic-subtitle'>Knowledge is the foundation of excellence.</p>", unsafe_allow_html=True)
    
    st.divider()
    
    search = st.text_input("Search Clinical Studies...")
    
    for art in ARTIGOS_CIENTIFICOS:
        if search.lower() in art["titulo"].lower() or search == "":
            st.markdown(f"""
                <div class="article-card">
                    <span style="color: #D4AF37; font-size: 0.7rem; font-weight: bold;">{art['categoria']}</span>
                    <h3 style="margin: 10px 0;">{art['titulo']}</h3>
                    <p style="font-size: 0.9rem; color: #666;">By {art['autor']}</p>
                    <p style="margin-top: 15px;">{art['resumo']}</p>
                    <a href="#" style="color: #1A1A1A; font-weight: bold; text-decoration: none; font-size: 0.8rem;">READ FULL STUDY →</a>
                </div>
            """, unsafe_allow_html=True)

# ================= PÁGINA: PORTAL DE ACESSO =================
elif menu == "Portal de Acesso":
    if st.session_state.user_role == "Visitante":
        st.markdown("<h1 class='luxury-title'>Private Access</h1>", unsafe_allow_html=True)
        st.write("Please identify yourself to access your personalized dashboard.")
        
        with st.container():
            col_l, col_r = st.columns([1, 1])
            with col_l:
                u = st.text_input("Username")
                p = st.text_input("Password", type="password")
                if st.button("AUTHENTICATE"):
                    role = check_login(u, p)
                    if role:
                        st.session_state.user_role = role
                        st.success(f"Welcome, {role}")
                        st.rerun()
                    else:
                        st.error("Invalid Credentials")
            with col_r:
                st.info("Access levels: Administration, Staff, and VIP Clients. If you are a new client, please contact our concierge.")
    else:
        st.success(f"You are currently logged in as: {st.session_state.user_role}")
        st.write("Use the sidebar to navigate to your exclusive panel.")

# ================= PÁGINA: ADMIN DASHBOARD =================
elif menu == "Admin Dashboard":
    st.markdown("<h1 class='luxury-title'>Executive Dashboard</h1>", unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Global Revenue", "€ 142.500", "+12%")
    m2.metric("VIP Retention", "98.4%", "+2.1%")
    m3.metric("Clinical Success", "99.9%", "Stable")
    
    st.divider()
    st.subheader("🤖 Strategic AI Assistant")
    task = st.selectbox("AI Task", ["Market Trend Analysis", "Staff Performance Review", "Global Expansion Plan"])
    if st.button("RUN ANALYSIS"):
        st.write(f"Generating {task} report for Luciene Bezerra...")
        st.progress(100)
        st.success("Analysis Complete: 'The European market shows a 15% increase in demand for organic trichology.'")

# ================= PÁGINA: STAFF PANEL =================
elif menu == "Staff Panel":
    st.markdown("<h1 class='luxury-title'>Specialist Workspace</h1>", unsafe_allow_html=True)
    st.subheader("Patient Protocols")
    patient = st.selectbox("Select Patient", ["Sophia Müller", "James Aris", "Isabella Costa"])
    st.write(f"Current Protocol for {patient}: **Intensive Follicular Regeneration**")
    if st.button("Update Clinical Notes"):
        st.toast("Notes saved to global database.")

# ================= PÁGINA: MY VIP JOURNEY =================
elif menu == "My VIP Journey":
    st.markdown("<h1 class='luxury-title'>Your VIP Journey</h1>", unsafe_allow_html=True)
    st.write("Welcome back. Your personalized treatment plan is active.")
    
    st.progress(65)
    st.caption("65% of your current protocol completed. Next session: Feb 20th.")
    
    st.divider()
    st.subheader("Concierge Chat")
    st.text_input("How can we assist you today?")
    st.button("SEND TO CONCIERGE")

# ================= PÁGINA: GLOBAL SERVICES =================
elif menu == "Global Services":
    st.markdown("<h1 class='luxury-title'>Our Expertise</h1>", unsafe_allow_html=True)
    
    services = {
        "Molecular Trichology": "Deep analysis of hair health at a cellular level.",
        "Scalp Detoxification": "Advanced purification using ozone and botanical extracts.",
        "Laser Therapy": "High-precision light therapy for hair density restoration.",
        "Luxury Hair Spa": "A sensory journey combining therapy and relaxation."
    }
    
    for s, d in services.items():
        with st.expander(s):
            st.write(d)
            st.button(f"Inquire about {s}", key=s)
