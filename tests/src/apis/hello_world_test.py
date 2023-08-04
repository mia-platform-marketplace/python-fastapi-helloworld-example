def test_hello_world(test_client):
    """
    Test say Hello
    """

    response = test_client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
