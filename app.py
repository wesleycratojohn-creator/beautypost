import streamlit as st
import random
import base64
from PIL import Image
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(
    page_title="Lu Bezerra | Instituto de Terapia Capilar",
    page_icon="💆‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= DESIGN DE ALTO PADRÃO E SINALIZAÇÃO (CSS) =================
def load_luxury_design():
    bg_img = ""
    if os.path.exists("logo.png"):
        with open("logo.png", "rb") as f:
            bg_img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

        /* Reset e Fontes */
        html, body, [class*="st-"] {{
            font-family: 'Montserrat', sans-serif;
            color: #1A1A1A;
        }}
        
        /* Fundo com Logo e Overlay */
        .stApp {{
            background-image: url("data:image/png;base64,{bg_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stApp > div:first-child {{
            background-color: rgba(255, 255, 255, 0.94);
        }}

        /* Sidebar Boutique */
        [data-testid="stSidebar"] {{
            background-color: #1A1A1A !important;
            border-right: 3px solid #D4AF37;
        }}
        [data-testid="stSidebar"] .stRadio label {{
            color: #FFFFFF !important;
            font-weight: 500 !important;
            font-size: 1rem !important;
            padding: 12px 0 !important;
        }}

        /* BOTÕES SINALIZADOS E VISÍVEIS */
        .stButton>button {{
            width: 100%;
            border-radius: 4px;
            border: 2px solid #D4AF37 !important; /* Borda dourada para sinalização */
            background-color: #1A1A1A !important; /* Fundo escuro */
            color: #D4AF37 !important; /* Texto dourado */
            padding: 14px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }}
        .stButton>button:hover {{
            background-color: #D4AF37 !important;
            color: #1A1A1A !important;
            transform: scale(1.02);
        }}

        /* Títulos */
        h1, h2, h3 {{
            font-family: 'Playfair Display', serif;
            color: #000000;
        }}

        /* Cards de Luxo */
        .luxury-card {{
            background-color: #FFFFFF;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.06);
            margin-bottom: 20px;
            border-left: 5px solid #D4AF37;
        }}

        /* Header Cleanup */
        header[data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0) !important;
        }}
        header[data-testid="stHeader"] * {{
            color: transparent !important;
            font-size: 0 !important;
        }}
        header[data-testid="stHeader"] button {{
            visibility: visible !important;
            color: #D4AF37 !important;
            background-color: #1A1A1A !important;
            border-radius: 50% !important;
            width: 45px !important;
            height: 45px !important;
        }}
        header[data-testid="stHeader"] button svg {{
            fill: #D4AF37 !important;
            visibility: visible !important;
        }}
        </style>
    """, unsafe_allow_html=True)

load_luxury_design()

# ================= DADOS E FERRAMENTAS =================
CREDENCIAIS = {
    "admin": {"usuario": "LUCIENE", "senha": "LuBezerra520", "cargo": "Diretoria"},
    "equipe": {"usuario": "EQUIPE", "senha": "Staff2026", "cargo": "Especialista"},
    "cliente": {"usuario": "CLIENTE", "senha": "Vip2026", "cargo": "Membro VIP"}
}

TOPICOS_TERAPIA = [
    {"titulo": "Microbioma do Couro Cabeludo", "desc": "O equilíbrio das bactérias e fungos é vital para evitar inflamações e queda."},
    {"titulo": "Fotobiomodulação (Laser)", "desc": "Uso de luz vermelha para aumentar o ATP celular e acelerar o crescimento."},
    {"titulo": "Argiloterapia Clínica", "desc": "Desintoxicação profunda com minerais que equilibram a oleosidade e pH."},
    {"titulo": "Eflúvio Telógeno", "desc": "Entenda como o estresse e deficiências nutricionais causam queda aguda."},
    {"titulo": "Alopecia Areata", "desc": "Abordagem terapêutica para falhas circulares de origem autoimune."},
    {"titulo": "Cronograma Capilar Científico", "desc": "Reposição de massa e lipídios baseada na porosidade real do fio."}
]

# ================= FUNÇÕES DE APOIO =================
def gerar_link_whatsapp(nome, servico, data, hora):
    texto = f"Olá Lu Bezerra! Gostaria de confirmar meu agendamento.\n\n👤 *Nome:* {nome}\n✨ *Serviço:* {servico}\n📅 *Data:* {data}\n⏰ *Hora:* {hora}\n\nAguardo confirmação! ✨"
    texto_url = urllib.parse.quote(texto)
    return f"https://wa.me/5574988220315?text={texto_url}"

# ================= NAVEGAÇÃO =================
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    
    st.markdown("<p style='color: #D4AF37; text-align: center; font-weight: 700; letter-spacing: 2px;'>INSTITUTO LU BEZERRA</p>", unsafe_allow_html=True)
    
    opcoes = ["🏠 Início", "📅 Agendamento Real", "💎 Protocolos & Ciência", "📚 Biblioteca Técnica", "🔐 Área Restrita"]
    
    if "logado" not in st.session_state:
        st.session_state.logado = False
        st.session_state.cargo = "Visitante"

    if st.session_state.cargo == "Diretoria":
        opcoes.insert(4, "📊 Gestão Estratégica")
    elif st.session_state.cargo == "Especialista":
        opcoes.insert(4, "📋 Prontuários")

    menu = st.radio("NAVEGAÇÃO", opcoes)
    
    st.markdown("---")
    if st.session_state.logado:
        st.write(f"Acesso: **{st.session_state.cargo}**")
        if st.button("SAIR DO SISTEMA"):
            st.session_state.logado = False
            st.session_state.cargo = "Visitante"
            st.rerun()

# ================= PÁGINA: INÍCIO =================
if menu == "🏠 Início":
    st.markdown("<h1 style='text-align: center;'>Lu Bezerra | Terapia Capilar</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: 600;'>CIÊNCIA, SAÚDE E AUTOESTIMA</p>", unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 🔬 O Diferencial Lu Bezerra")
        st.write("""
            Não tratamos apenas o fio, tratamos a causa. Através da tricologia avançada, 
            identificamos disfunções sistêmicas que afetam sua saúde capilar. 
            Nossa missão é devolver a você a confiança de um cabelo saudável e vibrante.
        """)
        st.link_button("CONHEÇA NOSSOS CASOS", "https://www.instagram.com/lubezerra_terapiacapilar")
    
    with col2:
        st.markdown("### ⭐ Resultados Reais")
        cols_res = st.columns(3)
        for i in range(1, 4):
            img_p = f"{i}.jpeg"
            if os.path.exists(img_p):
                cols_res[i-1].image(img_p, use_container_width=True)

# ================= PÁGINA: AGENDAMENTO REAL =================
elif menu == "📅 Agendamento Real":
    st.title("📅 Agendamento de Consultas")
    st.write("Preencha os dados abaixo para reservar seu horário exclusivo.")
    
    with st.form("form_agenda"):
        col_a, col_b = st.columns(2)
        nome = col_a.text_input("Seu Nome Completo")
        servico = col_b.selectbox("Serviço Desejado", ["Avaliação Tricoscópica", "Terapia Capilar", "Laserterapia", "Detox Capilar", "Mechas & Saúde"])
        
        data = col_a.date_input("Data Preferencial", min_value=datetime.now())
        hora = col_b.selectbox("Horário", ["08:00", "09:30", "11:00", "14:00", "15:30", "17:00"])
        
        submit = st.form_submit_button("SOLICITAR AGENDAMENTO")
        
        if submit:
            if nome:
                link = gerar_link_whatsapp(nome, servico, data.strftime('%d/%m/%Y'), hora)
                st.success("✅ Solicitação preparada! Clique no botão abaixo para confirmar no WhatsApp.")
                st.link_button("🚀 CONFIRMAR NO WHATSAPP", link)
            else:
                st.error("Por favor, informe seu nome.")

# ================= PÁGINA: PROTOCOLOS & CIÊNCIA =================
elif menu == "💎 Protocolos & Ciência":
    st.title("💎 Nossos Protocolos")
    
    for topico in TOPICOS_TERAPIA:
        with st.container():
            st.markdown(f"""
                <div class="luxury-card">
                    <h3 style="color: #D4AF37; margin-top: 0;">{topico['titulo']}</h3>
                    <p>{topico['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

# ================= PÁGINA: BIBLIOTECA TÉCNICA =================
elif menu == "📚 Biblioteca Técnica":
    st.title("📚 Biblioteca Científica")
    st.write("Conteúdo técnico para pacientes e profissionais.")
    
    with st.expander("📖 O Ciclo de Vida do Cabelo"):
        st.write("Entenda as fases Anágena (crescimento), Catágena (transição) e Telógena (queda).")
    
    with st.expander("📖 Nutrição e Cabelo"):
        st.write("A importância do Ferro, Zinco e Vitaminas do complexo B na síntese da queratina.")

# ================= PÁGINA: ÁREA RESTRITA =================
elif menu == "🔐 Área Restrita":
    if not st.session_state.logado:
        st.title("🔐 Acesso Restrito")
        u = st.text_input("Usuário")
        s = st.text_input("Senha", type="password")
        if st.button("ENTRAR NO SISTEMA"):
            for role, cred in CREDENCIAIS.items():
                if u == cred["usuario"] and s == cred["senha"]:
                    st.session_state.logado = True
                    st.session_state.cargo = cred["cargo"]
                    st.rerun()
            st.error("Credenciais incorretas.")
    else:
        st.success(f"Conectado como {st.session_state.cargo}")

# ================= PAINÉIS EXCLUSIVOS =================
elif menu == "📊 Gestão Estratégica":
    st.title("📊 Painel de Gestão")
    st.subheader("Métricas do Salão")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Agendamentos/Semana", "28", "+4")
    c2.metric("Ticket Médio", "R$ 350", "+R$ 25")
    c3.metric("Taxa de Conversão", "85%", "+5%")
    
    st.divider()
    st.subheader("🤖 Assistente de IA para Conteúdo")
    if st.button("GERAR LEGENDA PARA INSTAGRAM"):
        legendas = [
            "Cabelo saudável não é sorte, é tratamento. ✨ #TerapiaCapilar",
            "Sua autoestima merece o cuidado da ciência. 💆‍♀️ #LuBezerra",
            "Raiz saudável, fios radiantes. Agende sua avaliação! 💎"
        ]
        st.info(random.choice(legendas))

elif menu == "📋 Prontuários":
    st.title("📋 Prontuários Digitais")
    paciente = st.selectbox("Paciente", ["Ana Silva", "Carlos Oliveira", "Mariana Santos"])
    st.markdown(f"<div class='luxury-card'><h3>Ficha Técnica: {paciente}</h3><p>Histórico: 3 sessões de Laserterapia concluídas.</p></div>", unsafe_allow_html=True)
    st.button("ADICIONAR NOTA TÉCNICA")
