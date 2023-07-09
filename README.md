# :shopping: Mercado Moderno
### :hammer_and_wrench: Em Desenvolvimento!

## :bookmark_tabs: Sobre o Mercado Moderno
O Mercado Moderno é uma aplicação Web de um mercado online, onde é possível configurar uma loja e cadastrar produtos para que outras pessoas possam fazer suas compras online.
Este é um projeto desenvolvido para a disciplina de Projeto Integrado, da Universidade Federal do Espírito Santo (<a href="ufes.br">UFES</a>)

## :wrench: Configurações Iniciais

Essas são as instruções iniciais para configurar o projeto localmente. 

### Pré-requisitos

Essas são as ferramentas necessárias que você vai precisar ter instaladas para rodar o projeto:
* python - v3.10
* node.js -
* npm -

## :computer: Instalação

Clone o repositório ou faça o download dos arquivos
```bash
git clone https://github.com/LucasGaabriel/Mercado-Moderno.git
```

### Inicializando o Backend

Entre no diretório do backend:
```bash
cd backend
```

Configure um novo ambiente virtual para isolar as dependências do projeto: 
```bash
python -m venv venv
```

Ative o ambiente virtual:
* Linux ou macOS:
```bash
source venv/bin/activate
```
* Windows:
```bash
venv/Scripts/Activate
```

Para desativar um ambiente virtual, utilize o comando: ```deactivate```

Instale as dependências:
```bash
pip install .
```

Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

Crie um superusuário para acessar a área administrativa:
```bash
python manage.py createsuperuser
```

Rode a aplicação:
```bash
python manage.py runserver
```

--------------------------

### Inicializando o Frontend

Entre no diretório do frontend:
```bash
cd frontend
```

## :closed_lock_with_key: Licença

Este projeto é licenciado sob a Licença MIT. Veja [LICENSE](LICENSE.txt) para mais detalhes.

## :technologist: Colaboradores
* Daniel Siqueira - daniel.oliveira.17@edu.ufes.br / [Github](https://github.com/siqueiradaniel)
* Lucas Gabriel - lucas.go.costa@edu.ufes.br / [Github](https://github.com/LucasGaabriel)
