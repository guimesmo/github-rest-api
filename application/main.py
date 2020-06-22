import communication

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


class Home(Resource):
    def get(self):
        """Lista os endpoints disponíveis"""
        endpoints = {
            "user": "/api/<username>",
            "repo": "/api/<username>/<repo_name>",

        }
        return endpoints


class UserInfo(Resource):
    def get(self, username):
        try:
            return communication.get_user_repos(username)
        except communication.RequestError:
            return {"message": "Falha na busca do usuário"}, 400
        except communication.InvalidJsonFormat:
            return {"message": "Problema no formato da resposta. Tente novamente"}, 400


class RepoInfo(Resource):
    def get(self, username, repo_name):
        """
        Busca as informações do repositório. O nome do repositório começa
        com o nome de usuário em seguida o nome da aplicação
        """
        repo_fullname = f"{username}/{repo_name}"
        try:
            return communication.get_repo_information(repo_fullname)
        except communication.RequestError:
            return {"message": "Falha na busca do repositório."}, 400
        except communication.InvalidJsonFormat:
            return {"message": "Problema no formato da resposta. Tente novamente"}, 400


api.add_resource(Home, '/')
api.add_resource(UserInfo, '/api/<username>')
api.add_resource(RepoInfo, '/api/<username>/<repo_name>')
