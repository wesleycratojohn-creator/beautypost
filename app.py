import streamlit as st
import random
import base64
import os
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
from PIL import Image

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(
    page_title="Lu Bezerra | Terapia Capilar",
    page_icon="💆‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= SISTEMA DE AGENDA REAL (PERSISTÊNCIA EM SESSÃO) =================
if 'agenda_confirmada' not in st.session_state:
    hoje = datetime.now().date()
    st.session_state.agenda_confirmada = [
        {"data": hoje.strftime("%Y-%m-%d"), "hora": "09:30"},
        {"data": hoje.strftime("%Y-%m-%d"), "hora": "14:00"},
    ]

# ================= DESIGN E CORREÇÃO DE UI (BOTÕES E CONTRASTE) =================
def carregar_estilo_corrigido(img_path):
    encoded = ""
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
    
    st.markdown(
        f"""
        <style>
        /* Preservar Fundo Original */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        /* Overlay Suave para Legibilidade */
        .stApp > div:first-child {{
            background-color: rgba(255, 255, 255, 0.94) !important;
        }}

        /* CORREÇÃO DOS BOTÕES: Fundo Claro, Letras Pretas (Alto Contraste) */
        .stButton > button {{
            width: 100% !important;
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 2px solid #000000 !important;
            padding: 0.75rem 1.5rem !important;
            border-radius: 8px !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        }}
        
        .stButton > button:hover {{
            background-color: #000000 !important;
            color: #FFFFFF !important;
            border-color: #000000 !important;
        }}

        /* Inputs e Selects com Alto Contraste */
        input, select, .stSelectbox div {{
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
        }}

        /* Sidebar Estilizada */
        [data-testid="stSidebar"] {{
            background-color: #000000 !important;
            border-right: 2px solid #D4AF37 !important;
        }}
        [data-testid="stSidebar"] * {{
            color: #FFFFFF !important;
        }}

        /* Status da Agenda */
        .status-livre {{ color: #28a745; font-weight: bold; }}
        .status-ocupado {{ color: #dc3545; font-weight: bold; }}
        
        /* Limpeza de Header */
        header[data-testid="stHeader"] {{ background: transparent !important; }}
        header[data-testid="stHeader"] * {{ color: transparent !important; font-size: 0 !important; }}
        </style>
        """,
        unsafe_allow_html=True
    )

carregar_estilo_corrigido("logo.png")

# ================= DADOS ORIGINAIS =================
USUARIO_ADMIN = "LUCIENE"
SENHA_ADMIN = "LuBezerra520"

BASE_TECNICA = [
    "A terapia capilar trata disfunções do couro cabeludo através da análise tricossistêmica, promovendo equilíbrio fisiológico.",
    "Processos inflamatórios silenciosos são causas frequentes de queda capilar e afinamento dos fios.",
    "A saúde do couro cabeludo é determinante para o crescimento capilar saudável."
]

CONDUTA = [
    "O protocolo envolve controle inflamatório, estímulo da microcirculação e regeneração folicular.",
    "Utilizam-se ativos terapêuticos, técnicas manuais e acompanhamento contínuo.",
    "Cada tratamento é individualizado após avaliação profissional."
]

FECHAMENTO = [
    "A avaliação presencial é essencial para diagnóstico preciso.",
    "Protocolos personalizados garantem resultados reais.",
    "O acompanhamento profissional faz toda a diferença."
]

LEGENDAS_INSTAGRAM = [
    "Cabelo saudável começa no couro cabeludo. ✨",
    "Terapia capilar é ciência, cuidado e resultado. 💆‍♀️",
    "Cada fio conta uma história. Vamos cuidar da sua. 🤍",
    "Tratamento capilar profissional é investimento em autoestima."
]

def gerar_resposta(problema):
    return f"""
### 🧠 Análise Profissional
{random.choice(BASE_TECNICA)}

### 🔍 Queixa Relatada
**{problema}**

### 🧪 Conduta Terapêutica
{random.choice(CONDUTA)}

### ✅ Orientação Final
{random.choice(FECHAMENTO)}
"""

# ================= NAVEGAÇÃO =================
st.sidebar.markdown("<h2 style='color: #FFFFFF; text-align: center;'>Lu Bezerra</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #D4AF37; text-align: center; font-size: 0.8rem;'>TERAPIA CAPILAR</p>", unsafe_allow_html=True)
st.sidebar.divider()
pagina = st.sidebar.radio("Navegação", ["Cliente", "Agenda do Salão", "Área de Estudo", "Área Profissional"])

# ================= PÁGINA: CLIENTE =================
if pagina == "Cliente":
    st.markdown("<h1 style='text-align: center;'>Lu Bezerra Terapia Capilar</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Cuidado avançado para couro cabeludo e fios.</p>", unsafe_allow_html=True)

    st.divider()

    st.subheader("⭐ O que nossos clientes dizem")
    
    # Restaurando todas as fotos de feedback
    imagens = ["1.jpeg", "2.jpeg", "3.jpeg", "4.jpeg", "5.jpeg"]
    
    # Criar colunas para as imagens existentes
    imgs_existentes = [img for img in imagens if os.path.exists(img)]
    if imgs_existentes:
        cols = st.columns(len(imgs_existentes))
        for col, img in zip(cols, imgs_existentes):
            col.image(Image.open(img), use_container_width=True)

    st.divider()

    st.subheader("📞 Contato")
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🟢 WhatsApp", "https://wa.me/5574988220315")
    with c2:
        st.link_button("📸 Instagram", "https://www.instagram.com/lubezerra_terapiacapilar")

# ================= PÁGINA: AGENDA DO SALÃO =================
elif pagina == "Agenda do Salão":
    st.markdown("<h1>📅 Agenda Lu Bezerra Terapia Capilar</h1>", unsafe_allow_html=True)
    st.write("Consulte os horários e solicite seu agendamento.")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        data_sel = st.date_input("Selecione a Data", min_value=datetime.now().date())
        st.markdown("### 🕒 Horários")
        horarios_padrao = ["08:00", "09:30", "11:00", "14:00", "15:30", "17:00"]
        
        for h in horarios_padrao:
            ocupado = any(c['data'] == data_sel.strftime("%Y-%m-%d") and c['hora'] == h for c in st.session_state.agenda_confirmada)
            if ocupado:
                st.markdown(f"<span class='status-ocupado'>🔴 {h} - Reservado</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span class='status-livre'>🟢 {h} - Disponível</span>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 📝 Solicitar Horário")
        with st.form("form_agenda"):
            nome = st.text_input("Seu Nome")
            servico = st.selectbox("Serviço", ["Avaliação", "Terapia Capilar", "Laserterapia", "Protocolo Detox"])
            hora_sel = st.selectbox("Escolha o Horário", horarios_padrao)
            
            if st.form_submit_button("SOLICITAR VIA WHATSAPP"):
                if not nome:
                    st.error("Por favor, informe seu nome.")
                else:
                    msg = f"Olá Lu Bezerra! Gostaria de agendar:\n👤 Nome: {nome}\n✨ Serviço: {servico}\n📅 Data: {data_sel.strftime('%d/%m/%Y')}\n⏰ Hora: {hora_sel}"
                    url = f"https://wa.me/5574988220315?text={urllib.parse.quote(msg)}"
                    st.success("Solicitação pronta! Clique abaixo.")
                    st.link_button("📱 ENVIAR NO WHATSAPP", url)

# ================= PÁGINA: ÁREA DE ESTUDO =================
elif pagina == "Área de Estudo":
    st.markdown("<h1>🔬 Central de Estudos e Conhecimento</h1>", unsafe_allow_html=True)
    st.write("Conteúdo técnico sobre saúde capilar.")
    
    st.markdown("""
    ### 📚 Tópicos Avançados
    - **Microbioma Capilar**: O equilíbrio das bactérias no couro cabeludo.
    - **Fotobiomodulação**: O uso de luz para estimular o crescimento.
    - **Tricoscopia**: A importância do diagnóstico por imagem.
    - **Dermatite Seborreica**: Causas e protocolos de controle.
    - **Eflúvio Telógeno**: Entendendo a queda capilar aguda.
    """)
    
    st.info("Esta área é dedicada ao aprimoramento técnico e educação dos clientes.")

# ================= PÁGINA: ÁREA PROFISSIONAL =================
elif pagina == "Área Profissional":
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if not st.session_state.logado:
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if usuario == USUARIO_ADMIN and senha == SENHA_ADMIN:
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos")
    else:
        st.subheader("🧑‍⚕️ Resposta Técnica Profissional")
        problema = st.text_input("Informe a queixa capilar do cliente")
        if st.button("Gerar resposta técnica"):
            if problema:
                st.markdown(gerar_resposta(problema))

        st.divider()
        
        st.subheader("📊 Gestão de Agenda")
        st.write("Horários confirmados no sistema:")
        st.table(pd.DataFrame(st.session_state.agenda_confirmada))

        st.divider()
        
        if st.button("🚪 Logout"):
            st.session_state.logado = False
            st.rerun()
