def check_closure(state):
    score = float(state.get("intensity_score", 0.0))
    emotion = state.get("primary_emotion", "").lower()

    if score < 3.0:
        return "🧘 You seem clear. Let this settle."
    if emotion == "overwhelm" and score > 7.5:
        return "🌫️ No need to decide right now. Just breathe."
    return None
