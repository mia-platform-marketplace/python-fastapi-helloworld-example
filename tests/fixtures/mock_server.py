import os
import pytest
import httpretty
from dotenv import load_dotenv

# from src.apis.schemas.header_schema import HeaderRequest


class MockServer:
    """
    TODO: add description
    """

    def __init__(self):
        load_dotenv('default.env')

        # self.required_headers = HeaderRequest(
        #     LOG_LEVEL=os.environ.get('LOG_LEVEL'),
        #     USERID_HEADER_KEY=os.environ.get('USERID_HEADER_KEY'),
        #     GROUPS_HEADER_KEY=os.environ.get('GROUPS_HEADER_KEY'),
        #     CLIENTTYPE_HEADER_KEY=os.environ.get('CLIENTTYPE_HEADER_KEY'),
        #     BACKOFFICE_HEADER_KEY=os.environ.get('BACKOFFICE_HEADER_KEY'),
        #     MICROSERVICE_GATEWAY_SERVICE_NAME=os.environ.get(
        #         'MICROSERVICE_GATEWAY_SERVICE_NAME'),
        # ).__dict__.items()
        self.baseurl = None

    def enable(self):
        httpretty.enable(verbose=True, allow_net_connect=False)

    def disable(self):
        httpretty.reset()
        httpretty.disable()

    def set_required_headers(self, required_headers):
        self.required_headers = required_headers

    def get_required_headers(self):
        return self.required_headers

    def set_baseurl(self, baseurl):
        self.baseurl = baseurl

    def get_baseurl(self):
        return self.baseurl

    # pylint: disable=R0913
    def register_uri(
        self,
        method,
        uri,
        body='{"message": "HTTPretty :)"}',
        adding_headers=None,
        forcing_headers=None,
        status=200,
        responses=None,
        match_querystring=False,
        priority=0,
        **headers
    ):
        if self.baseurl is None:
            raise Exception('baseurl is not set')

        httpretty.register_uri(
            method,
            f'{self.baseurl}' if not uri else f'{self.baseurl}{uri}',
            body,
            adding_headers,
            forcing_headers,
            status,
            responses,
            match_querystring,
            priority,
            **headers
        )


@pytest.fixture
def mock_server():
    """
    This server is a utility that can be used to run a simple mock of an external service
    """

    mock_server = MockServer()
    mock_server.enable()

    yield mock_server

    mock_server.disable()
