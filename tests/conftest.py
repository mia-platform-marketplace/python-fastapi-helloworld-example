import os
import pytest
import httpretty
from dotenv import load_dotenv
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def client():
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


@pytest.fixture
def server():
    """
    This server can receive requests and mock the response
    """

    load_dotenv('default.env')

    baseurl = 'http://testserver'
    # require_headers = HeaderRequest(
    #     miauserid='miauserid',
    #     miausergroups='miausergroups',
    #     miaclienttype='miaclienttype',
    #     client_type='client-type',
    #     secret='secret',
    #     cookie='cookie',
    # ).__dict__.items()

    httpretty.enable(verbose=False, allow_net_connect=False)

    yield baseurl, require_headers

    httpretty.disable()
    httpretty.reset()
