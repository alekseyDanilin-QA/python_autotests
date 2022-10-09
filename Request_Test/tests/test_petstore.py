import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/404')
    assert response.status_code == 200

def test_1():
    response = requests.get('https://petstore.swagger.io/v2/pet/404')
    assert response.json()['name'] == 'pikachu'

def tests_2():
    response = requests.get('https://petstore.swagger.io/v2/store/order/9')
    assert response.json()['quantity'] == 1000