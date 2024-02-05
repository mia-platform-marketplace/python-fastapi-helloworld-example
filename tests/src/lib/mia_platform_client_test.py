import json
import pytest
import httpretty
from fastapi import status

from src.schemas.header_schema import HeaderSchema
from src.lib.mia_platform_client import MiaPlatformClient
from src.utils.logger import get_logger


@pytest.fixture(name='headers')
def fixture_headers():
    header_schema = HeaderSchema()
    headers = header_schema.model_dump(by_alias=True)
    yield headers


@pytest.fixture(name='baseurl')
def fixture_baseurl():
    baseurl = 'http://www.dummy-url.com'
    yield baseurl


@pytest.fixture(name='mia_platform_client')
def fixture_mia_platform_client(headers):
    logger = get_logger()
    mia_platform_client = MiaPlatformClient(headers, logger)
    yield mia_platform_client


class TestMiaPlatformClient:
    """
    Test all functionalities of Mia Platform Client
    """

    # Headers

    def test_200_get_with_extra_headers(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Successfully make request with extra headers
        """

        path = 'resources'
        url = f'{baseurl}/{path}'
        body = [{'message': 'Hi :)'}]
        extra_headers = {
            'x-dummy': 'test',
            'x-custom': '123'
        }
        expected_headers = {
            **headers,
            **extra_headers
        }

        mock_server.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        response = mia_platform_client.get(
            url,
            headers=extra_headers
        )

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET
        assert response.request.headers.items() >= expected_headers.items()

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    # Get

    def test_200_get(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Sucessfully retrive the resources from the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}'
        body = [{'message': 'Hi :)'}]

        mock_server.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        response = mia_platform_client.get(url)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET
        assert response.request.headers.items() >= headers.items()

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    def test_500_get(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Error on retriving the resources from the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}'

        mock_server.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.get(url)

    # Get by id

    def test_200_get_by_id(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Sucessfully retrive the resource :id from the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'
        body = {'message': 'Hi :)'}

        mock_server.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        response = mia_platform_client.get_by_id(f'{baseurl}/{path}', _id)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET
        assert response.request.headers.items() >= headers.items()

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    def test_404_get_by_id(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Required resource :id no found in the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'

        mock_server.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_404_NOT_FOUND,
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET BY ID {url}"
                f" respond with status code {status.HTTP_404_NOT_FOUND}"
        ):
            mia_platform_client.get_by_id(f'{baseurl}/{path}', _id)

    def test_500_get_by_id(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Error on retriving the resource :id in the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'

        mock_server.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET BY ID {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.get_by_id(f'{baseurl}/{path}', _id)

    # Count

    def test_200_count(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Sucessfully count the resources in the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}/count'
        body = 0

        mock_server.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        response = mia_platform_client.count(f'{baseurl}/{path}')

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET
        assert response.request.headers.items() >= headers.items()

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    def test_500_count(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Error on counting the resources in the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}/count'
        body = 0

        mock_server.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            body=body
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient COUNT {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.count(f'{baseurl}/{path}')

    # Post

    def test_201_post(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Sucessfully create the resource in the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}'
        body = {'key': 'value'}

        mock_server.register_uri(
            method=httpretty.POST,
            uri=url,
            status=status.HTTP_201_CREATED,
            body=json.dumps(body)
        )

        response = mia_platform_client.post(url, data=body)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.POST
        assert response.request.headers.items() >= headers.items()

        # Response
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == body

    def test_500_post(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Error on creating the resource in the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}'
        body = {'key': 'value'}

        mock_server.register_uri(
            method=httpretty.POST,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            body=json.dumps(body)
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient POST {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.post(url, data=body)

    # Put

    def test_201_put(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Sucessfully create the resource in the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}'
        body = {'key': 'value'}

        mock_server.register_uri(
            method=httpretty.PUT,
            uri=url,
            status=status.HTTP_201_CREATED,
            body=json.dumps(body)
        )

        response = mia_platform_client.put(url, data=body)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.PUT
        assert response.request.headers.items() >= headers.items()

        # Response
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == body

    def test_500_put(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Error on creating the resource in the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}'
        body = {'key': 'value'}

        mock_server.register_uri(
            method=httpretty.PUT,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            body=json.dumps(body)
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient PUT {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.put(url, json=body)

    # Patch

    def test_200_patch_by_id(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Sucessfully update the resource in the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'
        body = {'key': 'value'}

        mock_server.register_uri(
            method=httpretty.PATCH,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        response = mia_platform_client.patch(
            f'{baseurl}/{path}',
            _id,
            data=body
        )

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.PATCH
        assert response.request.headers.items() >= headers.items()

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    def test_404_patch_by_id(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Resource :id to update not found in the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'

        mock_server.register_uri(
            method=httpretty.PATCH,
            uri=url,
            status=status.HTTP_404_NOT_FOUND,
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient PATCH {url}"
                f" respond with status code {status.HTTP_404_NOT_FOUND}"
        ):
            mia_platform_client.patch(f'{baseurl}/{path}', _id)

    def test_500_patch_by_id(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Error on updating the resource :id in the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'

        mock_server.register_uri(
            method=httpretty.PATCH,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient PATCH {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.patch(f'{baseurl}/{path}', _id)

    # Delete

    def test_204_delete(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Sucessfully delete the resources from collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}'

        mock_server.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_204_NO_CONTENT,
        )

        response = mia_platform_client.delete(url)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.DELETE
        assert response.request.headers.items() >= headers.items()

        # Response
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_500_delete(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Error on deleting the resources from the collection
        """

        path = 'resources'
        url = f'{baseurl}/{path}'

        mock_server.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient DELETE {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.delete(url)

    # Delete by id

    def test_204_delete_by_id(
        self,
        headers,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Sucessfully delete the resource :id from the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'

        mock_server.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_204_NO_CONTENT,
        )

        response = mia_platform_client.delete_by_id(f'{baseurl}/{path}', _id)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.DELETE
        assert response.request.headers.items() >= headers.items()

        # Response
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_404_delete_by_id(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Resource :id to delete not found in the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'

        mock_server.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_404_NOT_FOUND,
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient DELETE BY ID {url}"
                f" respond with status code {status.HTTP_404_NOT_FOUND}"
        ):
            mia_platform_client.delete_by_id(f'{baseurl}/{path}', _id)

    def test_500_delete_by_id(
        self,
        baseurl,
        mock_server,
        mia_platform_client
    ):
        """
        Error on deleting the resource :id from the collection
        """

        _id = 1
        path = 'resources'
        url = f'{baseurl}/{path}/{_id}'

        mock_server.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient DELETE BY ID {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.delete_by_id(f'{baseurl}/{path}', _id)
