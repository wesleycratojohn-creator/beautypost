import streamlit as st
import random
import base64
from PIL import Image
import os
import pandas as pd
from datetime import datetime

# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(
    page_title="Lu Bezerra | Terapia Capilar de Luxo",
    page_icon="💆‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= DESIGN DE ALTO CONTRASTE E LUXO (CSS) =================
def load_enhanced_design():
    # Carrega a logo para o fundo se existir
    bg_img = ""
    if os.path.exists("logo.png"):
        with open("logo.png", "rb") as f:
            bg_img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

        /* Reset e Fontes Globais */
        html, body, [class*="st-"] {{
            font-family: 'Montserrat', sans-serif;
            color: #1A1A1A;
        }}
        
        /* Fundo com Logo e Overlay de Alto Contraste */
        .stApp {{
            background-image: url("data:image/png;base64,{bg_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Overlay para garantir contraste máximo do texto */
        .stApp > div:first-child {{
            background-color: rgba(255, 255, 255, 0.92);
        }}

        /* Sidebar (Gaveta) - Redesign para Sofisticação */
        [data-testid="stSidebar"] {{
            background-color: #1A1A1A !important;
            border-right: 2px solid #D4AF37;
        }}
        
        /* Estilização das Opções do Menu (Contraste Elevado) */
        [data-testid="stSidebar"] .stRadio label {{
            color: #FFFFFF !important;
            font-weight: 500 !important;
            font-size: 1.1rem !important;
            padding: 10px 0 !important;
            transition: 0.3s;
        }}
        
        [data-testid="stSidebar"] .stRadio label:hover {{
            color: #D4AF37 !important;
        }}

        /* Títulos com Elegância e Contraste */
        h1, h2, h3 {{
            font-family: 'Playfair Display', serif;
            color: #000000;
            font-weight: 700;
        }}

        /* Botões de Ação (Estilo Boutique) */
        .stButton>button {{
            width: 100%;
            border-radius: 0px;
            border: 2px solid #1A1A1A;
            background-color: #1A1A1A;
            color: #D4AF37;
            padding: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.4s ease;
        }}
        .stButton>button:hover {{
            background-color: #D4AF37;
            border-color: #D4AF37;
            color: #1A1A1A;
            transform: translateY(-2px);
        }}

        /* Cards de Conteúdo (Sombra Suave e Bordas Definidas) */
        .luxury-card {{
            background-color: #FFFFFF;
            padding: 30px;
            border-radius: 4px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            margin-bottom: 25px;
            border-top: 4px solid #D4AF37;
        }}
        
        /* Ajuste do ícone da gaveta (Streamlit default) */
        button[kind="header"] {{
            background-color: #1A1A1A !important;
            color: #D4AF37 !important;
            border-radius: 50% !important;
        }}
        
        /* Ocultar apenas o fundo e textos do header, mantendo os botões interativos */
        header[data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0) !important;
            color: rgba(0,0,0,0) !important;
        }}
        
        /* Esconder especificamente o texto indesejado sem afetar os ícones */
        header[data-testid="stHeader"] * {{
            color: transparent !important;
            font-size: 0 !important;
        }}
        
        /* Restaurar e estilizar o botão da sidebar (ícone de menu) */
        header[data-testid="stHeader"] button {{
            visibility: visible !important;
            color: #D4AF37 !important; /* Cor dourada para o ícone */
            background-color: #1A1A1A !important; /* Fundo escuro para contraste */
            border-radius: 50% !important;
            width: 45px !important;
            height: 45px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}
        
        /* Garantir que o ícone dentro do botão seja visível */
        header[data-testid="stHeader"] button svg {{
            fill: #D4AF37 !important;
            width: 25px !important;
            height: 25px !important;
            visibility: visible !important;
        }}
        
        /* Garantir que o botão de fechar a gaveta seja visível e elegante */
        [data-testid="stSidebarNav"] button {{
            color: #D4AF37 !important;
        }}
        </style>
    """, unsafe_allow_html=True)

load_enhanced_design()

# ================= SISTEMA DE LOGIN E PERMISSÕES =================
CREDENCIAIS = {
    "admin": {"usuario": "LUCIENE", "senha": "LuBezerra520", "cargo": "Diretoria Executiva"},
    "equipe": {"usuario": "EQUIPE", "senha": "Staff2026", "cargo": "Especialista Técnico"},
    "cliente": {"usuario": "CLIENTE", "senha": "Vip2026", "cargo": "Membro VIP"}
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
        "titulo": "Tricologia Clínica: O Futuro da Saúde Capilar",
        "conteudo": "A análise microscópica do couro cabeludo permite identificar patologias antes mesmo dos primeiros sintomas visíveis.",
        "tipo": "Artigo Científico",
        "data": "15/02/2026"
    },
    {
        "titulo": "Impacto do Estresse no Ciclo Folicular",
        "conteudo": "Estudos recentes comprovam que o cortisol elevado pode antecipar a fase telógena, causando queda acentuada.",
        "tipo": "Estudo Clínico",
        "data": "10/01/2026"
    }
]

# ================= NAVEGAÇÃO (GAVETA REDESENHADA) =================
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.markdown("<h1 style='color: #D4AF37; text-align: center;'>LU BEZERRA</h1>", unsafe_allow_html=True)
    
    st.markdown("<p style='color: #888; text-align: center; font-size: 0.8rem; letter-spacing: 2px;'>TERAPIA CAPILAR AVANÇADA</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    opcoes = ["🏠 Início", "💎 Nossos Protocolos", "📚 Biblioteca Científica", "📅 Agendamento VIP", "🔐 Área de Acesso"]
    
    # Opções dinâmicas baseadas no login
    if st.session_state.cargo == "Diretoria Executiva":
        opcoes.insert(4, "📊 Painel de Gestão")
    elif st.session_state.cargo == "Especialista Técnico":
        opcoes.insert(4, "📋 Prontuários Técnicos")
    elif st.session_state.cargo == "Membro VIP":
        opcoes.insert(4, "🌟 Minha Jornada VIP")

    menu = st.radio("MENU DE NAVEGAÇÃO", opcoes)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.session_state.logado:
        st.markdown(f"<p style='color: #D4AF37; font-size: 0.9rem;'>Perfil: <b>{st.session_state.cargo}</b></p>", unsafe_allow_html=True)
        if st.button("ENCERRAR SESSÃO"):
            st.session_state.logado = False
            st.session_state.cargo = "Visitante"
            st.rerun()
    else:
        st.markdown("<p style='color: #666; font-size: 0.8rem;'>Acesse sua conta para recursos exclusivos.</p>", unsafe_allow_html=True)

# ================= PÁGINA: INÍCIO =================
if menu == "🏠 Início":
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>Lu Bezerra</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #D4AF37; letter-spacing: 4px;'>EXCELÊNCIA EM TRICOLOGIA</p>", unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 🔬 Ciência e Sofisticação")
        st.write("""
            Combinamos o rigor científico da tricologia com o acolhimento de um spa de luxo. 
            Cada tratamento é precedido por uma análise microscópica detalhada, garantindo 
            que seu protocolo seja único e focado em resultados reais.
        """)
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("SOLICITAR CONSULTA PRIVADA", "https://wa.me/5574988220315")
    
    with col2:
        st.markdown("### ⭐ Resultados de Excelência")
        cols_res = st.columns(3)
        for i in range(1, 4):
            img_p = f"{i}.jpeg"
            if os.path.exists(img_p):
                cols_res[i-1].image(img_p, use_container_width=True, caption=f"Caso {i}")

# ================= PÁGINA: SERVIÇOS =================
elif menu == "💎 Nossos Protocolos":
    st.markdown("<h1 style='text-align: center;'>Protocolos Exclusivos</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Tecnologia de ponta para a saúde dos seus fios.</p>", unsafe_allow_html=True)
    
    servicos = {
        "Terapia Capilar Molecular": "Tratamento profundo que atua na regeneração da fibra e saúde do couro cabeludo.",
        "Laserterapia de Alta Precisão": "Uso de luz de baixa intensidade para bioestimulação do folículo piloso.",
        "Detox Bulbar Sistêmico": "Protocolo de desintoxicação profunda para otimizar o crescimento capilar.",
        "Spa Capilar Sensorial": "Uma experiência de relaxamento profundo aliada a tratamentos de alta performance."
    }
    
    cols = st.columns(2)
    for i, (s, d) in enumerate(servicos.items()):
        with cols[i % 2]:
            st.markdown(f"""
                <div class="luxury-card">
                    <h3 style="color: #D4AF37; margin-top: 0;">{s}</h3>
                    <p style="font-size: 1rem; line-height: 1.6;">{d}</p>
                    <hr style="border: 0.5px solid #EEE;">
                    <p style="font-size: 0.8rem; color: #888;">Duração média: 90 minutos</p>
                </div>
            """, unsafe_allow_html=True)

# ================= PÁGINA: BIBLIOTECA CIENTÍFICA =================
elif menu == "📚 Biblioteca Científica":
    st.title("Biblioteca Científica")
    st.write("Artigos e estudos fundamentados para sua segurança e conhecimento.")
    
    for art in ARTIGOS:
        with st.container():
            st.markdown(f"""
                <div style="background-color: #FDFDFD; padding: 20px; border-left: 4px solid #1A1A1A; margin-bottom: 20px;">
                    <span style="background-color: #D4AF37; color: #1A1A1A; padding: 2px 8px; font-size: 0.7rem; font-weight: bold;">{art['tipo']}</span>
                    <h3 style="margin: 10px 0;">{art['titulo']}</h3>
                    <p style="color: #444;">{art['conteudo']}</p>
                    <p style="font-size: 0.7rem; color: #999;">Publicado em: {art['data']}</p>
                </div>
            """, unsafe_allow_html=True)

# ================= PÁGINA: AGENDAMENTO =================
elif menu == "📅 Agendamento VIP":
    st.title("Agendamento VIP")
    st.write("Atendimento exclusivo com hora marcada.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class="luxury-card">
                <h3>📱 WhatsApp Concierge</h3>
                <p>Fale diretamente com nossa equipe para encontrar o melhor horário.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("INICIAR CONVERSA", "https://wa.me/5574988220315")
    with c2:
        st.markdown("""
            <div class="luxury-card">
                <h3>📸 Instagram Oficial</h3>
                <p>Acompanhe nosso dia a dia e novidades exclusivas.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("VER PERFIL", "https://www.instagram.com/lubezerra_terapiacapilar")

# ================= PÁGINA: ÁREA DE ACESSO (LOGIN) =================
elif menu == "🔐 Área de Acesso":
    if not st.session_state.logado:
        st.markdown("<h1 style='text-align: center;'>Acesso Privado</h1>", unsafe_allow_html=True)
        
        col_l, col_c, col_r = st.columns([1, 2, 1])
        with col_c:
            st.markdown("<div class='luxury-card'>", unsafe_allow_html=True)
            u = st.text_input("Usuário")
            s = st.text_input("Senha", type="password")
            if st.button("AUTENTICAR"):
                if realizar_login(u, s):
                    st.success(f"Bem-vindo(a), {st.session_state.cargo}!")
                    st.rerun()
                else:
                    st.error("Credenciais inválidas.")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.success(f"Sessão ativa como {st.session_state.cargo}.")
        st.write("Utilize o menu lateral para acessar suas ferramentas exclusivas.")

# ================= PAINÉIS ESPECÍFICOS =================
elif menu == "📊 Painel de Gestão":
    st.title("Dashboard Executivo")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Faturamento Mensal", "R$ 48.500", "+8%")
    m2.metric("Novos VIPs", "12", "+2")
    m3.metric("Taxa de Retorno", "92%", "Estável")
    m4.metric("Consultas IA", "156", "+24%")
    
    st.divider()
    st.subheader("🤖 Inteligência de Mercado")
    if st.button("GERAR INSIGHT DE MARKETING"):
        insights = [
            "Tendência: Aumento de 20% na busca por tratamentos orgânicos para couro cabeludo sensível.",
            "Sugestão: Criar campanha focada em 'Saúde Capilar Pós-Verão' para o próximo mês.",
            "Insight: Clientes VIP preferem agendamentos entre 14h e 17h nas terças-feiras."
        ]
        st.info(random.choice(insights))

elif menu == "📋 Prontuários Técnicos":
    st.title("Gestão Técnica")
    paciente = st.selectbox("Selecione o Paciente", ["Ana Silva", "Carlos Oliveira", "Mariana Santos"])
    st.markdown(f"<div class='luxury-card'><h3>Ficha: {paciente}</h3><p>Protocolo: <b>Regeneração Folicular Nível 2</b></p></div>", unsafe_allow_html=True)
    
    if st.button("REGISTRAR EVOLUÇÃO"):
        st.success("Evolução salva no prontuário digital.")

elif menu == "🌟 Minha Jornada VIP":
    st.title("Sua Jornada de Saúde")
    st.write("Acompanhe seu progresso e benefícios exclusivos.")
    
    st.progress(85)
    st.caption("85% do seu protocolo concluído. Você está quase lá!")
    
    st.divider()
    st.subheader("🎁 Seus Mimos VIP")
    st.write("✅ 15% de desconto em toda linha Home Care.")
    st.write("✅ Acesso antecipado a novos protocolos.")
    st.write("✅ Check-up capilar semestral cortesia.")
