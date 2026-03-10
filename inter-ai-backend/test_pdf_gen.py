import sys
import os
sys.path.append(r"c:\Users\suyas\OneDrive\Desktop\coact-ai\inter-ai-backend")
from cli_report import generate_report

try:
    generate_report(
        transcript=[{"role": "user", "content": "hi"}],
        role="user",
        ai_role="coach",
        scenario="test",
        framework=["GROW"],
        filename="test_report.pdf",
        mode="coaching",
        precomputed_data={
            "meta": {"overall_grade": "8/10", "session_mode": "skill_assessment"},
            "executive_summary": {"snapshot": "good", "final_score": "8/10", "outcome_summary": "good"},
            "strengths_and_improvements": { "strengths": ["good"], "missed_opportunities": ["bad"] },
            "heat_map": [{"dimension": "Test", "score": "8.5/10"}, {"dimension": "Test 2", "score": "9"}]
        },
        scenario_type="coaching"
    )
    print("PDF generation successful")
except Exception as e:
    import traceback
    traceback.print_exc()
