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


def parse_repo_info(repo_info):
    return {
        "name": repo_info["name"],
        "fullname": repo_info["full_name"],
        "url": repo_info["clone_url"]
    }


def get_user_repos(username: str) -> list:
    """Busca todos os repositórios do usuário na api do Github"""
    user_repos_url = settings.GITHUB_USER_REPOS_URL.format(username)
    response = get_content_from_url(user_repos_url)
    user_repos = [parse_repo_info(repo) for repo in response]

    return user_repos


def get_repo_information(repo_full_name: str) -> dict:
    """Busca todas as informações de um repositório na api do github"""
    user_repos_url = settings.GITHUB_REPO_INFO_URL.format(repo_full_name)
    response = get_content_from_url(user_repos_url)
    return parse_repo_info(response)
