import streamlit as st

st.set_page_config(page_title="Valentine 💖", layout="wide")

# ---------- SESSION STATE ----------
if "stage" not in st.session_state:
    st.session_state.stage = "landing"
if "music_started" not in st.session_state:
    st.session_state.music_started = False

# ---------- PLAY MUSIC ----------
if not st.session_state.music_started:
    st.audio("music.mp3", format="audio/mp3", start_time=0)
    st.session_state.music_started = True

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
body {
    overflow: hidden;
    margin: 0;
    font-family: sans-serif;
}

/* Landing page baby pink background */
body[data-page="landing"] {
    background-color: #ffc0cb;
}

/* Other pages light peach */
body[data-page]:not([data-page="landing"]) {
    background-color: #ffd6e7;
}

/* Big throbbing heart */
.big-heart {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 180px;
    color: red;
    animation: pulse 1.2s infinite;
    opacity: 0.9;
}
@keyframes pulse {
    0% { transform: translate(-50%, -50%) scale(1); }
    50% { transform: translate(-50%, -50%) scale(1.2); }
    100% { transform: translate(-50%, -50%) scale(1); }
}

/* Floating envelope */
.envelope {
    width: 180px;
    height: 120px;
    background: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 12px;
    text-align: center;
    line-height: 120px;
    font-weight: bold;
    color: #ff69b4;
    cursor: pointer;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    font-size: 18px;
}

/* Centered text */
.center { text-align: center; margin-top: 120px; }
.big-text { font-size: 42px; font-weight: bold; color: #ff4d88; }

/* Buttons */
.stButton>button {
    padding: 12px 24px;
    font-size: 18px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    margin: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- LANDING PAGE ----------
if st.session_state.stage == "landing":
    st.markdown('<div class="big-heart">💖</div>', unsafe_allow_html=True)
    
    # Envelope click
    if st.button("💌 Open Envelope"):
        st.session_state.stage = "question"
        st.rerun()

# ---------- QUESTION PAGE ----------
elif st.session_state.stage == "question":
    st.markdown('<div class="center big-text">Will you be my Valentine, again? 💗</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes 😍"):
            st.session_state.stage = "yes"
            st.rerun()
    with col2:
        if st.button("No 😏"):
            st.session_state.stage = "no"
            st.rerun()

# ---------- YES PAGE ----------
elif st.session_state.stage == "yes":
    st.balloons()
    st.markdown("""
    <div class="center">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif" width="350">
        <div class="big-text">
            Another year of you tolerating me,<br><br>
            I love you so much gullu pullu ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- NO PAGE ----------
elif st.session_state.stage == "no":
    st.markdown("""
    <div class="center big-text">
        Oh,<br><br>
        You missed your chance 😌<br>
        Better luck next time!
    </div>
    """, unsafe_allow_html=True)
