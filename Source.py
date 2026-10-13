import os, requests
# Import the load_dotenv function from the python-dotenv library to read the ShunyaLabs API key and token from the .env file in the project folder,
# and add them to environment variables (os.environ). This is a best practice for managing sensitive credentials w/o hardcoding them into the code.
from dotenv import load_dotenv
# Load the environment variables from the .env file in the project folder
load_dotenv()
access_token = os.environ.get("ACCESS_TOKEN")
# Call the Shunya Labs API with the token
with open("Barkheda Medhatal Meeting.m4a", "rb") as f:
    r = requests.post(
        "https://asrv2prod.shunyalabs.ai/v1/audio/transcriptions",
        headers={"Authorization": f"Bearer {access_token}"},
        files={"file": f},
        data={"model": "zero-indic"},
    )
r.raise_for_status()
print(r.json())
print(r.json()["text"])
