import json
import os
import pathlib


CURRENT_PATH = pathlib.Path(__file__).parent.absolute()


class RequestMock:
    status_code = 200
    content = '{}'

    def json(self):
        return {}


def get_json(filename):
    with open(os.path.join(CURRENT_PATH, 'data', filename)) as ofile:
        return json.loads(ofile.read())


def user_repos_mock():
    return get_json('user.json')


def single_repo_mock():
    return get_json('repo.json')


def invalid_json_mock():
    return {"invalid": "format"}


def request_failed_mock():
    obj = RequestMock()
    obj.status_code = 404
    return obj
