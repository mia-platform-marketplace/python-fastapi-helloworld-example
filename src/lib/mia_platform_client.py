import os
import requests


class MiaPlatformAuth(requests.auth.AuthBase):
    """
    Attaches HTTP headers to the given request object for Mia Platform authentication.
        
    Args:
        headers (dict): A dictionary containing the headers to be attached to the request.
        logger: A logger object.
    """

    def __init__(self, headers, logger):
        self.headers_to_proxy = {}

        header_keys_to_proxy = os.environ.get(
            'HEADER_KEYS_TO_PROXY'
        ).split(',')

        for header_key in header_keys_to_proxy:
            try:
                self.headers_to_proxy[header_key] = headers[header_key]
            except KeyError:
                logger.debug(
                    f'The parameter "{header_key}" is missing from the request headers'
                )

    def __call__(self, request):
        for key, value in self.headers_to_proxy.items():
            request.headers[key] = value

        return request


class MiaPlatformClient():
    """
    Provides a simple interface to make HTTP requests within a Mia Platform application cluster.

    Args:
        headers (dict): A dictionary containing the headers to be used for authentication.
        logger: A logger object.
    """

    def __init__(self, headers, logger):
        self.session = requests.Session()
        self.session.auth = MiaPlatformAuth(headers, logger)
        self.logger = logger

    def get(self, url, **kwargs):
        self.logger.debug(f'Start - MiaPlatformClient GET {url}')

        response = self.session.get(url, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient GET {url}" \
                f" respond with status code {response.status_code}"
            self.logger.error(message)
            raise Exception(message)

        self.logger.debug(f'End - MiaPlatformClient GET {url}')

        return response

    def get_by_id(self, url, _id, **kwargs):
        self.logger.debug(f'Start - MiaPlatformClient GET BY ID {url}/{_id}')

        response = self.session.get(f'{url}/{_id}', **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient GET BY ID {url}/{_id}" \
                f" respond with status code {response.status_code}"
            self.logger.error(message)
            raise Exception(message)

        self.logger.debug(f'End - MiaPlatformClient GET BY ID {url}/{_id}')

        return response

    def count(self, url, **kwargs):
        self.logger.debug(f'Start - MiaPlatformClient COUNT {url}')

        response = self.session.get(f'{url}/count', **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient COUNT {url}/count" \
                f" respond with status code {response.status_code}"
            self.logger.error(message)
            raise Exception(message)

        self.logger.debug(f'End - MiaPlatformClient GET BY ID {url}')

        return response

    def post(self, url, data=None, **kwargs):
        self.logger.debug(f'Start - MiaPlatformClient POST {url}')

        response = self.session.post(url, data, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient POST {url}" \
                f" respond with status code {response.status_code}"
            self.logger.error(message)
            raise Exception(message)

        self.logger.debug(f'End - MiaPlatformClient POST {url}')

        return response

    def put(self, url, data=None, **kwargs):
        self.logger.debug(f'Start - MiaPlatformClient PUT {url}')

        response = self.session.put(url, data, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient PUT {url}" \
                f" respond with status code {response.status_code}"
            self.logger.error(message)
            raise Exception(message)

        self.logger.debug(f'End - MiaPlatformClient PUT {url}')

        return response

    def patch(self, url, _id, data=None, **kwargs):
        self.logger.debug(f'Start - MiaPlatformClient PATCH {url}/{_id}')

        response = self.session.patch(f'{url}/{_id}', data, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient PATCH {url}/{_id}" \
                f" respond with status code {response.status_code}"
            self.logger.error(message)
            raise Exception(message)

        self.logger.debug(f'End - MiaPlatformClient PATCH {url}/{_id}')

        return response

    def delete(self, url, **kwargs):
        self.logger.debug(f'Start - MiaPlatformClient DELETE {url}')

        response = self.session.delete(url, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient DELETE {url}" \
                f" respond with status code {response.status_code}"
            self.logger.error(message)
            raise Exception(message)

        self.logger.debug(f'End - MiaPlatformClient DELETE {url}')

        return response

    def delete_by_id(self, url, _id, **kwargs):
        self.logger.debug(
            f'Start - MiaPlatformClient DELETE BY ID {url}/{_id}')

        response = self.session.delete(f'{url}/{_id}', **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient DELETE BY ID {url}/{_id}" \
                f" respond with status code {response.status_code}"
            self.logger.error(message)
            raise Exception(message)

        self.logger.debug(
            f'End - MiaPlatformClient DELETE BY ID {url}/{_id}')

        return response
