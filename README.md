# myfilms
Desafio:
    1 - Criar um sistema de controle de filmes já assistidos.

    2 - Ele deve conter uma forma de cadastrar os filmes, cadastrar quando o filme foi assistido, e um que gostaria.

    3 - Importar uma planilha de excel com os filmes usando celery

    4 - No frontend, ter um autocomplete que lista os filmes para assim, registrar sua visualização

    5 - Um relatório com chart.js mostrando quais filmes você já assistiu, quais você ainda não e quais você gostaria.

Candidato: Lucca Torrezilha Soares

Dependências principais:
    Django
    Pandas
    Celery
    Redis
    Disponível em requirements.txt

Outras Dependências:
    Redis Server: Como broker do Celery -> Para Windows disponível no .zip no projeto

Como rodar o projeto:
    - Instale as dependências
    - Rode o redis server
    - Rode o comando em um terminal separado: python -m celery -A myfilms worker -l info
    - Em outro terminal, no diretório myfilms/myfilms, rode: python manage.py runserver