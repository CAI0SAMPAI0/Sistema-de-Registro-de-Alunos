Sistema de Registro de Alunos

Aplicação desktop desenvolvida em Python utilizando Tkinter para interface gráfica e SQLite3 como banco de dados local. O sistema permite cadastrar, visualizar, atualizar e deletar registros de alunos, incluindo imagem associada.

Objetivo

Fornecer um sistema simples e funcional para gerenciamento de alunos, com persistência de dados local e interface gráfica intuitiva.

Tecnologias Utilizadas

Python 3.12+

Tkinter (interface gráfica)

SQLite3 (banco de dados local)

Pillow (manipulação de imagens)

tkcalendar (seleção de datas)

pathlib (controle profissional de caminhos)

Funcionalidades

Cadastro de aluno com:

Nome

Email

Telefone

Sexo

Data de nascimento

Endereço

Curso

Foto

Busca por ID

Atualização de registro

Exclusão de registro

Listagem completa em tabela dinâmica

Instalação

Clone o repositório ou copie o projeto.

Acesse a pasta raiz do projeto:

cd alunos

Instale as dependências necessárias:

pip install pillow tkcalendar

Tkinter e SQLite já vêm com a instalação padrão do Python.

Execução Correta

Execute o sistema a partir da raiz do projeto usando módulo:

python -m ui.interface

Não execute diretamente interface.py, pois isso pode causar erro de importação de módulos.

Banco de Dados

O banco SQLite é criado automaticamente na pasta:

data/estudante.db

A tabela estudantes é criada automaticamente caso não exista.

Estrutura da tabela:

id (INTEGER PRIMARY KEY AUTOINCREMENT)

nome (TEXT)

email (TEXT)

tel (TEXT)

sexo (TEXT)

data_nascimento (TEXT)

endereco (TEXT)

curso (TEXT)

picture (TEXT)

Arquitetura

O projeto está dividido em camadas:

UI (ui/interface.py)
Responsável pela interface gráfica e interação com o usuário.

Banco (data/banco.py)
Responsável exclusivamente pelas operações no banco de dados.

Assets (images/)
Imagens utilizadas na interface.

Separação clara entre interface e persistência de dados.

Boas Práticas Aplicadas

Uso de pathlib para manipulação segura de caminhos.

Separação de responsabilidades (UI ≠ Banco).

Banco criado dinamicamente.

Estrutura modular com pacotes Python.

Uso de __init__.py para organização como pacote.

Melhorias Futuras

Validação mais robusta de campos (email, telefone).

Tratamento de exceções no banco de dados.

Implementação de busca por nome.

Paginação na tabela.

Empacotamento em executável (.exe).

Implementação de padrão MVC mais estruturado.

Requisitos Mínimos

Windows 10+

Python 3.12+

4GB de RAM

Autor

Caio
Curso: Sistemas de Informação