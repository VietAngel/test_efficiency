import requests
from concurrent.futures import ThreadPoolExecutor

def login_admin(username, password):
    header = {
    }
    response = requests.post('http://localhost:5000/login-admin',headers=header, json={
        'username': str(username),
        'password': str(password),
    })
    print(response.content)
    token = str(response.content).split('"token":"')[1].split('"')[0]
    return token

with ThreadPoolExecutor(max_workers=100) as executor:
    # Khởi động các tác vụ sử dụng thread pool
    for i in range(100):
        executor.submit(login_admin, 'viet angel', 'Hoangviet305@')

