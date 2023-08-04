import pytest
import httpretty


class MockServer:
    """
    A simple mock server for testing purposes.
    """

    def enable(self):
        httpretty.enable(verbose=False, allow_net_connect=False)

    def disable(self):
        httpretty.reset()
        httpretty.disable()

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
        httpretty.register_uri(
            method,
            uri,
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
