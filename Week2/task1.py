import requests


# GET-запит

get_url = "https://jsonplaceholder.typicode.com/posts/1"

get_response = requests.get(get_url)

print("GET-запит")
print("Статус-код:", get_response.status_code)
print("\nЗаголовки відповіді:")
print(get_response.headers)
print("\nТіло відповіді:")
print(get_response.text)


# POST-запит

post_url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Test post",
    "body": "This is a test message",
    "userId": 1
}

post_response = requests.post(post_url, json=data)

print("\n\nPOST-запит")
print("Статус-код:", post_response.status_code)
print("\nЗаголовки відповіді:")
print(post_response.headers)
print("\nТіло відповіді:")
print(post_response.text)
