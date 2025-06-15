import streamlit as st
import google.generativeai as genai
from datetime import date

# Configuração da página
st.set_page_config(page_title="Planejador de Viagens com IA", page_icon="✈️")
st.title("✈️ Planejador de Viagens com IA")
st.write("Receba um roteiro personalizado com sugestões de passeios, horários e dicas de viagem!")

# Formulário com campos organizados
with st.form("form_viagem"):
    destino = st.text_input("🌍 Destino da viagem")
    col1, col2 = st.columns(2)
    with col1:
        data_inicio = st.date_input("📅 Data de início", value=date.today())
    with col2:
        data_fim = st.date_input("📅 Data de término", value=date.today())

    tipo_viagem = st.selectbox("🎯 Tipo de viagem", [
        "Cultural", "Gastronômica", "Relaxar", "Aventura", "Romântica", "Natureza"])
    orcamento = st.slider("💸 Orçamento estimado (opcional)",
                          0, 10000, 5000, step=500)
    gerar = st.form_submit_button("✨ Gerar Roteiro com IA")

# Validação e geração do roteiro
if gerar and destino and data_inicio <= data_fim:
    dias = (data_fim - data_inicio).days + 1
    st.info(f"🔎 Gerando roteiro para {destino} com duração de {dias} dias...")

    # Configura a API Gemini
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash-latest")

    # Prompt para a IA
    prompt = f"""
    Você é um guia de viagens experiente e amigável. Crie um roteiro turístico completo para visitar {destino} entre os dias {data_inicio.strftime('%d/%m/%Y')} e {data_fim.strftime('%d/%m/%Y')}.

    O estilo da viagem é {tipo_viagem.lower()} e o orçamento disponível é de R$ {orcamento}.
    Para cada dia, sugira:
    - Atividades com horários (use emojis para representar o tipo de atividade)
    - Lugares para comer ou visitar
    - Dicas locais (transporte, moeda, clima)
    Use linguagem clara e organizada por dia. Formate como uma lista.
    """

    with st.spinner("⏳ Consultando IA e montando seu roteiro..."):
        response = model.generate_content(prompt)

    st.success("✅ Roteiro gerado com sucesso!")
    st.subheader("📋 Seu roteiro personalizado")
    st.markdown(response.text)
    st.download_button("📥 Baixar roteiro (.txt)",
                       response.text, file_name="roteiro_viagem.txt")

elif gerar:
    st.warning("⚠️ Preencha o destino e selecione um intervalo de datas válido.")
