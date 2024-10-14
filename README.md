# 📂 Visualizador de Arquivos com Flask

Este projeto é uma aplicação web desenvolvida com **Flask** que permite o upload, visualização e gerenciamento de arquivos. Ele suporta diversos tipos de arquivos como PDF, CSV e imagens, e oferece uma interface simples e intuitiva para visualizar os arquivos diretamente no navegador.

## 🚀 Funcionalidades

- **Upload de arquivos multitype** usando `multipart/form-data`.
- **Visualização interativa** de arquivos PDF e imagens.
- Gerenciamento simples de arquivos com opção de exclusão.
- Design **responsivo** utilizando **Bootstrap**.
- Suporte a diferentes tipos de arquivos: PDF, CSV, imagens e mais.

---

## 🛠️ Tecnologias Utilizadas

- **Flask**: Framework web para o back-end.
- **Bootstrap**: Framework CSS para o design responsivo.
- **Jinja2**: Para renderização de templates.
- **HTML5 e CSS3**: Para a interface do usuário.

---

## 📥 Como Instalar e Rodar o Projeto

### Pré-requisitos

- **Python 3.6+**
- **pip**: Gerenciador de pacotes do Python
- **Virtualenv** (opcional, mas recomendado)

### Siga os passos abaixo para rodar o projeto no seu ambiente:

### 🖥️ Windows:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Inicie o servidor Flask:
   ```bash
   flask run
   ```

6. Abra o navegador e acesse:
   ```
   http://127.0.0.1:5000
   ```

---

### 🍎 Mac:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   ```

3. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Inicie o servidor Flask:
   ```bash
   flask run
   ```

6. Abra o navegador e acesse:
   ```
   http://127.0.0.1:5000
   ```

---

### 🐧 Linux:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   ```

3. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Exporte a variável de ambiente para Flask:
   ```bash
   export FLASK_APP=main.py
   ```

6. Inicie o servidor Flask:
   ```bash
   flask run
   ```

7. Abra o navegador e acesse:
   ```
   http://127.0.0.1:5000
   ```

---

## 🗂️ Estrutura do Projeto

```bash
├── static
│   └── favicon.png  # Seu favicon
├── templates
│   ├── base.html    # Template base
│   ├── upload.html  # Página de upload
│   └── view_pdf.html# Página de visualização de PDF
├── app.py           # Arquivo principal da aplicação
├── requirements.txt # Dependências do projeto
└── README.md        # Documentação do projeto
```

---

## 📝 Como Utilizar a Aplicação

1. **Faça upload** de um arquivo na página principal.
2. Após o upload, **visualize** PDFs e imagens diretamente no navegador.
3. Para arquivos não visualizáveis diretamente (como CSV), você pode baixá-los ou deletá-los.
4. Use a interface para **gerenciar seus arquivos** de forma simples.

---

## 📂 Dependências

As principais bibliotecas usadas neste projeto estão listadas no arquivo `requirements.txt`:
```text
Flask==2.0.1
Flask-Uploads==0.2.1
Werkzeug==2.0.1
```

---

## 🛠️ Possíveis Melhorias Futuras

- 📊 Suporte a visualização de mais tipos de arquivos (como `.txt` e `.csv` diretamente na interface).
- 📈 Melhorias na usabilidade e feedback ao usuário durante o upload.
- 🚀 Deploy em plataformas como **Heroku** ou **AWS**.

---

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias.

---

## 🧑‍💻 Autor

Desenvolvido por **[thaleson silva](https://www.linkedin.com/in/thaleson-silva/)**. Vamos nos conectar no LinkedIn para trocar ideias!

