from backend.pipelines.trend_pipeline import (
    run_trends
)

trends = run_trends()

print("\n TRENDING TOPICS\n")

for t in trends:

    print(
        f"{t['topic']} "
        f"(Score: {t['trend_score']}) "
        f"Momentum: {t['momentum']}"
    )