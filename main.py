import communication

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def home():
    """Lista os endpoints disponíveis"""
    endpoints = {
        "user": "/api/<username>",
        "repo": "/api/<repo_fullname>",

    }
    return jsonify(endpoints)


@app.route('/api/<username>')
def username_info(username):
    try:
        info = communication.get_user_repos(username)
    except communication.RequestError:
        return "Falha na busca do usuário", 400
    return jsonify(info)


@app.route('/api/<username>/<repo_prefix>')
@app.route('/api/<username>/<repo_prefix>/<repo_name>')
def repo_info(username, repo_prefix, repo_name=None):
    """
    Busca as informações do repositório. O nome do repositório começa
    com o nome de usuário em seguida pode haver variação no número de parâmetros
    """
    repo_fullname = "/".join([n for n in (username, repo_prefix, repo_name,) if n])
    try:
        repo_info = communication.get_repo_information(repo_fullname)
    except communication.RequestError:
        return "Falha na busca do repositório", 400
    return jsonify(repo_info)
