<h1 align="center">Registration of People</h1>

<p>
Esse é um projeto em Django de um sistema de cadastro de pessoas utilizando a linguagem de programação Python e o framework Django.
O acesso ao banco de dados SQLite foi feito totalmente pelo ORM do Django, a estrutura sql do banco também está disponível nesse projeto, mas não sera preciso criar o banco ele está dentro do projeto. 
</p>


## Pré-requisitos

###### 1 - Ter o python instalado:
- É necessário ter o python instalado
- Se ele não estiver instalado baixe e instale pelo site oficial: https://www.python.org/downloads/

###### 2 - Faça o clone desse repositório em sua máquina:
- Usando o git bash, escolha um diretório de sua preferencia e execute os comandos:
- git clone https://github.com/diogoss120/registration-of-people.git

###### 3 - Crie o ambiente virtual:
- Navegue até a pasta onde foi feito o clone desse repositório
- cd registration-of-people/
- python -m venv venv

###### 4 - Ative o ambiente virtual: 
- source venv/Scripts/activate

###### 5 - Faça a instalação dos pacotes necessários: 
- pip install -r requirements.txt

###### 6 - Inicie o servidor: 
- python manage.py runserver
- Acesse a url http://127.0.0.1:8000/ no seu navegador

#### Para logar no admin 'http://127.0.0.1:8000/admin/':
- Caso deseje acessar o admin, use o usuário 'Diogo' com a senha 'diogo' para fazer o login

#### Navegação pela interface:
- A tela inicial é a tela de cadastro de pessoas, para ver as pessoas já cadastradas clique sobre o link 'Return to list' que fica abaixo do formulário
- Para editar o cadastro de uma pessoa basta clicar sobre o nome dela e a mesma será disponibilizada em um formulário para edição
- Também é possivel gerar nomes aleatórios ao fazer o cadastro de uma nova pessoa, para isso basta clicar sobre o botão 'Generate Name'
- Para adicionar uma nova pessoa, clique sobre o botão New Person e será encaminhado para o formulário de cadastro


## 🛠 Tecnologias
As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [JavaScript](https://www.javascript.com/)
- [Html](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [SQlite](https://www.sqlite.org/index.html)
