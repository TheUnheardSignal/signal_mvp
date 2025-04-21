import openai
openai.api_key = "YOUR_API_KEY"

def extract_emotional_state(user_input):
    prompt = f"""
You are SIGNAL, a sentient emotional mirror. Detect:
1. Primary emotion
2. Underlayer context
3. Intensity (0.0–10.0)
4. Symbolic signal frame

Input: \"{user_input}\"
Return JSON.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are SIGNAL."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return parse_response(response['choices'][0]['message']['content'])

def parse_response(raw):
    import json
    try: return json.loads(raw)
    except:
        lines = raw.splitlines()
        result = {}
        for line in lines:
            if ':' in line:
                k, v = line.split(':', 1)
                result[k.strip().lower().replace(" ", "_")] = v.strip()
        return result
