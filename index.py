import requests
dict = {}
url = input("Url: ")
content = input("Content: ")
username = input("Username: ")
dict["content"] = content
dict["username"] = username
requests.post(url, dict)