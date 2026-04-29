from ai_models.llm.deepseek_client import analyze_transcript


def analyze_video(transcript):

    result = analyze_transcript(transcript)

    topic = result.get("topic")
    category = result.get("category")
    keywords = result.get("keywords")
    trend_score = result.get("trend_score")

    return {
        "topic": topic,
        "category": category,
        "keywords": keywords,
        "trend_score": trend_score
    }