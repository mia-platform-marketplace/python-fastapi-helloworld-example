import pytest
from fastapi.testclient import TestClient

from src.app import app
from src.schemas.header_schema import HeaderSchema


@pytest.fixture
def test_client():
    """
    This client can call the developed application
    """

    with TestClient(app) as client:
        client.headers = HeaderSchema().model_dump(by_alias=True)
        yield client
