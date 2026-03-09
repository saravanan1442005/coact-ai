import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')

url = f"{os.getenv('SUPABASE_URL')}/rest/v1/profiles?limit=1"
headers = {
    'apikey': os.getenv('SUPABASE_SERVICE_KEY'),
    'Authorization': f"Bearer {os.getenv('SUPABASE_SERVICE_KEY')}",
    'Content-Type': 'application/json'
}

print('Trying to read profiles to see if schema cache recovers...')
try:
    response = requests.get(url, headers=headers)
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')
except Exception as e:
    print(f'Error: {e}')
