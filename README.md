# ✈️ Planejador de Viagens com IA

Este projeto é um **Software as a Service (SaaS)** desenvolvido com **Streamlit** que gera roteiros personalizados de viagem utilizando inteligência artificial (IA), através da API **Gemini** do Google.

---

## 💡 Funcionalidades

- Receba um roteiro completo com sugestões de passeios, horários, alimentação e dicas locais
- Personalize destino, datas, tipo de viagem e orçamento
- IA com linguagem natural e uso de emojis para tornar o plano mais visual e intuitivo
- Interface leve, interativa e responsiva
- Download do roteiro em `.txt`

---

## 🛠️ Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) — para criar a interface
- [Google Gemini API](https://ai.google.dev/) — para gerar os roteiros com IA
- Python 3.9+

---

## 🚀 Como Executar Localmente

1. Clone este repositório:
```https://github.com/Majorphd/planejador-viagens-ia.git```
cd planejador-viagens-ia

2. Instale as dependências:
pip install -r requirements.txt

3. Crie um arquivo .streamlit/secrets.toml ou use st.secrets:
GEMINI_API_KEY = "cole-sua-chave-da-api"

4. Execute o projeto:
streamlit run app.py

## 🔗 Acesse o app online:
👉 [Clique aqui para acessar o app no Streamlit](https://planejador-viagens-ia-o4urktanhcunkgcg3npprz.streamlit.app)

👥 Integrantes do Grupo
Paulo Henrique Dantas Teodósio RGM:40068170


📌 Observações
A API Gemini foi escolhida por ser gratuita e ensinada em aula
A chave de API está protegida por meio do recurso st.secrets


Projeto apresentado na disciplina de Fundamentos de Inteligência Artificial no curso de Ciência da Computação – 6º período.
