import requests as req

uri = "http://localhost:8080/"

print("Adding new user...")
payload = {"name":"Roger Rabbit", "role":"comedy relief"}
r = req.post(uri+"employees", data = payload)
print(r.text)