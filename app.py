import streamlit as st
import base64

st.set_page_config(page_title="Valentine 💖", layout="wide")

# ---------- SESSION STATE ----------
if "stage" not in st.session_state:
    st.session_state.stage = "landing"
if "envelope_opened" not in st.session_state:
    st.session_state.envelope_opened = False
if "music_started" not in st.session_state:
    st.session_state.music_started = False

# ---------- AUTOPLAY MUSIC ----------
def autoplay_audio():
    if not st.session_state.music_started:
        with open("music.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
        st.markdown(f"""
        <audio id="bg-music" autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
        const music = document.getElementById("bg-music");
        music.play();
        </script>
        """, unsafe_allow_html=True)
        st.session_state.music_started = True

# ---------- GLOBAL CSS + JS ----------
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
    border-radius: 12px;
    text-align: center;
    line-height: 120px;
    font-weight: bold;
    color: #ff69b4;
    cursor: pointer;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    animation: float 8s infinite ease-in-out;
    font-size: 18px;
}
@keyframes float {
    0% { top: 5%; left: 5%; }
    25% { top: 20%; left: 80%; }
    50% { top: 70%; left: 40%; }
    75% { top: 40%; left: 70%; }
    100% { top: 5%; left: 5%; }
}

/* Centered text */
.center { text-align: center; margin-top: 120px; }
.big-text { font-size: 42px; font-weight: bold; color: #ff4d88; }

/* Moving "No" button */
.runaway { 
    position: absolute; 
    padding:12px 24px; 
    font-size:18px; 
    border-radius:8px; 
    border:none; 
    background:#ff69b4; 
    color:white; 
    cursor:pointer; 
}

/* Floating hearts animation */
.heart-float {
    position: absolute;
    font-size: 24px;
    animation-name: floatheart;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}
@keyframes floatheart {
    0% { transform: translateY(100vh) scale(1); opacity: 1; }
    100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
}
</style>

<script>
// Floating hearts
for (let i = 0; i < 25; i++) {
    let heart = document.createElement("div");
    heart.className = "heart-float";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (6 + Math.random() * 6) + "s";
    heart.innerHTML = "💖";
    document.body.appendChild(heart);
}

// Move button away
function moveButton(btn){
    btn.style.top = Math.random()*70 + "vh";
    btn.style.left = Math.random()*70 + "vw";
}
</script>
""", unsafe_allow_html=True)

# ---------- AUTOPLAY MUSIC ON EVERY PAGE ----------
autoplay_audio()

# ---------- LANDING PAGE ----------
if st.session_state.stage == "landing":
    st.markdown('<div class="big-heart">💖</div>', unsafe_allow_html=True)

    if not st.session_state.envelope_opened:
        st.markdown("""
        <div class="envelope" onclick="document.querySelector('.envelope').style.display='none';">
            Open me 💌
        </div>
        """, unsafe_allow_html=True)
        if st.button("💌 Open the envelope"):
            st.session_state.envelope_opened = True
            st.session_state.stage = "question"
            st.rerun()
    else:
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
        st.markdown("""
        <button class="runaway"
        onmouseover="moveButton(this)">
        No 😏
        </button>
        <script>
        document.querySelector('.runaway').onclick = function(){window.location.href=window.location.href + '#no';};
        </script>
        """, unsafe_allow_html=True)

    # Detect URL hash for "No" click
    if st.experimental_get_query_params().get('no'):
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
