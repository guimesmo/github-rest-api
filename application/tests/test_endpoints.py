import unittest

from main import app
from unittest import mock

from tests.utils import user_repos_mock, single_repo_mock, request_failed_mock, invalid_json_mock


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    @mock.patch('communication.get_content_from_url', return_value=user_repos_mock())
    def test_user_repo_endpoint(self, repo_info):
        response = self.client.get('/api/testcase')
        self.assertEqual(200, response.status_code)

    @mock.patch('communication.get_content_from_url', return_value=user_repos_mock())
    def test_repo_endpoint_contenttype(self, repo_info):
        response = self.client.get('/api/testcase')
        self.assertEqual('application/json', response.content_type)

    @mock.patch('requests.get', return_value=request_failed_mock())
    def test_user_repos_raises_400_on_error(self, repo_info):
        response = self.client.get('/api/testcase')
        self.assertEqual(400, response.status_code)

    @mock.patch('communication.get_content_from_url', return_value=[invalid_json_mock()])
    def test_user_repos_raises_400_invalid_json_error(self, repo_info):
        response = self.client.get('/api/testcase')
        self.assertEqual(400, response.status_code)

    @mock.patch('communication.get_content_from_url', return_value=single_repo_mock())
    def test_single_repo_endpoint(self, repo_info):
        response = self.client.get('/api/testcase/testrepo')
        self.assertEqual(200, response.status_code)

    @mock.patch('requests.get', return_value=request_failed_mock())
    def test_single_repo_raises_400_on_error(self, repo_info):
        response = self.client.get('/api/testcase/testrepo')
        self.assertEqual(400, response.status_code)

    @mock.patch('communication.get_content_from_url', return_value=invalid_json_mock())
    def test_single_repo_raises_400_invalid_json_error(self, repo_info):
        response = self.client.get('/api/testcase/testrepo')
        self.assertEqual(400, response.status_code)

