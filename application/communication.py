import requests
import json
import logging
import settings

logger = logging.getLogger()

class RequestError(Exception):
    """Excessão genérica para erros de requisição"""
    pass


class InvalidJsonFormat(Exception):
    """Excessão para mudança no formato ou erro do json"""
    pass


def get_content_from_url(url: str) -> json:
    """Função simplificada busca conteúdo da URL. Em caso de falha retorna exceção"""
    response = requests.get(url)
    logger.info(f'[GET_CONTENT_FROM_URL] {url}')
    if response.status_code != 200:
        logger.info(f'[GET_CONTENT_FROM_URL] STATUS ERR: {response.status_code}')
        raise RequestError
    logger.info('[GET_CONTENT_FROM_URL] SUCCESS')
    return response.json()


def parse_repo_info(repo_info: dict) -> dict:
    try:
        return {
            "name": repo_info["name"],
            "fullname": repo_info["full_name"],
            "url": repo_info["clone_url"]
        }
    except KeyError:
        raise InvalidJsonFormat


def get_user_repos(username: str) -> list:
    """Busca todos os repositórios do usuário na api do Github"""
    user_repos_url = settings.GITHUB_USER_REPOS_URL.format(username)

    logger.info(f'[GET_USER_REPOS] target: {user_repos_url}')
    response = get_content_from_url(user_repos_url)
    user_repos = [parse_repo_info(repo) for repo in response]

    return user_repos


def get_repo_information(repo_full_name: str) -> dict:
    """Busca todas as informações de um repositório na api do github"""
    repo_url = settings.GITHUB_REPO_INFO_URL.format(repo_full_name)
    response = get_content_from_url(repo_url)
    return parse_repo_info(response)
