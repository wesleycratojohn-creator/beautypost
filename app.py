import streamlit as st
import random
import base64
from PIL import Image
import os
import pandas as pd
from datetime import datetime

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(
    page_title="Lu Bezerra | Terapia Capilar Especializada",
    page_icon="💆‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= IDENTIDADE VISUAL ORIGINAL (CSS) =================
def load_css():
    # Carrega a logo para o fundo se existir
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
        }}
        
        /* Fundo Original com Logo */
        .stApp {{
            background-image: url("data:image/png;base64,{bg_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Overlay para legibilidade */
        .stApp > div:first-child {{
            background-color: rgba(255, 255, 255, 0.85);
        }}

        /* Sidebar Customizada */
        [data-testid="stSidebar"] {{
            background-color: rgba(255, 255, 255, 0.9);
            border-right: 1px solid #E0E0E0;
        }}

        /* Títulos e Textos */
        h1, h2, h3 {{
            font-family: 'Playfair Display', serif;
            color: #333333;
        }}

        /* Botões Profissionais */
        .stButton>button {{
            width: 100%;
            border-radius: 5px;
            border: 1px solid #333;
            background-color: #333;
            color: white;
            padding: 10px;
            font-weight: 600;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #555;
            border-color: #555;
            color: #fff;
        }}

        /* Cards de Conteúdo */
        .luxury-card {{
            background-color: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            border: 1px solid #F0F0F0;
        }}
        </style>
    """, unsafe_allow_html=True)

load_css()

# ================= SISTEMA DE LOGIN E PERMISSÕES =================
CREDENCIAIS = {
    "admin": {"usuario": "LUCIENE", "senha": "LuBezerra520", "cargo": "Administração"},
    "equipe": {"usuario": "EQUIPE", "senha": "Staff2026", "cargo": "Funcionário"},
    "cliente": {"usuario": "CLIENTE", "senha": "Vip2026", "cargo": "Cliente VIP"}
}

if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.cargo = "Visitante"

def realizar_login(u, s):
    for role, cred in CREDENCIAIS.items():
        if u == cred["usuario"] and s == cred["senha"]:
            st.session_state.logado = True
            st.session_state.cargo = cred["cargo"]
            return True
    return False

# ================= CONTEÚDO TÉCNICO E CIENTÍFICO =================
ARTIGOS = [
    {
        "titulo": "A Ciência da Terapia Capilar",
        "conteudo": "A terapia capilar vai além da estética, focando na saúde do couro cabeludo e na fisiologia do fio.",
        "tipo": "Artigo Científico"
    },
    {
        "titulo": "Estudo sobre Alopecia Androgenética",
        "conteudo": "Novas pesquisas indicam que o diagnóstico precoce aumenta em 80% as chances de recuperação capilar.",
        "tipo": "Estudo Clínico"
    }
]

# ================= NAVEGAÇÃO =================
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.title("Lu Bezerra")
    
    st.markdown("---")
    
    opcoes = ["Início", "Serviços", "Biblioteca Científica", "Agendamento", "Área Restrita"]
    
    # Opções dinâmicas baseadas no login
    if st.session_state.cargo == "Administração":
        opcoes.insert(4, "Painel Administrativo")
    elif st.session_state.cargo == "Funcionário":
        opcoes.insert(4, "Painel da Equipe")
    elif st.session_state.cargo == "Cliente VIP":
        opcoes.insert(4, "Espaço VIP")

    menu = st.radio("Navegação Principal", opcoes)
    
    st.markdown("---")
    if st.session_state.logado:
        st.write(f"Conectado como: **{st.session_state.cargo}**")
        if st.button("Sair do Sistema"):
            st.session_state.logado = False
            st.session_state.cargo = "Visitante"
            st.rerun()
    else:
        st.info("Acesse a Área Restrita para recursos exclusivos.")

# ================= PÁGINA: INÍCIO =================
if menu == "Início":
    st.markdown("<h1 style='text-align: center;'>Lu Bezerra | Terapia Capilar</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic;'>Excelência Global em Saúde e Estética Capilar</p>", unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("✨ Nossa Missão")
        st.write("""
            Proporcionar saúde e autoestima através de protocolos científicos personalizados. 
            Utilizamos o que há de mais moderno na tricologia mundial para cuidar de você.
        """)
        st.link_button("Falar com Especialista", "https://wa.me/5574988220315")
    
    with col2:
        st.subheader("⭐ Resultados")
        # Mostra imagens de resultados se existirem
        cols_res = st.columns(3)
        for i in range(1, 4):
            img_p = f"{i}.jpeg"
            if os.path.exists(img_p):
                cols_res[i-1].image(img_p, use_container_width=True)

# ================= PÁGINA: SERVIÇOS =================
elif menu == "Serviços":
    st.title("💎 Nossos Protocolos")
    
    servicos = {
        "Terapia Capilar Avançada": "Diagnóstico via microcâmera e tratamento de patologias do couro cabeludo.",
        "Laserterapia de Baixa Intensidade": "Estímulo celular para crescimento e fortalecimento dos fios.",
        "Detox Bulbar": "Limpeza profunda e desobstrução dos folículos pilosos.",
        "Cronograma Capilar de Luxo": "Nutrição e reconstrução com ativos de alta performance."
    }
    
    for s, d in servicos.items():
        with st.container():
            st.markdown(f"""
                <div class="luxury-card">
                    <h3>{s}</h3>
                    <p>{d}</p>
                </div>
            """, unsafe_allow_html=True)

# ================= PÁGINA: BIBLIOTECA CIENTÍFICA =================
elif menu == "Biblioteca Científica":
    st.title("📚 Conhecimento e Ciência")
    st.write("Explore artigos e estudos que fundamentam nossos tratamentos.")
    
    for art in ARTIGOS:
        with st.expander(f"{art['tipo']}: {art['titulo']}"):
            st.write(art['conteudo'])
            st.caption("Fonte: Instituto de Tricologia Lu Bezerra")

# ================= PÁGINA: AGENDAMENTO =================
elif menu == "Agendamento":
    st.title("📅 Reserve seu Momento")
    st.write("Escolha o canal de sua preferência para agendar sua avaliação.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("📱 WhatsApp")
        st.link_button("Agendar via WhatsApp", "https://wa.me/5574988220315")
    with c2:
        st.info("📸 Instagram")
        st.link_button("Seguir no Instagram", "https://www.instagram.com/lubezerra_terapiacapilar")

# ================= PÁGINA: ÁREA RESTRITA (LOGIN) =================
elif menu == "Área Restrita":
    if not st.session_state.logado:
        st.title("🔐 Acesso Restrito")
        st.write("Identifique-se para acessar as ferramentas de gestão e benefícios VIP.")
        
        with st.form("login_form"):
            u = st.text_input("Usuário")
            s = st.text_input("Senha", type="password")
            if st.form_submit_button("Entrar no Sistema"):
                if realizar_login(u, s):
                    st.success(f"Bem-vindo(a), {st.session_state.cargo}!")
                    st.rerun()
                else:
                    st.error("Credenciais incorretas. Por favor, tente novamente.")
    else:
        st.success(f"Você já está conectado como {st.session_state.cargo}.")
        st.write("Utilize o menu lateral para acessar seu painel exclusivo.")

# ================= PAINÉIS ESPECÍFICOS =================
elif menu == "Painel Administrativo":
    st.title("🛠 Gestão Estratégica")
    st.subheader("Visão Geral do Negócio")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Novos Clientes (Mês)", "42", "+15%")
    m2.metric("Taxa de Retenção", "94%", "+2%")
    m3.metric("Satisfação (NPS)", "9.8", "Estável")
    
    st.divider()
    st.subheader("🤖 Assistente de IA para Marketing")
    if st.button("Gerar Legenda para Instagram"):
        frases = [
            "A saúde do seu cabelo começa na raiz. Agende sua avaliação! ✨",
            "Terapia capilar: ciência a favor da sua autoestima. 💆‍♀️",
            "Resultados reais exigem protocolos profissionais. 💎"
        ]
        st.code(random.choice(frases))

elif menu == "Painel da Equipe":
    st.title("📋 Operação e Protocolos")
    st.write("Acesse as fichas técnicas e orientações para os atendimentos do dia.")
    
    paciente = st.selectbox("Paciente do Horário", ["Ana Silva", "Carlos Oliveira", "Mariana Santos"])
    st.info(f"Protocolo sugerido para {paciente}: **Laserterapia + Detox**")
    
    if st.button("Confirmar Realização"):
        st.success("Atendimento registrado com sucesso.")

elif menu == "Espaço VIP":
    st.title("🌟 Seu Espaço VIP")
    st.write("Bem-vindo(a) ao seu portal de benefícios exclusivos.")
    
    st.progress(70)
    st.caption("Você completou 70% do seu protocolo atual. Faltam apenas 3 sessões!")
    
    st.divider()
    st.subheader("🎁 Benefícios Ativos")
    st.write("- 10% de desconto em produtos home care.")
    st.write("- Prioridade em agendamentos de feriados.")
