import streamlit as st
import base64

st.set_page_config(page_title="Valentine 💖", layout="wide")

# ---------- SESSION STATE ----------
if "stage" not in st.session_state:
    st.session_state.stage = "landing"
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
[data-testid="stAppViewContainer"] {
    background-color: #ffc0cb !important;
}

/* Other pages light peach */
[data-testid="stAppViewContainer"]:not([data-page="landing"]) {
    background-color: #ffd6e7 !important;
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
    z-index: 1000;
}
@keyframes float {
    0% { top: 5%; left: 5%; }
    25% { top: 20%; left: 80%; }
    50% { top: 70%; left: 40%; }
    75% { top: 40%; left: 70%; }
    100% { top: 5%; left: 5%; }
}

/* Centered text */
.center { 
    text-align: center; 
    margin-top: 120px; 
}
.big-text { 
    font-size: 42px; 
    font-weight: bold; 
    color: #ff4d88; 
    margin-bottom: 40px;
}

/* Moving "No" button */
.runaway { 
    position: absolute; 
    padding: 12px 24px; 
    font-size: 18px; 
    border-radius: 8px; 
    border: none; 
    background: #ff69b4; 
    color: white; 
    cursor: pointer; 
}

/* Yes button styling */
.stButton button {
    width: 200px;
    height: 60px;
    font-size: 20px !important;
    background-color: #ff69b4 !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
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

// Handle envelope click
function openEnvelope() {
    window.location.href = window.location.href.split('?')[0] + '?stage=question';
}
</script>
""", unsafe_allow_html=True)

# ---------- AUTOPLAY MUSIC ON EVERY PAGE ----------
autoplay_audio()

# Get query parameters
query_params = st.experimental_get_query_params()

# ---------- LANDING PAGE ----------
if "stage" not in query_params or query_params["stage"][0] == "landing":
    st.session_state.stage = "landing"
    
    # Big throbbing heart
    st.markdown('<div class="big-heart">💖</div>', unsafe_allow_html=True)
    
    # Floating envelope with click handler
    st.markdown("""
    <div class="envelope" onclick="openEnvelope()">
        Open me 💌
    </div>
    """, unsafe_allow_html=True)
    
    # Empty container to prevent Streamlit from showing other elements
    st.empty()

# ---------- QUESTION PAGE ----------
elif query_params["stage"][0] == "question" or st.session_state.stage == "question":
    st.session_state.stage = "question"
    
    # Update background for other pages
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffd6e7 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="center big-text">Will you be my Valentine, again? 💗</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes 😍"):
            st.session_state.stage = "yes"
            st.rerun()
    with col2:
        st.markdown("""
        <button class="runaway" onmouseover="moveButton(this)" 
                onclick="window.location.href=window.location.href.split('?')[0] + '?stage=no'">
        No 😏
        </button>
        """, unsafe_allow_html=True)

# ---------- YES PAGE ----------
elif query_params["stage"][0] == "yes" or st.session_state.stage == "yes":
    st.session_state.stage = "yes"
    
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
elif query_params["stage"][0] == "no" or st.session_state.stage == "no":
    st.session_state.stage = "no"
    
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffd6e7 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="center">
        <div class="big-text">
            Oh<br><br>
            You missed your chance!<br>
            Better luck next time!
        </div>
    </div>
    """, unsafe_allow_html=True)
