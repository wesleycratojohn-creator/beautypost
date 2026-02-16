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

# ================= SISTEMA DE PERSISTÊNCIA DE DADOS =================
if 'agenda_db' not in st.session_state:
    hoje = datetime.now().date()
    st.session_state.agenda_db = [
        {"data": hoje.strftime("%Y-%m-%d"), "hora": "09:30", "cliente": "Exemplo", "servico": "Avaliação"},
        {"data": hoje.strftime("%Y-%m-%d"), "hora": "14:00", "cliente": "Exemplo", "servico": "Terapia"},
    ]

# ================= DESIGN SYSTEM DE LUXO (CSS) =================
def load_luxury_styles():
    bg_img = ""
    if os.path.exists("logo.png"):
        with open("logo.png", "rb") as f:
            bg_img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

        /* Reset e Base */
        html, body, [class*="st-"] {{
            font-family: 'Montserrat', sans-serif;
            color: #1A1A1A;
        }}
        
        /* Fundo e Overlay de Alta Qualidade */
        .stApp {{
            background-image: url("data:image/png;base64,{bg_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stApp > div:first-child {{
            background-color: rgba(255, 255, 255, 0.97) !important;
        }}

        /* BOTÕES SINALIZADOS E PROFISSIONAIS */
        .stButton > button {{
            width: 100% !important;
            background-color: #1A1A1A !important;
            color: #D4AF37 !important;
            border: 2px solid #D4AF37 !important;
            padding: 0.75rem 1.5rem !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        }}
        
        .stButton > button:hover {{
            background-color: #D4AF37 !important;
            color: #1A1A1A !important;
            border-color: #1A1A1A !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 15px rgba(0,0,0,0.2) !important;
        }}

        /* Sidebar de Luxo */
        [data-testid="stSidebar"] {{
            background-color: #0F0F0F !important;
            border-right: 3px solid #D4AF37 !important;
        }}
        [data-testid="stSidebar"] * {{
            color: #F5F5F5 !important;
        }}
        [data-testid="stSidebarNav"] {{
            padding-top: 2rem !important;
        }}

        /* Títulos e Tipografia */
        h1, h2, h3 {{
            font-family: 'Playfair Display', serif !important;
            color: #000000 !important;
            font-weight: 700 !important;
        }}
        
        /* Luxury Cards */
        .luxury-card {{
            background-color: #FFFFFF;
            padding: 30px;
            border-radius: 12px;
            border-left: 6px solid #D4AF37;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            margin-bottom: 25px;
            transition: transform 0.3s ease;
        }}
        .luxury-card:hover {{
            transform: scale(1.01);
        }}
        
        /* Ocultar Elementos Técnicos do Streamlit */
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
            width: 45px !important;
            height: 45px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}
        header[data-testid="stHeader"] button svg {{
            fill: #D4AF37 !important;
            visibility: visible !important;
            width: 25px !important;
            height: 25px !important;
        }}
        
        /* Status de Agenda */
        .status-disponivel {{
            color: #2D6A4F;
            font-weight: 700;
            background: #D8F3DC;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.9rem;
        }}
        .status-ocupado {{
            color: #A4133C;
            font-weight: 700;
            background: #FFB3C1;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.9rem;
        }}
        </style>
    """, unsafe_allow_html=True)

load_luxury_styles()

# ================= NAVEGAÇÃO ESTRUTURADA =================
with st.sidebar:
    st.markdown("<h1 style='color: #D4AF37; text-align: center; font-size: 1.8rem;'>LU BEZERRA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; letter-spacing: 3px; font-size: 0.7rem; color: #888;'>INSTITUTO DE TRICOLOGIA</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    menu = st.radio("SELECIONE O PORTAL", 
                    ["🏠 Home Experience", "📅 Agenda de Luxo", "🔬 Central Científica", "🔐 Gestão Exclusiva"])
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.7rem; color: #555;'>© 2026 Lu Bezerra Terapia Capilar<br>Todos os direitos reservados.</p>", unsafe_allow_html=True)

# ================= PÁGINA: HOME EXPERIENCE =================
if menu == "🏠 Home Experience":
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>A Ciência do Cuidado</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #D4AF37; font-size: 1.2rem; font-style: italic;'>Onde a saúde do couro cabeludo encontra a sofisticação.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 💎 Excelência em Cada Detalhe")
        st.write("""
            No Instituto Lu Bezerra, não apenas tratamos sintomas; investigamos causas. 
            Nossa abordagem une tecnologia de ponta e protocolos personalizados para 
            garantir que sua jornada capilar seja transformadora e definitiva.
        """)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("EXPLORAR PROTOCOLOS"):
            st.toast("Navegando para a Central Científica...")
            
    with col2:
        st.markdown("### ✨ Resultados de Autoridade")
        st.write("Transformações que devolvem a autoestima e a saúde.")
        res_cols = st.columns(3)
        for i in range(3):
            res_cols[i].markdown(f"<div style='background: #F0F0F0; height: 150px; border-radius: 8px; display: flex; align-items: center; justify-content: center; border: 1px solid #DDD;'>📸 Caso {i+1}</div>", unsafe_allow_html=True)

# ================= PÁGINA: AGENDA DE LUXO =================
elif menu == "📅 Agenda de Luxo":
    st.markdown("<h1>📅 Gestão de Agendamentos</h1>", unsafe_allow_html=True)
    st.write("Consulte horários reais e solicite sua reserva exclusiva.")
    
    col_calendar, col_booking = st.columns([1, 1.5], gap="large")
    
    with col_calendar:
        st.markdown("### 1. Escolha a Data")
        data_sel = st.date_input("Data da Consulta", min_value=datetime.now().date())
        
        st.markdown("### 🕒 Disponibilidade do Dia")
        horarios = ["08:00", "09:30", "11:00", "14:00", "15:30", "17:00"]
        
        for h in horarios:
            is_ocupado = any(c['data'] == data_sel.strftime("%Y-%m-%d") and c['hora'] == h for c in st.session_state.agenda_db)
            if is_ocupado:
                st.markdown(f"<div style='margin-bottom: 10px;'><span class='status-ocupado'>RESERVADO</span> <span style='margin-left: 10px;'>{h}</span></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='margin-bottom: 10px;'><span class='status-disponivel'>DISPONÍVEL</span> <span style='margin-left: 10px;'>{h}</span></div>", unsafe_allow_html=True)

    with col_booking:
        st.markdown("### 2. Solicite sua Reserva")
        with st.form("luxury_booking_form"):
            nome = st.text_input("Nome Completo")
            contato = st.text_input("WhatsApp para Confirmação")
            servico = st.selectbox("Protocolo Desejado", ["Avaliação Tricoscópica", "Terapia Capilar Detox", "Laserterapia Sistêmica", "Protocolo de Crescimento"])
            hora_sel = st.selectbox("Horário Desejado", horarios)
            
            submit = st.form_submit_button("SOLICITAR AGENDAMENTO VIP")
            
            if submit:
                if not nome or not contato:
                    st.error("Por favor, preencha todos os campos para prosseguir.")
                else:
                    is_ocupado = any(c['data'] == data_sel.strftime("%Y-%m-%d") and c['hora'] == hora_sel for c in st.session_state.agenda_db)
                    if is_ocupado:
                        st.error("Este horário acabou de ser reservado. Por favor, escolha outro.")
                    else:
                        msg = f"Olá Lu Bezerra! Gostaria de solicitar um agendamento VIP:\n\n👤 Nome: {nome}\n✨ Protocolo: {servico}\n📅 Data: {data_sel.strftime('%d/%m/%Y')}\n⏰ Hora: {hora_sel}"
                        wa_url = f"https://wa.me/5574988220315?text={urllib.parse.quote(msg)}"
                        st.success("✅ Solicitação enviada com sucesso!")
                        st.link_button("📱 CONFIRMAR VIA WHATSAPP", wa_url)

# ================= PÁGINA: CENTRAL CIENTÍFICA =================
elif menu == "🔬 Central Científica":
    st.markdown("<h1>🔬 Biblioteca de Tricologia Avançada</h1>", unsafe_allow_html=True)
    st.write("Conhecimento científico para fundamentar seu tratamento.")
    
    tab1, tab2, tab3 = st.tabs(["📚 Artigos Técnicos", "🧪 Protocolos Clínicos", "🧬 Estudos de Caso"])
    
    with tab1:
        st.markdown("""
            <div class='luxury-card'>
                <h3>O Microbioma do Couro Cabeludo</h3>
                <p>Estudos recentes comprovam que o desequilíbrio da flora bacteriana é o principal gatilho para inflamações e queda capilar crônica.</p>
            </div>
            <div class='luxury-card'>
                <h3>Fotobiomodulação e ATP Celular</h3>
                <p>Como a luz de baixa intensidade (LLLT) atua nas mitocôndrias do folículo piloso para acelerar a fase anágena.</p>
            </div>
            <div class='luxury-card'>
                <h3>Eflúvio Telógeno Pós-Inflamatório</h3>
                <p>Análise das causas sistêmicas que levam à queda aguda e como reverter o quadro através da nutrição e terapia tópica.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
            <div class='luxury-card'>
                <h3>Protocolo Detox Lu Bezerra</h3>
                <p>Desobstrução folicular profunda utilizando argilas raras e óleos essenciais quimiotipados.</p>
            </div>
            <div class='luxury-card'>
                <h3>Protocolo de Alta Frequência</h3>
                <p>Uso de ozônio para ação bactericida e estimulação da microcirculação periférica.</p>
            </div>
        """, unsafe_allow_html=True)

# ================= PÁGINA: GESTÃO EXCLUSIVA =================
elif menu == "🔐 Gestão Exclusiva":
    st.markdown("<h1>🔐 Portal Administrativo</h1>", unsafe_allow_html=True)
    
    if 'auth_admin' not in st.session_state:
        st.session_state.auth_admin = False
        
    if not st.session_state.auth_admin:
        with st.container():
            st.markdown("<div class='luxury-card'>", unsafe_allow_html=True)
            user = st.text_input("Identificação")
            password = st.text_input("Chave de Acesso", type="password")
            if st.button("ACESSAR SISTEMA"):
                if user == "LUCIENE" and password == "LuBezerra520":
                    st.session_state.auth_admin = True
                    st.rerun()
                else:
                    st.error("Credenciais inválidas. Tente novamente.")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.success("Bem-vinda, Luciene. Sistema operando com segurança.")
        
        st.subheader("📊 Visão Geral da Agenda")
        if st.session_state.agenda_db:
            df = pd.DataFrame(st.session_state.agenda_db)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhum agendamento registrado para o período.")
            
        if st.button("ENCERRAR SESSÃO"):
            st.session_state.auth_admin = False
            st.rerun()
