import os
import sys
import json
import traceback
from faker import Faker

# Mock up environment variables for testing local Supabase if available
from dotenv import load_dotenv
load_dotenv(".env")

from database import save_session_to_db, get_session_from_db

dummy_session = {
    "id": "test-session-1234",
    "user_id": "00000000-0000-0000-0000-000000000000",
    "scenario_type": "custom",
    "session_mode": "skill_assessment",
    "title": "Test Title",
    "ai_character": "alex",
    "mode": "coaching",
    "role": "manager",
    "ai_role": "employee",
    "scenario": "test scenario",
    "framework": ["GROW"],
    "transcript": [
        {"role": "assistant", "content": "How can I help?", "audio_url": None},
        {"role": "user", "content": "I need help", "audio_url": "test.mp3"}
    ],
    "report_data": {},
    "completed": False,
    "created_at": "2026-03-09T10:00:00.000000"
}

print("Testing save_session_to_db with incomplete session...")
success = save_session_to_db(dummy_session)
print(f"Save success: {success}")

if success:
    print("Testing get_session_from_db...")
    fetched = get_session_from_db("test-session-1234")
    print(f"Fetched session exists: {fetched is not None}")
    if fetched:
        print(f"Fetched transcript: {fetched.get('transcript')}")

print("\nTesting complete session save (with report)...")
dummy_session["completed"] = True
dummy_session["report_data"] = {
    "meta": {"overall_grade": "8/10", "completed_at": "2026-03-09T10:15:00.000000"}
}
success2 = save_session_to_db(dummy_session)
print(f"Complete save success: {success2}")
