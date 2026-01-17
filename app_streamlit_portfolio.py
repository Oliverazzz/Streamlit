app.py

import streamlit as st import pandas as pd import plotly.express as px

—————————

CONFIGURAÇÃO DA PÁGINA

—————————

st.set_page_config( page_title=“Luiz Oliveira | Portfólio”,
page_icon=“💼”, layout=“wide” )

—————————

CABEÇALHO

—————————

st.title(“💼 Luiz Oliveira”) st.subheader(“Programação CNC • Automação •
Eletrônica • Desenvolvimento”)

st.write(““” Bem-vindo ao meu portfólio interativo desenvolvido em
Streamlit.
Aqui você verá projetos, gráficos, integração de dados e mídia. “““)

st.divider()

—————————

SIDEBAR

—————————

st.sidebar.title(“📌 Navegação”) menu = st.sidebar.radio( “Ir para:”,
[“🏠 Início”, “🛠️ Projetos”, “📊 Dados”, “🎥 Vídeo”, “📩 Contato”] )

—————————

PÁGINA INÍCIO

—————————

if menu == “🏠 Início”: col1, col2 = st.columns(2)

    with col1:
        st.header("Sobre mim")
        st.write("""
        Operador e programador CNC, programador CLP/IHM, 
        eletricista industrial e desenvolvedor de soluções automatizadas.
        Experiência em Siemens, Fanuc, Mastercam, Arduino e sistemas embarcados.
        """)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1600880292203-757bb62b4baf",
            caption="Tecnologia e Automação",
            use_container_width=True
        )

—————————

PÁGINA PROJETOS

—————————

elif menu == “🛠️ Projetos”: st.header(“🛠️ Projetos em destaque”)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🔧 Central eletrônica de motor em C++")
        st.write("Controle de ignição e injeção baseado em roda fônica.")

    with col2:
        st.info("⚙️ Programação CNC Siemens/Fanuc")
        st.write("Automação de usinagem e otimização de tempo de ciclo.")

    with col3:
        st.info("🌐 Sites interativos")
        st.write("Web apps com pagamento, QR Code e hospedagem automática.")

—————————

PÁGINA DADOS

—————————

elif menu == “📊 Dados”: st.header(“📊 Demonstração de conexão com
dados”)

    df = pd.DataFrame({
        "Dia": ["Seg", "Ter", "Qua", "Qui", "Sex"],
        "Peças Produzidas": [120, 150, 180, 170, 200]
    })

    st.dataframe(df)

    fig = px.bar(df, x="Dia", y="Peças Produzidas", title="Produção Semanal")
    st.plotly_chart(fig, use_container_width=True)

—————————

PÁGINA VÍDEO

—————————

elif menu == “🎥 Vídeo”: st.header(“🎥 Demonstração em vídeo”)
st.video(“https://www.youtube.com/watch?v=R2nr1uZ8ffc”)

—————————

PÁGINA CONTATO

—————————

elif menu == “📩 Contato”: st.header(“📩 Entre em contato”)

    nome = st.text_input("Seu nome")
    email = st.text_input("Seu e-mail")
    mensagem = st.text_area("Mensagem")

    if st.button("Enviar"):
        st.success("Mensagem enviada! (simulação)")

—————————

RODAPÉ

—————————

st.divider() st.caption(“Portfólio desenvolvido em Streamlit 🚀”)
