import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from emotion import extract_emotional_state
from insight import generate_insight
from action import suggest_micro_action
from closure import check_closure

import streamlit as st

st.set_page_config(page_title="Signal", layout="centered")
st.title("🔁 SIGNAL — Real-Time Emotional Co-Pilot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("What’s present for you right now?")

if st.button("Send") and user_input:
    state = extract_emotional_state(user_input)
    reflection = generate_insight(user_input, state)
    action = suggest_micro_action(state)
    closure = check_closure(state)

    st.session_state.history.append({
        "input": user_input,
        "reflection": reflection,
        "action": action,
        "closure": closure
    })

# Display chat
for entry in reversed(st.session_state.history):
    st.markdown(f"**You:** {entry['input']}")
    st.markdown(f"**Signal:** {entry['reflection']}")
    if entry['action']:
        st.markdown(f"🌀 *Try:* {entry['action']}")
    if entry['closure']:
        st.markdown(f"🧘 {entry['closure']}")
    st.markdown("---")
