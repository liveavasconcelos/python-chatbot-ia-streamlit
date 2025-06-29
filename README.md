# 🤖 ChatBot com IA usando Streamlit
Este projeto é um ChatBot inteligente criado com Python, utilizando Streamlit para interface e integração com OpenAI para gerar respostas automáticas com inteligência artificial.
Foi desenvolvido durante a **Imersão Python** promovida pela [Hashtag Treinamentos](https://https://www.hashtagtreinamentos.com/).

## 🛠 Tecnologias Utilizadas
- Python
- Streamlit
- OpenAI API
- Interface chat_message do Streamlit

## 💡 Funcionalidades
- Interface amigável via navegador com Streamlit
- Entrada de mensagens do usuário
- Exibição do histórico do chat
- Integração com o modelo GPT-4o da OpenAI
- Resposta automática com IA baseada no histórico da conversa

## 📁 Estrutura do Projeto
```
📦python-chatbot-ia-streamlit
 ┣ 📄main.py
 ┗📄README.md
```

## 🚀 Como Executar o Projeto
1. **Clone o repositório**
```bash
git clone https://github.com/liveavasconcelos/python-chatbot-ia-streamlit.git
cd python-chatbot-ia-streamlit
```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install openai streamlit
```

4. **Configure sua chave da API da OpenAI:**
No arquivo main.py, substitua:

```python
modelo = OpenAI(api_key="cole a chave da API aqui")
pela sua chave real da OpenAI, que você encontra em: https://platform.openai.com/account/api-keys
```

5. **Execute a aplicação:**
```bash
streamlit run main.py
```

## ✅ Exemplo de Uso:
Quando o usuário digita uma mensagem, ela aparece no chat e a IA responde automaticamente, mantendo o histórico da conversa:

```text
Usuário: Olá, tudo bem?
IA: Olá! Estou bem, obrigado. Como posso te ajudar hoje?
```

## 📌 Observações
- ⚠️Você precisa de uma conta na OpenAI para gerar sua chave de API.
- O projeto usa st.session_state para armazenar o histórico das mensagens.

## 📚 Sobre o Projeto
Projeto desenvolvido durante a Imersão Python da Hashtag Treinamentos, com adaptações e melhorias pessoais.

## 👩🏻‍💻 Autora
Livea Mendes de Vasconcelos

[GitHub](https://github.com/liveavasconcelos) | [Linkedin](https://www.linkedin.com/in/livea-vasconcelos/)
