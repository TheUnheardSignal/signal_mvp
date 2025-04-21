import random

MICRO_ACTIONS = {
    "overwhelm": ["Close your eyes for 5 seconds.", "Breathe in stillness."],
    "frustration": ["Shake your wrists.", "Stretch one tight area."],
    "anxiety": ["Notice 3 textures.", "Anchor your feet to the floor."],
    "sadness": ["Hands on heart.", "Say: I don’t have to rush this."],
    "unknown": ["Be still. Signal is with you."]
}

def suggest_micro_action(state):
    emotion = state.get("primary_emotion", "unknown").lower()
    return random.choice(MICRO_ACTIONS.get(emotion, MICRO_ACTIONS["unknown"]))
