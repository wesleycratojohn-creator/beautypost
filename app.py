import streamlit as st
import random
import base64
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

# ================= SISTEMA DE AGENDA REAL (SIMULADO COM PERSISTÊNCIA EM SESSÃO) =================
if 'horarios_confirmados' not in st.session_state:
    # Simulando alguns horários já ocupados para demonstração
    hoje = datetime.now().date()
    st.session_state.horarios_confirmados = [
        {"data": hoje.strftime("%Y-%m-%d"), "hora": "09:30"},
        {"data": hoje.strftime("%Y-%m-%d"), "hora": "14:00"},
        {"data": (hoje + timedelta(days=1)).strftime("%Y-%m-%d"), "hora": "11:00"}
    ]

# ================= DESIGN E CORREÇÃO DE UI (BOTÕES E CONTRASTE) =================
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
        
        /* Fundo com Overlay para Contraste */
        .stApp {{
            background-image: url("data:image/png;base64,{bg_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stApp > div:first-child {{
            background-color: rgba(255, 255, 255, 0.96) !important;
        }}

        /* CORREÇÃO DOS BOTÕES: Garantir visibilidade e sinalização */
        .stButton > button {{
            width: 100% !important;
            background-color: #1A1A1A !important;
            color: #D4AF37 !important;
            border: 2px solid #D4AF37 !important;
            padding: 0.6rem 1rem !important;
            border-radius: 5px !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            transition: all 0.3s ease !important;
            display: block !important;
            visibility: visible !important;
            opacity: 1 !important;
        }}
        
        .stButton > button:hover {{
            background-color: #D4AF37 !important;
            color: #1A1A1A !important;
            border-color: #1A1A1A !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
        }}

        /* Sidebar Estilizada */
        [data-testid="stSidebar"] {{
            background-color: #1A1A1A !important;
            border-right: 2px solid #D4AF37 !important;
        }}
        [data-testid="stSidebar"] * {{
            color: #FFFFFF !important;
        }}
        
        /* Títulos e Cards */
        .luxury-card {{
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #D4AF37;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 15px;
        }}
        
        /* Ocultar Erros de Header do Streamlit */
        header[data-testid="stHeader"] {{
            background: transparent !important;
        }}
        header[data-testid="stHeader"] * {{
            color: transparent !important;
            font-size: 0 !important;
        }}
        header[data-testid="stHeader"] button {{
            visibility: visible !important;
            color: #D4AF37 !important;
            background: #1A1A1A !important;
            border-radius: 50% !important;
        }}
        header[data-testid="stHeader"] button svg {{
            fill: #D4AF37 !important;
            visibility: visible !important;
        }}
        </style>
    """, unsafe_allow_html=True)

load_luxury_design()

# ================= NAVEGAÇÃO =================
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37; text-align: center;'>LU BEZERRA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.8rem;'>TERAPIA CAPILAR AVANÇADA</p>", unsafe_allow_html=True)
    st.divider()
    
    menu = st.radio("MENU PRINCIPAL", 
                    ["🏠 Início", "📅 Agenda & Reservas", "🔬 Central de Estudos", "🔐 Área Administrativa"])

# ================= PÁGINA: INÍCIO =================
if menu == "🏠 Início":
    st.markdown("<h1 style='text-align: center;'>Excelência em Tricologia</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #D4AF37;'>Ciência e Cuidado para sua Saúde Capilar</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 🌟 Nossa Filosofia")
        st.write("Combinamos o rigor científico da tricologia com o acolhimento de um spa de luxo. Cada tratamento é precedido por uma análise microscópica detalhada.")
        if st.button("VER PROTOCOLOS"):
            st.info("Navegue até 'Central de Estudos' para ver nossos protocolos.")
            
    with col2:
        st.markdown("### 📸 Resultados")
        st.write("Confira as transformações reais de nossos pacientes.")
        # Espaço para imagens
        st.columns(3)[0].write("🖼️ Caso 1")
        st.columns(3)[1].write("🖼️ Caso 2")
        st.columns(3)[2].write("🖼️ Caso 3")

# ================= PÁGINA: AGENDA & RESERVAS =================
elif menu == "📅 Agenda & Reservas":
    st.title("📅 Sistema de Agendamento")
    st.write("Consulte os horários disponíveis e solicite sua reserva.")
    
    col_data, col_form = st.columns([1, 2])
    
    with col_data:
        data_selecionada = st.date_input("Selecione a Data", min_value=datetime.now().date())
        
        st.markdown("### 🕒 Horários do Dia")
        horarios_dia = ["08:00", "09:30", "11:00", "14:00", "15:30", "17:00"]
        
        for h in horarios_dia:
            ocupado = any(c['data'] == data_selecionada.strftime("%Y-%m-%d") and c['hora'] == h for c in st.session_state.horarios_confirmados)
            if ocupado:
                st.markdown(f"<span style='color: #ff4b4b;'>🔴 {h} - Ocupado</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color: #28a745;'>🟢 {h} - Disponível</span>", unsafe_allow_html=True)

    with col_form:
        st.markdown("### 📝 Solicitar Horário")
        with st.form("reserva_form"):
            nome = st.text_input("Nome Completo")
            whatsapp = st.text_input("WhatsApp (com DDD)")
            servico = st.selectbox("Serviço", ["Avaliação Tricoscópica", "Terapia Capilar Detox", "Laserterapia", "Protocolo Alopecia"])
            hora_escolhida = st.selectbox("Escolha um horário disponível", horarios_dia)
            
            enviar = st.form_submit_button("SOLICITAR AGENDAMENTO")
            
            if enviar:
                ocupado = any(c['data'] == data_selecionada.strftime("%Y-%m-%d") and c['hora'] == hora_escolhida for c in st.session_state.horarios_confirmados)
                if ocupado:
                    st.error("Este horário já foi preenchido. Por favor, escolha outro.")
                elif not nome or not whatsapp:
                    st.warning("Por favor, preencha todos os campos.")
                else:
                    msg = f"Olá Lu Bezerra! Gostaria de agendar:\n👤 Nome: {nome}\n✨ Serviço: {servico}\n📅 Data: {data_selecionada.strftime('%d/%m/%Y')}\n⏰ Hora: {hora_escolhida}"
                    url = f"https://wa.me/5574988220315?text={urllib.parse.quote(msg)}"
                    st.success("✅ Solicitação enviada! Clique no botão abaixo para confirmar.")
                    st.link_button("📱 CONFIRMAR NO WHATSAPP", url)

# ================= PÁGINA: CENTRAL DE ESTUDOS =================
elif menu == "🔬 Central de Estudos":
    st.title("🔬 Biblioteca Científica e Protocolos")
    st.write("Aprofunde seu conhecimento sobre a saúde do couro cabeludo.")
    
    tabs = st.tabs(["📚 Artigos", "🧪 Protocolos", "🧬 Estudos de Caso"])
    
    with tabs[0]:
        st.markdown("""
        <div class='luxury-card'>
            <h4>O Impacto do Estresse no Ciclo Capilar</h4>
            <p>O cortisol elevado pode antecipar a fase telógena, causando o eflúvio telógeno agudo.</p>
        </div>
        <div class='luxury-card'>
            <h4>Microbioma e Dermatite Seborreica</h4>
            <p>O desequilíbrio da Malassezia spp. é um fator chave nas inflamações do couro cabeludo.</p>
        </div>
        <div class='luxury-card'>
            <h4>Fotobiomodulação na Alopecia Androgenética</h4>
            <p>Como o laser de baixa intensidade estimula as células-tronco do folículo piloso.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with tabs[1]:
        st.markdown("""
        <div class='luxury-card'>
            <h4>Protocolo Detox Profundo</h4>
            <p>Argiloterapia associada a óleos essenciais para desobstrução folicular.</p>
        </div>
        <div class='luxury-card'>
            <h4>Protocolo de Alta Frequência</h4>
            <p>Ação bactericida e fungicida para controle de oleosidade e caspa.</p>
        </div>
        """, unsafe_allow_html=True)

# ================= PÁGINA: ÁREA ADMINISTRATIVA =================
elif menu == "🔐 Área Administrativa":
    st.title("🔐 Gestão do Instituto")
    
    if 'admin_logado' not in st.session_state:
        st.session_state.admin_logado = False
        
    if not st.session_state.admin_logado:
        u = st.text_input("Usuário")
        p = st.text_input("Senha", type="password")
        if st.button("ACESSAR PAINEL"):
            if u == "LUCIENE" and p == "LuBezerra520":
                st.session_state.admin_logado = True
                st.rerun()
            else:
                st.error("Acesso negado.")
    else:
        st.success("Bem-vinda, Luciene!")
        st.subheader("📊 Horários Confirmados")
        df = pd.DataFrame(st.session_state.horarios_confirmados)
        st.table(df)
        
        if st.button("LOGOUT"):
            st.session_state.admin_logado = False
            st.rerun()
