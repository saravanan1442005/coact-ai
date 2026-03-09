import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')

url = f"{os.getenv('SUPABASE_URL')}/rest/v1/practice_history"
headers = {
    'apikey': os.getenv('SUPABASE_SERVICE_KEY'),
    'Authorization': f"Bearer {os.getenv('SUPABASE_SERVICE_KEY')}",
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}
data = {
    'session_id': 'test-session-999',
    'user_id': '00000000-0000-0000-0000-000000000000',
    'scenario_type': 'custom',
    'session_mode': 'skill_assessment',
    'title': 'Test Title',
    'ai_character': 'alex',
    'mode': 'coaching',
    'role': 'manager',
    'ai_role': 'employee',
    'scenario': 'test scenario',
    'framework': ['GROW'],
    'transcript': {'_compressed': 'eJyrVkrLzE1VsjI0M1XSUUqtKMEsLilNLlGwUkpMSC1WyilNS87PLcjPz01VqgUAUvwMgg=='},
    'report_data': {},
    'completed': False,
    'created_at': '2026-03-09T10:00:00.000000'
}

print('Sending request...')
try:
    response = requests.post(url, headers=headers, json=data)
    print(f'Status Code: {response.status_code}')
    print(f'Response Body: {response.text}')
except Exception as e:
    print(f"Error: {e}")
