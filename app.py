import streamlit as st
import random
import base64
from PIL import Image
import os

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(
    page_title="Lu Bezerra | Terapia Capilar & Salão de Luxo",
    page_icon="💆‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ESTILIZAÇÃO CSS PROFISSIONAL =================
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400;700&display=swap');

        /* Reset e Fontes */
        html, body, [class*="st-"] {
            font-family: 'Lato', sans-serif;
        }
        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            color: #4A3728;
        }

        /* Background e Container */
        .stApp {
            background-color: #FDFBF9;
        }

        /* Sidebar Customizada */
        [data-testid="stSidebar"] {
            background-color: #F5E6D3;
            border-right: 1px solid #E0C9A6;
        }
        
        /* Botões Estilizados */
        .stButton>button {
            background-color: #8C6A5E;
            color: white;
            border-radius: 20px;
            border: none;
            padding: 0.5rem 2rem;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #4A3728;
            color: #F5E6D3;
            transform: translateY(-2px);
        }

        /* Cards de Serviço */
        .service-card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border: 1px solid #F5E6D3;
            text-align: center;
            height: 100%;
            transition: transform 0.3s;
        }
        .service-card:hover {
            transform: scale(1.02);
        }

        /* Banner Principal */
        .hero-section {
            background-color: rgba(245, 230, 211, 0.3);
            padding: 60px 20px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 40px;
            border: 1px solid #E0C9A6;
        }
        </style>
    """, unsafe_allow_html=True)

local_css()

# ================= LOGIN ADMIN =================
USUARIO_ADMIN = "LUCIENE"
SENHA_ADMIN = "LuBezerra520"

# ================= DADOS DO SALÃO =================
SERVICOS = {
    "Terapia Capilar": "Tratamento especializado para queda, oleosidade e saúde do couro cabeludo.",
    "Mechas & Coloração": "Técnicas avançadas para iluminar e transformar seu visual com saúde.",
    "Corte Design": "Cortes personalizados que valorizam seu rosto e estilo.",
    "Alisamento Terapêutico": "Redução de volume com foco na integridade da fibra capilar.",
    "Tratamentos VIP": "Cronograma capilar personalizado com as melhores marcas do mercado."
}

# ================= NAVEGAÇÃO =================
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)
    else:
        st.title("Lu Bezerra")
    
    st.markdown("---")
    menu = st.radio("Navegação", ["Início", "Serviços", "Agendamento", "Blog & Dicas", "Área Profissional"])
    st.markdown("---")
    st.info("📍 Localização: Sua Cidade, Estado")

# ================= PÁGINA INICIAL =================
if menu == "Início":
    st.markdown(f"""
        <div class="hero-section">
            <h1 style="font-size: 3rem; margin-bottom: 0;">Lu Bezerra</h1>
            <h3 style="font-weight: 400; color: #8C6A5E;">Terapia Capilar & Estética Avançada</h3>
            <p style="font-size: 1.2rem; color: #6D4C41; max-width: 600px; margin: 20px auto;">
                Ciência e arte unidas para a saúde dos seus fios. 
                Especialista em tratamentos personalizados para o couro cabeludo.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("✨ Nossa Filosofia")
        st.write("""
            Acreditamos que um cabelo bonito começa com um couro cabeludo saudável. 
            Nossos protocolos de **Terapia Capilar** são baseados em diagnósticos precisos 
            e tratamentos personalizados para cada necessidade.
        """)
        st.button("Saiba mais sobre Terapia Capilar")
    
    with col2:
        # Galeria de fotos (usando as imagens existentes)
        imagens_galeria = ["1.jpeg", "2.jpeg", "3.jpeg"]
        cols_img = st.columns(3)
        for i, img_p in enumerate(imagens_galeria):
            if os.path.exists(img_p):
                cols_img[i].image(img_p, use_container_width=True)

    st.divider()
    st.subheader("⭐ Resultados Reais")
    cols_dep = st.columns(5)
    for i in range(1, 6):
        img_path = f"{i}.jpeg"
        if os.path.exists(img_path):
            cols_dep[i-1].image(img_path, caption=f"Resultado {i}", use_container_width=True)

# ================= PÁGINA DE SERVIÇOS =================
elif menu == "Serviços":
    st.title("💎 Nossos Serviços")
    st.write("Oferecemos o que há de mais moderno em tratamentos capilares e estética.")
    
    cols = st.columns(3)
    for i, (servico, desc) in enumerate(SERVICOS.items()):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="service-card">
                    <h3 style="font-size: 1.3rem; margin-top: 0;">{servico}</h3>
                    <p style="color: #666; font-size: 0.9rem;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)
            st.write("") # Espaçador

# ================= PÁGINA DE AGENDAMENTO =================
elif menu == "Agendamento":
    st.title("📅 Agende sua Experiência")
    st.write("Escolha a melhor forma de entrar em contato conosco.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div style="background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #E0C9A6;">
                <h3 style="margin-top: 0;">📞 Atendimento Rápido</h3>
                <p>Clique no botão abaixo para falar diretamente conosco pelo WhatsApp e consultar horários disponíveis.</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.link_button("🟢 Iniciar Conversa no WhatsApp", "https://wa.me/5574988220315")
    
    with c2:
        st.markdown("""
            <div style="background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #E0C9A6;">
                <h3 style="margin-top: 0;">📸 Siga nosso Trabalho</h3>
                <p>Acompanhe as transformações diárias e dicas exclusivas no nosso Instagram oficial.</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.link_button("📸 Ver Instagram Oficial", "https://www.instagram.com/lubezerra_terapiacapilar")

# ================= PÁGINA DE BLOG =================
elif menu == "Blog & Dicas":
    st.title("📚 Espaço Educativo")
    st.write("Dicas de especialistas para manter a saúde do seu cabelo em casa.")
    
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        with st.expander("🧴 Como lavar o cabelo corretamente?"):
            st.write("""
                1. Use água morna ou fria.
                2. Aplique o shampoo apenas no couro cabeludo.
                3. Massageie suavemente com as pontas dos dedos.
                4. Enxágue bem e aplique o condicionador apenas nas pontas.
            """)
    
    with col_b2:
        with st.expander("☀️ Proteção solar para os fios"):
            st.write("""
                Assim como a pele, o cabelo sofre com a radiação UV. 
                Use sempre protetores térmicos com filtro solar antes de se expor ao sol 
                ou usar ferramentas de calor.
            """)

# ================= ÁREA PROFISSIONAL =================
elif menu == "Área Profissional":
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if not st.session_state.logado:
        st.subheader("🔐 Acesso Restrito")
        with st.form("login_form"):
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            if st.form_submit_button("Entrar"):
                if usuario == USUARIO_ADMIN and senha == SENHA_ADMIN:
                    st.session_state.logado = True
                    st.success("Bem-vinda, Luciene!")
                    st.rerun()
                else:
                    st.error("Credenciais inválidas")
    else:
        st.title("🛠 Painel de Gestão & IA")
        
        tab1, tab2, tab3 = st.tabs(["🤖 Assistente Técnico", "✍️ Marketing", "📊 Gestão"])
        
        with tab1:
            st.subheader("Análise Técnica")
            queixa = st.text_area("Descreva a queixa do cliente:")
            if st.button("Gerar Parecer Técnico"):
                st.info("Gerando análise baseada em protocolos de Terapia Capilar...")
                st.markdown(f"**Análise para:** {queixa}")
                st.success("Protocolo sugerido: Desintoxicação bulbar + Laserterapia de baixa intensidade.")
        
        with tab2:
            st.subheader("Criador de Conteúdo")
            opcao = st.selectbox("O que deseja criar?", ["Legenda Instagram", "Frase do Dia", "Prompt para Imagem"])
            if st.button("Gerar Conteúdo"):
                frases = [
                    "A saúde do seu fio começa na raiz. ✨",
                    "Terapia capilar não é luxo, é saúde. 💆‍♀️",
                    "Transforme sua autoestima através do cuidado capilar. 💎"
                ]
                st.success(f"Conteúdo gerado: '{random.choice(frases)}'")
        
        with tab3:
            st.subheader("Resumo do Salão")
            st.write("Funcionalidade em desenvolvimento: Integração com banco de dados de clientes.")

        if st.sidebar.button("Sair do Painel"):
            st.session_state.logado = False
            st.rerun()
