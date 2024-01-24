import requests
import json

def send_message_to_flock(api_token, room_id, message):
    url = f"https://api.flock.com/hooks/sendMessage/{api_token}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "to": room_id,
        "text": message
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

# Replace these with your actual values
flock_api_token = "9218ceda-1e05-4402-a216-4a3ed1ef00be"
flock_room_id = "Bogdan Mileyko"
generated_password = "your_generated_password"

send_message_to_flock(flock_api_token, flock_room_id, generated_password)
