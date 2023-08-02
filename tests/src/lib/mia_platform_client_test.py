import json
import pytest
import httpretty
from fastapi import status

from src.utils.logger_conf import logger
from src.schemas.header_schema import HeaderSchema
from src.lib.mia_platform_client import MiaPlatformClient


@pytest.fixture(name='baseurl')
def fixture_baseurl():
    baseurl = 'http://www.dummy-url.com'
    yield baseurl


@pytest.fixture(name='mia_platform_client')
def fixture_mia_platform_client():
    mia_platform_client = MiaPlatformClient(
        HeaderSchema().dict(),
        logger
    )
    yield mia_platform_client


class TestMiaPlatformClient:
    """
    Test all functionalities of Mia Platform Client
    """

    # Get

    def test_200_get(self, baseurl, mock_server, mia_platform_client):
        """
        Sucessfully retrive the resources from the collection
        """

        path = '/resource'
        url = f'{baseurl}{path}'
        body = [{'message': 'Hi :)'}]

        mock_server.set_baseurl(baseurl)
        mock_server.register_uri(
            method=httpretty.GET,
            uri=path,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        response = mia_platform_client.get(url)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    def test_500_get(self, baseurl, mock_server, mia_platform_client):
        """
        Error on retriving the resources from the collection
        """

        path = '/resource'
        url = f'{baseurl}{path}'

        mock_server.set_baseurl(baseurl)
        mock_server.register_uri(
            method=httpretty.GET,
            uri=path,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.get(url)

    # Get by id

    def test_200_get_by_id(self, baseurl, mock_server, mia_platform_client):
        """
        Sucessfully retrive the resource :id from the collection
        """

        _id = 1
        path = f'/resource'
        url = f'{baseurl}{path}'
        body = {'message': 'Hi :)'}

        mock_server.set_baseurl(baseurl)
        mock_server.register_uri(
            method=httpretty.GET,
            uri=path,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        response = mia_platform_client.get_by_id(url, _id)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    # def test_404_get_by_id(self, mock_server):
    #     """
    #     Required resource :id no found in the collection
    #     """

    #     baseurl, _ = mock_server

    #     _id = 1
    #     url = f'{baseurl}/{_id}/'

    #     httpretty.register_uri(
    #         method=httpretty.GET,
    #         uri=url,
    #         status=status.HTTP_404_NOT_FOUND,
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient GET BY ID {url}"
    #             f" respond with status code {status.HTTP_404_NOT_FOUND}"
    #     ):
    #         mia_platform_client.get_by_id(baseurl, _id)

    # def test_500_get_by_id(self, mock_server):
    #     """
    #     Error on retriving the resource :id in the collection
    #     """

    #     baseurl, _ = mock_server

    #     _id = 1
    #     url = f'{baseurl}/{_id}/'

    #     httpretty.register_uri(
    #         method=httpretty.GET,
    #         uri=url,
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient GET BY ID {url}"
    #             f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
    #     ):
    #         mia_platform_client.get_by_id(baseurl, _id)

    # # Count

    # def test_200_count(self, mock_server):
    #     """
    #     Sucessfully count the resources in the collection
    #     """

    #     baseurl, required_headers = mock_server

    #     url = f'{baseurl}/count/'
    #     body = '0'

    #     httpretty.register_uri(
    #         method=httpretty.GET,
    #         uri=url,
    #         status=status.HTTP_200_OK,
    #         body=json.dumps(body)
    #     )

    #     mia_platform_client = MiaPlatformClient()
    #     response = mia_platform_client.count(baseurl)

    #     # Request
    #     assert response.request.url == url
    #     assert response.request.method == httpretty.GET

    #     # Response
    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.json() == body

    #     self.validate_sent_headers(required_headers, response)

    # def test_500_count(self, mock_server):
    #     """
    #     Error on counting the resources in the collection
    #     """

    #     baseurl, _ = mock_server

    #     url = f'{baseurl}/count/'
    #     body = '0'

    #     httpretty.register_uri(
    #         method=httpretty.GET,
    #         uri=url,
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         body=body
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient COUNT {url}"
    #             f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
    #     ):
    #         mia_platform_client.count(baseurl)

    # # Post

    # def test_201_post(self, mock_server):
    #     """
    #     Sucessfully create the resource in the collection
    #     """

    #     baseurl, required_headers = mock_server

    #     url = f'{baseurl}/'
    #     body = {'key': 'value'}

    #     httpretty.register_uri(
    #         method=httpretty.POST,
    #         uri=url,
    #         status=status.HTTP_201_CREATED,
    #         body=json.dumps(body)
    #     )

    #     mia_platform_client = MiaPlatformClient()
    #     response = mia_platform_client.post(baseurl, data=body)

    #     # Request
    #     assert response.request.url == url
    #     assert response.request.method == httpretty.POST

    #     # Response
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert response.json() == body

    #     self.validate_sent_headers(required_headers, response)

    # def test_500_post(self, mock_server):
    #     """
    #     Error on creating the resource in the collection
    #     """

    #     baseurl, _ = mock_server

    #     url = f'{baseurl}/'
    #     body = {'key': 'value'}

    #     httpretty.register_uri(
    #         method=httpretty.POST,
    #         uri=url,
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         body=json.dumps(body)
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient POST {url}"
    #             f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
    #     ):
    #         mia_platform_client.post(url, data=body)

    # # Put

    # def test_200_put(self, mock_server):
    #     """
    #     Sucessfully overwrite the resouce in the collection
    #     """

    #     baseurl, required_headers = mock_server

    #     url = f'{baseurl}/'
    #     body = {'key': 'value'}

    #     httpretty.register_uri(
    #         method=httpretty.PUT,
    #         uri=url,
    #         status=status.HTTP_200_OK,
    #         body=json.dumps(body)
    #     )

    #     mia_platform_client = MiaPlatformClient()
    #     response = mia_platform_client.put(baseurl, data=body)

    #     # Request
    #     assert response.request.url == url
    #     assert response.request.method == httpretty.PUT

    #     # Response
    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.json() == body

    #     self.validate_sent_headers(required_headers, response)

    # def test_201_put(self, mock_server):
    #     """
    #     Sucessfully create the resource in the collection
    #     """

    #     baseurl, required_headers = mock_server

    #     url = f'{baseurl}/'
    #     body = {'key': 'value'}

    #     httpretty.register_uri(
    #         method=httpretty.PUT,
    #         uri=url,
    #         status=status.HTTP_201_CREATED,
    #         body=json.dumps(body)
    #     )

    #     mia_platform_client = MiaPlatformClient()
    #     response = mia_platform_client.put(baseurl, data=body)

    #     # Request
    #     assert response.request.url == url
    #     assert response.request.method == httpretty.PUT

    #     # Response
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert response.json() == body

    #     self.validate_sent_headers(required_headers, response)

    # def test_500_put(self, mock_server):
    #     """
    #     Error on creating / overwriting the resource in the collection
    #     """

    #     baseurl, _ = mock_server

    #     url = f'{baseurl}/'
    #     body = {'key': 'value'}

    #     httpretty.register_uri(
    #         method=httpretty.PUT,
    #         uri=url,
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         body=json.dumps(body)
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient PUT {url}"
    #             f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
    #     ):
    #         mia_platform_client.put(url, json=body)

    # # Patch

    # def test_200_patch_by_id(self, mock_server):
    #     """
    #     Sucessfully update the resource in the collection
    #     """

    #     baseurl, required_headers = mock_server

    #     _id = 1
    #     url = f'{baseurl}/{_id}/'
    #     body = {'key': 'value'}

    #     httpretty.register_uri(
    #         method=httpretty.PATCH,
    #         uri=url,
    #         status=status.HTTP_200_OK,
    #         body=json.dumps(body)
    #     )

    #     mia_platform_client = MiaPlatformClient()
    #     response = mia_platform_client.patch(baseurl, _id, data=body)

    #     # Request
    #     assert response.request.url == url
    #     assert response.request.method == httpretty.PATCH

    #     # Response
    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.json() == body

    #     self.validate_sent_headers(required_headers, response)

    # def test_404_patch_by_id(self, mock_server):
    #     """
    #     Resource :id to update not found in the collection
    #     """

    #     baseurl, _ = mock_server

    #     _id = 1
    #     url = f'{baseurl}/{_id}/'

    #     httpretty.register_uri(
    #         method=httpretty.PATCH,
    #         uri=url,
    #         status=status.HTTP_404_NOT_FOUND,
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient PATCH {url}"
    #             f" respond with status code {status.HTTP_404_NOT_FOUND}"
    #     ):
    #         mia_platform_client.patch(baseurl, _id)

    # def test_500_patch_by_id(self, mock_server):
    #     """
    #     Error on updating the resource :id in the collection
    #     """

    #     baseurl, _ = mock_server

    #     _id = 1
    #     url = f'{baseurl}/{_id}/'

    #     httpretty.register_uri(
    #         method=httpretty.PATCH,
    #         uri=url,
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient PATCH {url}"
    #             f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
    #     ):
    #         mia_platform_client.patch(baseurl, _id)

    # # Delete

    # def test_204_delete(self, mock_server):
    #     """
    #     Sucessfully delete the resources from collection
    #     """

    #     baseurl, required_headers = mock_server

    #     url = f'{baseurl}/'

    #     httpretty.register_uri(
    #         method=httpretty.DELETE,
    #         uri=url,
    #         status=status.HTTP_204_NO_CONTENT,
    #     )

    #     mia_platform_client = MiaPlatformClient()
    #     response = mia_platform_client.delete(url)

    #     # Request
    #     assert response.request.url == url
    #     assert response.request.method == httpretty.DELETE

    #     # Response
    #     assert response.status_code == status.HTTP_204_NO_CONTENT

    #     self.validate_sent_headers(required_headers, response)

    # def test_500_delete(self, mock_server):
    #     """
    #     Error on deleting the resources from the collection
    #     """

    #     baseurl, _ = mock_server

    #     url = f'{baseurl}/'

    #     httpretty.register_uri(
    #         method=httpretty.DELETE,
    #         uri=url,
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient DELETE {url}"
    #             f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
    #     ):
    #         mia_platform_client.delete(url)

    # # Delete by id

    # def test_204_delete_by_id(self, mock_server):
    #     """
    #     Sucessfully delete the resource :id from the collection
    #     """

    #     baseurl, required_headers = mock_server

    #     _id = 1
    #     url = f'{baseurl}/{_id}/'

    #     httpretty.register_uri(
    #         method=httpretty.DELETE,
    #         uri=url,
    #         status=status.HTTP_204_NO_CONTENT,
    #     )

    #     mia_platform_client = MiaPlatformClient()
    #     response = mia_platform_client.delete_by_id(baseurl, _id)

    #     # Request
    #     assert response.request.url == url
    #     assert response.request.method == httpretty.DELETE

    #     # Response
    #     assert response.status_code == status.HTTP_204_NO_CONTENT

    #     self.validate_sent_headers(required_headers, response)

    # def test_404_delete_by_id(self, mock_server):
    #     """
    #     Resource :id to delete not found in the collection
    #     """

    #     baseurl, _ = mock_server

    #     _id = 1
    #     url = f'{baseurl}/{_id}/'

    #     httpretty.register_uri(
    #         method=httpretty.DELETE,
    #         uri=url,
    #         status=status.HTTP_404_NOT_FOUND,
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient DELETE BY ID {url}"
    #             f" respond with status code {status.HTTP_404_NOT_FOUND}"
    #     ):
    #         mia_platform_client.delete_by_id(baseurl, _id)

    # def test_500_delete_by_id(self, mock_server):
    #     """
    #     Error on deleting the resource :id from the collection
    #     """

    #     baseurl, _ = mock_server

    #     _id = 1
    #     url = f'{baseurl}/{_id}/'

    #     httpretty.register_uri(
    #         method=httpretty.DELETE,
    #         uri=url,
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #     )

    #     mia_platform_client = MiaPlatformClient()

    #     with pytest.raises(
    #         Exception,
    #         match=f"Error - MiaPlatformClient DELETE BY ID {url}"
    #             f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
    #     ):
    #         mia_platform_client.delete_by_id(baseurl, _id)
