import unittest
import os
import tempfile
import pytest
# Third party modules
import pytest
from modules import app


class TestUrls(unittest.TestCase):
    def test_homepage_response(client):
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_deprecated_page(client):
        response = app.test_client().get('/hello')
        assert response.status_code == 404

    def test_account_response_without_authentication(client):
        response = app.test_client().get('/account')
        assert response.status_code == 302

if __name__ == '__main__':
    unittest.main()