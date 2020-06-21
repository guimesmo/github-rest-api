import requests
import settings
import json


class RequestError(Exception):
    """Excessão genérica para erros de requisição"""
    pass


def get_content_from_url(url: str) -> json:
    """Função simplificada busca conteúdo da URL. Em caso de falha retorna exceção"""
    response = requests.get(url)
    if response.status_code != 200:
        raise RequestError
    return response.json()


def get_user_repos(username: str) -> list:
    """Busca todos os repositórios do usuário na api do Github"""
    user_repos_url = settings.GITHUB_USER_REPOS_URL.format(username)
    return get_content_from_url(user_repos_url)


def get_repo_information(repo_full_name: str) -> dict:
    """Busca todas as informações de um repositório na api do github"""
    user_repos_url = settings.GITHUB_REPO_INFO_URL.format(repo_full_name)
    return get_content_from_url(user_repos_url)
