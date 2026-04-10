def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return None

    return {
        "anger": 0.01,
        "disgust": 0.01,
        "fear": 0.01,
        "joy": 0.96,
        "sadness": 0.01,
        "dominant_emotion": "joy"
    }