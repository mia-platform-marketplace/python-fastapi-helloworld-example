import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def test_client():
    """
    This client can call the developed application
    """

    with TestClient(app) as test_client:
        test_client.headers = {
            'miauserid': 'miauserid',
            'miausergroups': 'miausergroups',
            'miaclienttype': 'miaclienttype',
            'client-type': 'client-type',
            'x-request-id': 'x-request-id'
        }
        yield test_client
