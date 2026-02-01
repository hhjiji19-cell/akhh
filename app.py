import streamlit as st
import base64
import time

st.set_page_config(page_title="Valentine 💖", layout="wide")

# ---------- SESSION STATE ----------
if "stage" not in st.session_state:
    st.session_state.stage = "landing"
if "music_started" not in st.session_state:
    st.session_state.music_started = False
if "envelope_opened" not in st.session_state:
    st.session_state.envelope_opened = False

# ---------- AUTOPLAY MUSIC ----------
def autoplay_audio():
    if not st.session_state.music_started:
        try:
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
        except:
            # If music file doesn't exist, just continue without it
            st.session_state.music_started = True

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
/* Main container styling */
.main {
    background-color: #ffc0cb !important;
    background-image: 
        linear-gradient(rgba(255, 192, 203, 0.8) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 192, 203, 0.8) 1px, transparent 1px);
    background-size: 50px 50px;
    min-height: 100vh;
    margin: 0;
    padding: 0;
}

/* For other pages */
.other-page {
    background-color: #ffd6e7 !important;
    background-image: 
        linear-gradient(rgba(255, 214, 231, 0.8) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 214, 231, 0.8) 1px, transparent 1px);
    background-size: 50px 50px;
    min-height: 100vh;
}

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

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
    z-index: 1;
}
@keyframes pulse {
    0% { transform: translate(-50%, -50%) scale(1); }
    50% { transform: translate(-50%, -50%) scale(1.2); }
    100% { transform: translate(-50%, -50%) scale(1); }
}

/* Floating envelope */
.envelope-container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1000;
    text-align: center;
}

.envelope {
    width: 200px;
    height: 140px;
    background: white;
    border-radius: 12px;
    font-weight: bold;
    color: #ff69b4;
    cursor: pointer;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    animation: float 8s infinite ease-in-out;
    font-size: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    border: 2px dashed #ff69b4;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}

/* Open button */
.open-btn {
    background: linear-gradient(45deg, #ff69b4, #ff1493);
    color: white;
    padding: 15px 40px;
    border: none;
    border-radius: 30px;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
    transition: all 0.3s ease;
}

.open-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(255, 105, 180, 0.6);
}

/* Centered content */
.center-container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    width: 100%;
    max-width: 800px;
    z-index: 2;
}

.big-text {
    font-size: 48px;
    font-weight: bold;
    color: #ff4d88;
    margin-bottom: 40px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

/* Yes/No buttons */
.yes-no-container {
    display: flex;
    justify-content: center;
    gap: 50px;
    margin-top: 40px;
}

.yes-btn, .no-btn {
    padding: 15px 40px;
    font-size: 24px;
    border: none;
    border-radius: 15px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: bold;
}

.yes-btn {
    background: linear-gradient(45deg, #ff69b4, #ff1493);
    color: white;
    box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
}

.yes-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 8px 25px rgba(255, 105, 180, 0.6);
}

.no-btn {
    background: linear-gradient(45deg, #87CEFA, #1E90FF);
    color: white;
    box-shadow: 0 5px 15px rgba(135, 206, 250, 0.4);
    position: relative;
}

.no-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 8px 25px rgba(135, 206, 250, 0.6);
}

/* Floating hearts */
.heart {
    position: absolute;
    font-size: 24px;
    animation: floatUp 6s linear infinite;
    opacity: 0;
}

@keyframes floatUp {
    0% {
        transform: translateY(100vh) scale(0.5);
        opacity: 0;
    }
    10% {
        opacity: 1;
    }
    90% {
        opacity: 1;
    }
    100% {
        transform: translateY(-100px) scale(1.5);
        opacity: 0;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- FLOATING HEARTS JAVASCRIPT ----------
st.markdown("""
<script>
// Create floating hearts
function createHearts() {
    const container = document.body;
    for (let i = 0; i < 30; i++) {
        const heart = document.createElement('div');
        heart.className = 'heart';
        heart.innerHTML = '💖';
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDelay = Math.random() * 5 + 's';
        heart.style.animationDuration = (3 + Math.random() * 7) + 's';
        heart.style.fontSize = (20 + Math.random() * 30) + 'px';
        container.appendChild(heart);
    }
}

// Run when page loads
window.addEventListener('load', createHearts);
</script>
""", unsafe_allow_html=True)

# ---------- AUTOPLAY MUSIC ----------
autoplay_audio()

# ---------- LANDING PAGE ----------
if st.session_state.stage == "landing":
    # Apply baby pink checkered background
    st.markdown('<div class="main"></div>', unsafe_allow_html=True)
    
    # Big throbbing heart
    st.markdown('<div class="big-heart">💖</div>', unsafe_allow_html=True)
    
    # Envelope and button container
    st.markdown("""
    <div class="envelope-container">
        <div class="envelope">
            💌 Valentine's Letter 💌
        </div>
        <button class="open-btn" onclick="window.location.href=window.location.href.split('?')[0] + '?open=envelope'">
            Click me to open the envelope
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if envelope should be opened
    query_params = st.experimental_get_query_params()
    if query_params.get("open") == ["envelope"]:
        st.session_state.stage = "question"
        st.rerun()

# ---------- QUESTION PAGE ----------
elif st.session_state.stage == "question":
    # Apply different background for question page
    st.markdown('<div class="other-page"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="center-container">
        <div class="big-text">Will you be my Valentine, again? 💗</div>
        <div class="yes-no-container">
            <button class="yes-btn" onclick="window.location.href=window.location.href.split('?')[0] + '?answer=yes'">
                Yes 😍
            </button>
            <button class="no-btn" 
                    onmouseover="this.style.top=Math.random()*70+'vh'; this.style.left=Math.random()*70+'vw';"
                    onclick="window.location.href=window.location.href.split('?')[0] + '?answer=no'">
                No 😏
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Check for answer
    query_params = st.experimental_get_query_params()
    if query_params.get("answer") == ["yes"]:
        st.session_state.stage = "yes"
        st.rerun()
    elif query_params.get("answer") == ["no"]:
        st.session_state.stage = "no"
        st.rerun()

# ---------- YES PAGE ----------
elif st.session_state.stage == "yes":
    # Apply different background for yes page
    st.markdown('<div class="other-page"></div>', unsafe_allow_html=True)
    
    st.balloons()
    
    st.markdown("""
    <div class="center-container">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif" 
             width="350" style="border-radius: 20px; margin-bottom: 30px;">
        <div class="big-text">
            Another year of you tolerating me,<br><br>
            I love you so much gullu pullu ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- NO PAGE ----------
elif st.session_state.stage == "no":
    # Apply different background for no page
    st.markdown('<div class="other-page"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="center-container">
        <div class="big-text">
            Oh<br><br>
            You missed your chance!<br>
            Better luck next time! 😌
        </div>
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm84emN4MHRlMG5zZndqOWZtaWNoNmM0MjJ5Y3ppNnE1aDl5cm9vcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l2JhL1YfZP4P8z1EI/giphy.gif" 
             width="300" style="border-radius: 20px; margin-top: 30px;">
    </div>
    """, unsafe_allow_html=True)
