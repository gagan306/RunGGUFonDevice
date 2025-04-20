import requests

res = requests.post("http://localhost:8000/chat", json={
    "prompt": "Tell me a fun fact about space.",
    "max_tokens": 50
})
print(res.json())
