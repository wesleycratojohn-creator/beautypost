import streamlit as st
import random
import base64
from PIL import Image

# ================= CONFIG =================
st.set_page_config(
    page_title="Lu Bezerra | Terapia Capilar",
    layout="wide"
)

# ================= FUNDO COM LOGO =================
def fundo_com_logo(img_path):
    with open(img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

fundo_com_logo("logo.png")

# ================= LOGIN =================
USUARIO_ADMIN = "LUCIENE"
SENHA_ADMIN = "LuBezerra520"

# ================= BASES PROFISSIONAIS =================
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

PROMPTS_PROFISSIONAIS = [
    "Crie uma resposta profissional sobre queda capilar com linguagem técnica e acessível.",
    "Explique a importância da avaliação tricossistêmica para clientes leigos.",
    "Gere uma orientação profissional para couro cabeludo oleoso.",
    "Crie um texto educativo sobre saúde capilar e autocuidado."
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

# ================= MENU =================
st.sidebar.title("Menu")
pagina = st.sidebar.radio("", ["Cliente", "Área Profissional"])

# ================= CLIENTE (NÃO ALTERADO) =================
if pagina == "Cliente":
    st.markdown("<h1>💆‍♀️ Terapia Capilar Especializada</h1>", unsafe_allow_html=True)
    st.markdown("**Cuidado avançado para couro cabeludo e fios.**")

    st.divider()

    st.subheader("⭐ O que nossos clientes dizem")
    cols = st.columns(5)
    imagens = ["1.jpeg", "2.jpeg", "3.jpeg", "4.jpeg", "5.jpeg"]

    for col, img in zip(cols, imagens):
        col.image(Image.open(img), width=230)

    st.divider()

    st.subheader("📞 Contato")
    c1, c2 = st.columns(2)

    with c1:
        st.link_button("🟢 WhatsApp", "https://wa.me/5574988220315")

    with c2:
        st.link_button("📸 Instagram", "https://www.instagram.com/lubezerra_terapiacapilar")

# ================= ÁREA PROFISSIONAL =================
elif pagina == "Área Profissional":

    if "logado" not in st.session_state:
        st.session_state.logado = False

    if not st.session_state.logado:
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            if usuario == USUARIO_ADMIN and senha == SENHA_ADMIN:
                st.session_state.logado = True
                st.success("Login realizado")
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos")

    else:
        # ===== EXISTENTE =====
        st.subheader("🧑‍⚕️ Resposta Técnica Profissional")
        problema = st.text_input("Informe a queixa capilar do cliente")

        if st.button("Gerar resposta técnica"):
            if problema:
                st.markdown(gerar_resposta(problema))

        st.divider()

        # ===== NOVOS RECURSOS (APENAS ADIÇÃO) =====
        st.subheader("✍️ Gerador de Frases Profissionais")
        if st.button("Gerar frase profissional"):
            st.success(random.choice(FECHAMENTO))

        st.subheader("📸 Gerador de Legendas para Instagram")
        if st.button("Gerar legenda"):
            st.info(random.choice(LEGENDAS_INSTAGRAM))

        st.subheader("🧠 Gerador de Prompts Profissionais")
        if st.button("Gerar prompt"):
            st.code(random.choice(PROMPTS_PROFISSIONAIS))

        if st.button("🚪 Logout"):
            st.session_state.logado = False
            st.rerun()
