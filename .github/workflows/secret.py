
import os

api_key = os.environ.get("API_KEY")

if api_key:
    print("API key loaded successfully!")
else:
    print("API key not found!")
