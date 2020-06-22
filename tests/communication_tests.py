import json
import os
import pathlib
import unittest
from unittest import mock

from communication import get_user_repos, get_repo_information

CURRENT_PATH = pathlib.Path(__file__).parent.absolute()

def get_json(filename):
    with open(os.path.join(CURRENT_PATH, 'data', filename)) as ofile:
        return json.loads(ofile.read())


def user_repos_mock():
    return get_json('user.json')


def single_repo_mock():
    return get_json('repo.json')


class TestGithubParsers(unittest.TestCase):
    @mock.patch('communication.get_content_from_url', return_value=user_repos_mock())
    def test_parse_user_info(self, repo_info):
        expected_return = {
            "name": "testrepo",
            "url": "https://github.com/testcase/testrepo.git",
            "fullname": "testcase/testrepo"
        }
        self.assertEqual(expected_return, get_user_repos("testcase")[0])

    @mock.patch('communication.get_content_from_url', return_value=single_repo_mock())
    def test_parse_repo_info(self, repo_info):
        expected_return = {
            "name": "testrepo",
            "url": "https://github.com/testcase/testrepo.git",
            "fullname": "testcase/testrepo"
        }
        self.assertEqual(expected_return, get_repo_information("testcase/testrepo"))
