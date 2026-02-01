import streamlit as st
import base64

st.set_page_config(page_title="My Valentine ❤️", layout="wide", initial_sidebar_state="collapsed")

# ---------- SESSION STATE ----------
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'response' not in st.session_state:
    st.session_state.response = None

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
/* Remove Streamlit padding/margins */
.css-18e3th9 {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
.css-1d391kg {padding-top: 0rem;}

/* Hide menu/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Checkered baby pink background */
.stApp {
    background-color: #FFE6E6 !important;
    background-image: 
        linear-gradient(45deg, #ffb6c1 25%, transparent 25%),
        linear-gradient(-45deg, #ffb6c1 25%, transparent 25%),
        linear-gradient(45deg, transparent 75%, #ffb6c1 75%),
        linear-gradient(-45deg, transparent 75%, #ffb6c1 75%);
    background-size: 30px 30px;
    background-position: 0 0, 0 15px, 15px -15px, -15px 0px;
    background-attachment: fixed;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Center container */
.centered {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    height: 100vh;
}

/* Throbbing heart */
.heartbeat {
    animation: heartbeat 1.2s infinite;
    color: red;
    font-size: 10rem;
    margin: 50px 0;
    filter: drop-shadow(0 0 20px rgba(255,0,0,0.5));
}
@keyframes heartbeat {
    0% {transform: scale(1);}
    25% {transform: scale(1.1);}
    50% {transform: scale(1);}
    75% {transform: scale(1.1);}
    100% {transform: scale(1);}
}

/* Floating envelope */
@keyframes float {
    0% {transform: translate(0,0);}
    25% {transform: translate(20vw, 10vh);}
    50% {transform: translate(-15vw, 20vh);}
    75% {transform: translate(15vw, -10vh);}
    100% {transform: translate(0,0);}
}
.wandering-envelope {
    font-size: 6rem;
    position: absolute;
    cursor: pointer;
    animation: float 10s ease-in-out infinite;
    color: #D22B69;
    z-index: 100;
    filter: drop-shadow(0 10px 20px rgba(210,43,105,0.5));
}

/* Landing page button */
.landing-button {
    background: linear-gradient(135deg, #FF3366, #FF0066);
    color: white;
    border: none;
    padding: 20px 50px;
    font-size: 1.8rem;
    border-radius: 30px;
    font-weight: bold;
    margin-top: 40px;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(255,51,102,0.4);
}
.landing-button:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 15px 30px rgba(255,51,102,0.6);
}

/* Valentine question */
.valentine-question {
    color: #D22B69;
    font-size: 3rem;
    font-weight: bold;
    margin: 50px 0;
}

/* Buttons container */
.buttons-container {
    display: flex;
    gap: 40px;
    justify-content: center;
    margin-top: 40px;
}

/* YES/NO buttons */
.valentine-button {
    background: linear-gradient(135deg, #FF3366, #FF0066);
    color: white;
    border: none;
    padding: 20px 50px;
    font-size: 1.8rem;
    border-radius: 30px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
}
.valentine-button:hover {
    transform: translateY(-5px) scale(1.05);
}

/* NO button style */
.no-button {
    background: linear-gradient(135deg, #666, #444);
}
.no-button:hover {
    background: linear-gradient(135deg, #555, #333);
}
</style>
""", unsafe_allow_html=True)

# ---------- AUDIO SETUP ----------
def setup_audio():
    try:
        with open("music.mp3", "rb") as f:
            audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
        html = f"""
        <audio id="valentineMusic" loop autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        return html
    except:
        return ""
st.markdown(setup_audio(), unsafe_allow_html=True)

# ---------- LANDING PAGE ----------
if st.session_state.page == 'landing':
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.markdown('<div class="heartbeat">❤️</div>', unsafe_allow_html=True)
    
    # Floating envelope
    st.markdown("""
    <div class="wandering-envelope" onclick="document.getElementById('openBtn').click()">💌</div>
    """, unsafe_allow_html=True)
    
    # Landing page button
    if st.button("Click me to open the envelope", key="openBtn"):
        st.session_state.page = 'valentine'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- VALENTINE QUESTION PAGE ----------
elif st.session_state.page == 'valentine':
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.markdown('<div class="valentine-question">Will you be my Valentine, again?</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="buttons-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("YES 💖"):
            st.session_state.response = 'yes'
            st.session_state.page = 'response'
            st.rerun()
    with col2:
        if st.button("NO 💔"):
            st.session_state.response = 'no'
            st.session_state.page = 'response'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- RESPONSE PAGE ----------
elif st.session_state.page == 'response':
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    if st.session_state.response == 'yes':
        st.markdown('<div class="heartbeat">💖</div>', unsafe_allow_html=True)
        st.image(
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdT1n/12afltvVzJIesM/giphy.gif",
            width=400
        )
        st.markdown('<h2 style="color:#D22B69;">I love you gullu pullu 💘</h2>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown('<div class="heartbeat" style="color:#666;">💔</div>', unsafe_allow_html=True)
        st.markdown('<h2 style="color:#666;">Oh... You missed your chance 😌</h2>', unsafe_allow_html=True)
    
    if st.button("Start Over ✨"):
        st.session_state.page = 'landing'
        st.session_state.response = None
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
