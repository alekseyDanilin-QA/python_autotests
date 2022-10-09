from http.client import OK
from urllib import response
import requests

response = requests.post("https://petstore.swagger.io/v2/pet",json={
  "id": 404,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "pikachu",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)
print(response.status_code)

response = requests.put("https://petstore.swagger.io/v2/pet",json={
  "id": 404,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "pikachu",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 405,
      "name": "string"
    }
  ],
  "status": "available"
})

print(response.text)
print(response.status_code)

response = requests.get("https://petstore.swagger.io/v2/pet/404")
print(response.text)
print(response.status_code)