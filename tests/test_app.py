import unittest

from modules import app


class TestUrls(unittest.TestCase):
    def test_homepage_response(self):
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_deprecated_page(self):
        response = app.test_client().get('/hello')
        assert response.status_code == 404

    def test_account_response_without_authentication(self):
        response = app.test_client().get('/account')
        assert response.status_code == 302
