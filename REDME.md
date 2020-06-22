## GITHUB REST API CLIENT

Esta aplicação simplifica a leitura de dados de um usuário ou repositório

### Instruções de execução

1 - Crie um virtualenv com Python 3.6 ou superior

2 - Ative o virtualenv

3 - Instale o requirements.txt

`pip install -r requirements.txt`

4 - Utilize o make. Os seguintes comandos estão disponíveis:

`make runserver` - servidor de produção com uwsgi

`make runlocal` - servidor padrão para teste local do flask

`make test` - execução dos testes com unnitest

`make coverage` - execução dos testes com coverage

### Docker
Você pode fazer a execução do projeto utilizando docker:

1 - Faça o build da imagem:

`docker build --tag restapi:0.1 .`

2 - Execute a imagem criada:
`docker run --publish 5000:5000 --rm --name restapi restapi:0.1`

A porta padrão de execução do projeto é a porta 5000
 
