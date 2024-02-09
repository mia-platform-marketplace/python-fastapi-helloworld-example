# Python FastAPI Hello World Microservice Example

[![Python
version](https://img.shields.io/badge/python-v3.10-blue)](.coverage/html/index.html)
[![FastAPI
version](https://img.shields.io/badge/fastapi-v0.100.1-blue)](.coverage/html/index.html)
[![Coverage](.badges/coverage-badge.svg)](.coverage/html/index.html)

---

## Local development

To develop the service locally you need:

- python 3.10

A virtual environment is a Python tool for dependency management and project
isolation. For further info about the creation and management of a virtual environment,
please check the [Python official documentation](https://docs.python.org/3/library/venv.html).
To create your virtual environment run the following command:

```shell
python -m venv /path/to/new/virtual/environment
```

To activate your virtual envirorment run the following command on
your terminal:

```shell
source /path/to/virtual/environment/bin/activate
```

When finished, to deactive the virtual envirorment run the following
command:

```shell
deactivate
```

Remember to put the path to the virtual environment in the `.gitignore` file.

During development, you will probably have to perform the same operations many
times: start the application locally, check the code quality, run tests and compute coverage. Therefore,
to avoid to remember each time the syntax of the commands to be executed, the
main commands were collected in a Makefile. [Makefile](https://www.gnu.org/software/make/manual/make.html) is a Unix automation tool that contains the recipe to build and run your program. So, listed below are the
commands that can be executed by the make command:

Install requirements and pre-commit:
```shell
make setup
```

Run application locally:
```shell
make start
```

Run linter:
```shell
make lint
```

Run tests:
```shell
make test
```

Compute the coverage:
```shell
make coverage
```

## Utilities

### MiaPlatformClient

The `MiaPlatformClient` class simplifies HTTP requests within a Mia Platform application cluster. It uses the requests library for common operations like `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` on resource URLs. Designed for the Mia Platform environment, it supports activity logging with a specified logger. The `MiaPlatformAuth` class extends `requests.auth.AuthBase`, enabling the addition of specified HTTP headers to requests via the `MiaPlatformClient` instance. These headers are extracted from the provided object for seamless header proxying. The `HEADER_KEYS_TO_PROXY` env variable facilitates specifying headers for forwarding, providing customizable control over header forwarding behavior to suit individual needs.

These examples show how to use the MiaPlatformClient lib.

Usage example in a generic function:

```python
from src.utils.logger import get_logger

def dummy():
    # Define headers for authentication
    headers = {
      'key': 'value'
    }

    logger = get_logger()

    # Create a MiaPlatformClient instance with the defined headers and imported logger
    mia_platform_client = MiaPlatformClient(headers, logger)
```

Usage example within an endpoint handler:

```python
@router.get("/")
def dummy(request: Request):
    # Get the Mia Platform client instance from the request's state
    mia_platform_client = request.state.mia_platform_client

    # Make a standard request using the Mia Platform client
    response = mia_platform_client.get(url)

    # Alternatively, make a request with extra headers
    response = mia_platform_client.get(url, headers)

    # Return the JSON content of the response
    return response.json()
```

### MockServer

`MockServer` is a purpose-built utility to effortlessly emulate external services, enhancing testing efficiency. It creates mock servers to replicate real-world behavior, simplifying the simulation of external services. Managed by the mocking library HTTPretty, it allows the registration of preset URIs linked to specific HTTP methods and their expected responses. As a pytest fixture named `mock_server`, this tool facilitates smooth test execution.

The following example show how to use the MockServer test utility.

```python
# Note: we are using the mock_server fixture, which automatically creates an instance of the MockServer class and enables/disables the server as needed

def dummy(
    baseurl,
    mock_server,
    mia_platform_client
):
    # Define the resource path
    path = 'resources'
    
    # Construct the complete URL
    url = f'{baseurl}/{path}'
    
    # Prepare a sample response body
    body = [{'message': 'Hi :)'}]

    # Register a new mock endpoint
    mock_server.register_uri(
        method=httpretty.GET,
        uri=url,
        status=status.HTTP_200_OK,
        body=json.dumps(body)
    )

    # Make a request using the Mia Platform client
    response = mia_platform_client.get(url)

    # Assertions
    # ...
```

---

## DevOps console

This walkthrough will explain you how to correctly create a microservice in Python that uses FastAPI framework to return an hello message from the DevOps Console.

### Create a microservice

In order to do so, access to [Mia-Platform DevOps Console](https://console.cloud.mia-platform.eu/login), create a new project and go to the **Design** area.

From the Design area of your project select _Microservices_ and then create a new one, you have now reached [Mia-Platform Marketplace](https://docs.mia-platform.eu/development_suite/api-console/api-design/marketplace/)!
In the marketplace you will see a set of Examples and Templates that can be used to set-up microservices with a predefined and tested function.

For this walkthrough select the following template: **Python FastAPI**.
Give your microservice the name you prefer, in this walkthrough we'll refer to it with the following name: **python-hello-fastapi**. Then, fill the other required fields and confirm that you want to create a microservice.  
A more detailed description on how to create a Microservice can be found in [Microservice from template - Get started](https://docs.mia-platform.eu/development_suite/api-console/api-design/custom_microservice_get_started/#2-service-creation) section of Mia-Platform documentation.

### Expose an endpoint to your microservice

In order to access to your new microservice it is necessary to create an endpoint that targets it.  
In particular, in this walkthrough you will create an endpoint to your microservice *python-hello-fastapi*. To do so, from the Design area of your project select _Endpoints_ and then create a new endpoint.
Now you need to choose a path for your endpoint and to connect this endpoint to your microservice. Give to your endpoint the following path: **/fastapi-greetings**. Then, specify that you want to connect your endpoint to a microservice and, finally, select *python-hello-fastapi*.  
Step 3 of [Microservice from template - Get started](https://docs.mia-platform.eu/development_suite/api-console/api-design/custom_microservice_get_started/#3-creating-the-endpoint) section of Mia-Platform documentation will explain in detail how to create an endpoint from the DevOps Console.

### Save your changes

After having created an endpoint to your microservice you should save the changes that you have done to your project in the DevOps console.  
Remember to choose a meaningful title for your commit (e.g 'created service python_hello_fastapi'). After some seconds you will be prompted with a popup message which confirms that you have successfully saved all your changes.  
Step 4 of [Microservice from template - Get started](https://docs.mia-platform.eu/development_suite/api-console/api-design/custom_microservice_get_started/#4-save-the-project) section of Mia-Platform documentation will explain how to correctly save the changes you have made on your project in the DevOps console.

### Deploy

Once all the changes that you have made are saved, you should deploy your project through the DevOps Console. Go to the **Deploy** area of the DevOps Console.  
Once here select the environment and the branch you have worked on and confirm your choices clicking on the *deploy* button. When the deploy process is finished you will receveive a pop-up message that will inform you.  
Step 5 of [Microservice from template - Get started](https://docs.mia-platform.eu/development_suite/api-console/api-design/custom_microservice_get_started/#5-deploy-the-project-through-the-api-console) section of Mia-Platform documentation will explain in detail how to correctly deploy your project.

### Try it

Now, if you launch the following command on your terminal (remember to replace `<YOUR_PROJECT_HOST>` with the real host of your project):

```shell
curl <YOUR_PROJECT_HOST>/fastapi-greetings/hello
```

you should see the following message:

```json
{ "message": "Hello World!" }
```

Congratulations! You have successfully learnt how to use our Python FastAPI _Hello World_ Example on the DevOps Console!