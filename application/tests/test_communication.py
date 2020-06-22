import unittest
from unittest import mock

from communication import get_user_repos, get_repo_information, InvalidJsonFormat
from tests.utils import user_repos_mock, single_repo_mock, invalid_json_mock


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

    @mock.patch('communication.get_content_from_url', return_value=invalid_json_mock())
    def test_parse_repo_invalid_json(self, repo_info):
        self.assertRaises(InvalidJsonFormat, get_repo_information, "testcase/testrepo")
