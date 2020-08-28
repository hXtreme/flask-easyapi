#!/usr/bin/env python

"""
Test `flask_easyapi` package with `test_apps/greet`.
"""

import pytest

from flask.testing import Client
from .test_apps.greet import greet


@pytest.fixture
def client() -> Client:
    with greet.app.test_client() as client:
        return client


@pytest.fixture(params=["Hello", "Hey"])
def greeting(request):
    return request.param


@pytest.fixture(params=["Alice"])
def name(request):
    return request.param


@pytest.fixture(params=["Alex"])
def alt_name(request):
    return request.param


def common_test(client: Client):
    assert client.head("/").status_code == 404


def test_noop(client):
    assert True


def test_simple_greet(client: Client):
    """
    Test the ``/simple_greet`` endpoint.

    This is a sanity check to make sure we aren't breaking the
    usual working of Blueprints.

    :param client: Client to the flask app.
    """
    common_test(client)
    response = client.get("/simple_greet")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_greet_parameterized(client: Client, name: str):
    """
    Test the ``/greet_parameterized`` endpoint.

    Test to check if EasyAPI passes the ``name`` url parameter passed
    to the endpoint.

    :param client: Client to the flask app.
    :param name: Name of the person to greet.
    """
    common_test(client)
    response = client.get(f"/greet_parameterized?name={name}")
    assert response.status_code == 200
    assert response.data == f"Hello, {name}!".encode()


def test_custom_greet_parameterized(client: Client, greeting: str, name: str):
    """
    Test the ``/custom_greet_parameterized`` endpoint.

    Test to check if EasyAPI passes both the ``greeting`` and ``name`` url parameter
    correctly to the endpoint even when the order in url parameters is changed.

    :param client: Client to the flask app.
    :param greeting: Greeting to greet the person with.
    :param name: Name of the person to greet.
    """
    common_test(client)
    response_greeting_name = client.get(
        f"/custom_greet_parameterized?greeting={greeting}&name={name}"
    )
    assert response_greeting_name.status_code == 200
    assert response_greeting_name.data == f"{greeting}, {name}!".encode()

    # Change the order of name and greeting in url parameters.
    response_name_greeting = client.get(
        f"/custom_greet_parameterized?name={name}&greeting={greeting}"
    )
    assert response_name_greeting.status_code == 200
    assert response_name_greeting.data == f"{greeting}, {name}!".encode()
    assert response_greeting_name.data == response_name_greeting.data


def test_greet_name(client: Client, name: str, alt_name: str):
    """
    Test the ``/greet/<name>`` endpoint.

    Test to check if EasyAPI correctly passes the arguments recieved
    from the route.

    For the test we'll send a get request to ``/greet/<name>`` with url
    parameter: ``name=<alt_name>``. We expect EasyAPI to ignore ``alt_name``
    and pass ``name`` to the endpoint.

    :param client: Client to the flask app.
    :param name: Name of the person to greet.
    :param alt_name: Name of another person.
    """
    common_test(client)
    response = client.get(f"/greet/{name}?name={alt_name}")
    assert response.status_code == 200
    assert response.data == f"Hello, {name}!".encode()
