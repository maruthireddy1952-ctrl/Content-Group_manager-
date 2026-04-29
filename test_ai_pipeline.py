from backend.services.transcript_service import get_transcript
from backend.services.ai_analysis_service import analyze_video

video_id = "5MgBikgcWnY"

transcript = get_transcript(video_id)
print("Transcript length:", len(transcript) if transcript else 0)
print(transcript[:200])
if not transcript:
    print("No transcript found for this video.")
else:
    analysis = analyze_video(transcript)
    print(analysis)
