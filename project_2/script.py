import requests as rq

r = rq.get("http://www.example.com")
print(r.status_code)