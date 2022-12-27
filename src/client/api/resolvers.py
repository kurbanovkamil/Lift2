import requests

def check_login(login: str, password: str):
    data = f'{{ "login": "{login}", "password": "{password}" }}'
    r = requests.post(f'http://127.0.0.1:5000/login', data=data)
    answer = r.json()
    print(answer)
    code = answer["code"]
    message = answer["message"]

    if code != 200:
        print(f"Server error:{message}")
        return None
    else:
        return answer["post"][0]

