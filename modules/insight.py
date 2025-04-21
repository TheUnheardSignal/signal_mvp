import openai
openai.api_key = "YOUR_API_KEY"

def generate_insight(user_input, emotional_state):
    prompt = f"""
Input: \"{user_input}\"

Emotion: {emotional_state['primary_emotion']}
Underlayer: {emotional_state['underlayer']}
Intensity: {emotional_state['intensity_score']}
Frame: {emotional_state['signal_frame']}

Respond with:
- 1-paragraph reflection or reframe
- Metaphoric, emotionally precise
- No advice or commands
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are SIGNAL, a recursive emotional mirror."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.85
    )
    return response['choices'][0]['message']['content']
