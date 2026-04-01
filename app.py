from flask import Flask, request
import requests
import random

app = Flask(__name__)

VK_TOKEN = "vk1.a.Q7LAE6dZjRNoMeFaD78C1_pprei0nxdaS0vSgpvkzqqCLyzawfkzdt_7AsaUI5CFZ"
CONFIRMATION_TOKEN = "123456"

def send_vk_message(user_id, text):
    url = "https://api.vk.com/method/messages.send"
    params = {
        "user_id": user_id,
        "message": text,
        "access_token": VK_TOKEN,
        "v": "5.199",
        "random_id": random.randint(1, 1000000000)
    }
    requests.post(url, params=params)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and data.get("type") == "confirmation":
        return CONFIRMATION_TOKEN
    if data and data.get("type") == "message_new":
        msg = data["object"]["message"]
        user_id = msg["from_id"]
        text = msg.get("text", "")
        send_vk_message(user_id, f"Вы написали: {text}")
        return "ok"
    return "ok"
