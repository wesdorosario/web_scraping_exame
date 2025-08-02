# O que é este projeto?
- Este é um projeto de Web Scraping (raspagem de dados) feito em Python, que tem como objetivo extrair publicações de uma página específica de notícias do site Exame (https://exame.com/).

# Bibliotecas Utilizadas:
- requests: para fazer requisições HTTP e obter o conteúdo da página.
- BeautifulSoup: para analisar o HTML da página e extrair as informações desejadas.

# O que esse código faz?
- Acessa uma URL específica do site Exame.
- Extrai as últimas publicações (títulos) da página de uma seção específica do site e seus respectivos links. 
- Salva as informações em um arquivo de texto chamado "resultado_web_scraping.txt" automaticamente de forma organizada.

# Como usar:
1. Certifique-se de ter o Python instalado em seu computador.  
   (A versão usada neste código foi Python 3.12.3)

2. Instale as bibliotecas necessárias, se ainda não estiverem instaladas:

### 2.1 Crie um ambiente virtual (ALTAMENTE recomendado)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/MacOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.2 Instale as dependências com:

```bash
pip install -r requirements.txt
```

3. Usando o programa:

#### 3.1 Edite o arquivo `main.py` e insira a URL da página que deseja raspar na variável `url`.

#### 3.2 Execute o script com:

```bash
python main.py
```

4. Após a execução, verifique o arquivo `resultado_web_scraping.txt` para ver as publicações extraídas.

5. Você pode usar quantas URLs quiser. Basta alterar a variável `url` no código e executar novamente.

⚠️ **Atenção:** A cada raspagem o arquivo `resultado_web_scraping.txt` será sobrescrito, ou seja, as publicações anteriores serão perdidas.

# Observações:
- Esse código foi projetado para funcionar com a estrutura atual do site da Exame. Se o site for alterado, pode ser necessário ajustar o código. Então basicamente basta escolher um tópico de notícias e seguir as instruções acima.
