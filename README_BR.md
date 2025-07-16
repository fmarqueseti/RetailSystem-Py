# RetailSystem-Py

**RetailSystem-Py** é um sistema educacional de gerenciamento de vendas desenvolvido em Python. O projeto foi construído como parte do curso *"Python do básico ao avançado + Inteligência Artificial"*, ministrado por **Caio Sampaio** da plataforma **Pythonando**.

O sistema possui duas versões:
- Interface texto (modo console)
- Interface gráfica (utilizando **Tkinter**)

Além disso, integra banco de dados MySQL.

---

## 📌 Objetivos

- Praticar os fundamentos e recursos avançados da linguagem Python
- Integrar banco de dados relacionais com aplicações Python
- Criar interfaces gráficas com Tkinter
- Explorar boas práticas como modularização e internacionalização de sistemas

---

## 📁 Estrutura do Projeto

```
RetailSystem-Py/
│
├── doc/
│   ├── DER.png                 # Diagrama Entidade-Relacionamento
│   ├── schema.sql              # Criação e carga inicial do banco de dados
└── src/
    ├── txt/                    # Versão com interface texto
    │   ├── myERP.py            # Arquito principal
    │   ├── mysql_conn.py       # Detalhes de conexão ao banco de dados mysql
    │   ├── myUtil.py           # Funções utilitárias
    │   ├── ordersMenu.py       # Menu de pedidos
    │   ├── productsMenu.py     # Menu de produtos
    │   └── statisticsMenu.py   # Menu de estatísticas de vendas (gráficos)
    │
    └── tkinter/                # Versão com interface gráfica (tkinter)
        ├── myERP.py            # Arquito principal
        ├── connection.py       # Classe de conexão ao banco de dados mysql
        ├── login.py            # Classe de login/signup
        ├── mainMenu.py         # Classe do menu principal
        ├── ordersList.py       # Classe de pedidos
        ├── productsMenu.py     # Classe do menu de produtos
        └── statistics.py       # Classe de estatísticas de vendas (gráficos)
```

---

## 🧠 Estrutura do Banco de Dados

O sistema utiliza um banco de dados relacional MySQL com as seguintes entidades principais:

- **Product**: Cadastro de produtos com nome, ingredientes, categoria e valor.
- **Ordem Item**: Registro de vendas com itens vendidos e ainda não entregues.
- **Ordem History**: Registro de vendas com histórico de itens vendidos.
- **User**: Para controle de acesso.

O script `schema.sql` no diretório `doc` pode ser utilizado para criar e popular o banco com dados de exemplo.

---

## ⚙️ Regras de Negócio

- Cadastro, alteração e exclusão de produtos, organizados por categoria
- Registro de vendas com controle de baixa de pedidos entregues
- Estatísticas de vendas por valor e quantidade (gráficos)

---

## 🌐 Internacionalização

O sistema foi adaptado para o idioma **inglês**, incluindo:
- Tradução completa dos menus e mensagens
- Renomeação de campos e estruturas do banco de dados
- Padronização dos nomes de arquivos e módulos em inglês

---

## 🧩 Pré-requisitos

Para rodar o sistema, é necessário instalar os seguintes pacotes Python:

```bash
pip install pymysql matplotlib
```
---

## 🚀 Como Executar

### Interface Texto:

```bash
python3 myERP.py
```

Certifique-se de que o banco de dados MySQL está configurado e acessível. Use o script `schema.sql` para prepará-lo.

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!  
Sinta-se à vontade para:

- Abrir **issues** com sugestões ou melhorias
- Criar uma **pull request** com correções ou novas funcionalidades
- Compartilhar ideias para expandir o projeto

---

## 📄 Licença

Este projeto é licenciado sob a Licença MIT.  
Consulte o a [licença](https://github.com/fmarqueseti/RetailSystem-Py?tab=MIT-1-ov-file) para mais detalhes.

---

## 📚 Créditos

Curso: *Python do básico ao avançado + Inteligência Artificial*  
Instrutor: **Caio Sampaio** — [Pythonando](https://www.pythonando.com.br)

Desenvolvido e aprimorado por: [**Fábio Marques**](https://www.linkedin.com/in/fmrqs/)

---