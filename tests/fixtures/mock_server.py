import pytest
import httpretty
from dotenv import load_dotenv

from src.schemas.header_schema import HeaderSchema


class MockServer:
    """
    TODO: add description
    """

    def __init__(self):
        load_dotenv('default.env')

        self.required_headers = HeaderSchema().dict()
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

    server = MockServer()
    server.enable()

    yield server

    server.disable()
