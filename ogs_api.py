import http.client as http_client
import requests
from dotenv import load_dotenv
import os
import socketio

load_dotenv()


http_client.HTTPConnection.debuglevel = 3


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
token_url = "https://online-go.com/oauth2/token/"


data = {
    "grant_type": "password",
    "username": username,
    "password": password,
    "client_id": client_id,
    "client_secret": client_secret,
}

response = requests.post(token_url, data=data)
response = response.json()
access_token = response["access_token"]


def get_user_id(username):
    response = requests.get(
        f"https://online-go.com/api/v1/players?username={username}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    response = response.json()
    return response["results"][0]["id"]


user_id = get_user_id(username)

response = requests.get(
    "https://online-go.com/api/v1",
    headers={"Authorization": f"Bearer {access_token}"},
)
response = response.json()
print(response)

sio = socketio.Client()
sio.connect("https://online-go.com/socket.io/?EIO=3&transport=websocket")
sio.emit(
    "connect/game", {"game_id": 60228080, "player_id": user_id, "auth": access_token}
)
