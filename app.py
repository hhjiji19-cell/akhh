import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS with wandering envelope
def local_css():
    st.markdown("""
    <style>
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
        overflow: hidden !important;
    }
    
    /* Main container to allow envelope to move */
    .main-container {
        position: relative;
        width: 100%;
        height: 85vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    
    /* Wandering envelope that moves around entire screen */
    @keyframes wander {
        0% {
            transform: translate(0vw, 0vh) rotate(0deg) scale(1);
            left: 10%;
            top: 20%;
        }
        10% {
            transform: translate(15vw, -10vh) rotate(15deg) scale(1.1);
            left: 25%;
            top: 10%;
        }
        20% {
            transform: translate(-10vw, 20vh) rotate(-10deg) scale(0.9);
            left: 15%;
            top: 30%;
        }
        30% {
            transform: translate(20vw, 15vh) rotate(20deg) scale(1.2);
            left: 35%;
            top: 45%;
        }
        40% {
            transform: translate(-15vw, -5vh) rotate(-15deg) scale(0.95);
            left: 20%;
            top: 40%;
        }
        50% {
            transform: translate(25vw, -15vh) rotate(25deg) scale(1.15);
            left: 45%;
            top: 25%;
        }
        60% {
            transform: translate(-20vw, 25vh) rotate(-20deg) scale(0.85);
            left: 25%;
            top: 50%;
        }
        70% {
            transform: translate(30vw, 10vh) rotate(30deg) scale(1.3);
            left: 55%;
            top: 60%;
        }
        80% {
            transform: translate(-25vw, -20vh) rotate(-25deg) scale(0.9);
            left: 30%;
            top: 40%;
        }
        90% {
            transform: translate(10vw, 30vh) rotate(10deg) scale(1.05);
            left: 40%;
            top: 70%;
        }
        100% {
            transform: translate(0vw, 0vh) rotate(0deg) scale(1);
            left: 10%;
            top: 20%;
        }
    }
    
    .wandering-envelope {
        position: absolute !important;
        animation: wander 25s linear infinite;
        cursor: pointer;
        font-size: 6rem;
        transition: all 0.3s ease;
        z-index: 100;
        filter: drop-shadow(0 10px 20px rgba(210, 43, 105, 0.4));
        color: #D22B69;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 
            0 0 0 10px rgba(255, 182, 193, 0.3),
            0 0 0 20px rgba(255, 182, 193, 0.2),
            0 0 0 30px rgba(255, 182, 193, 0.1);
    }
    
    .wandering-envelope:hover {
        animation-play-state: paused;
        transform: scale(1.4) !important;
        filter: drop-shadow(0 15px 30px rgba(210, 43, 105, 0.6));
        z-index: 200;
    }
    
    /* Heart animation */
    @keyframes heartbeat {
        0% { transform: scale(1); }
        25% { transform: scale(1.1); }
        50% { transform: scale(1); }
        75% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    
    .heartbeat {
        animation: heartbeat 1.2s infinite;
        color: #FF0000;
        text-align: center;
        font-size: 7rem;
        margin: 10px 0 30px 0;
        filter: drop-shadow(0 0 10px rgba(255, 0, 0, 0.3));
    }
    
    /* Content that stays centered */
    .centered-content {
        position: relative;
        z-index: 10;
        background: rgba(255, 255, 255, 0.85);
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        width: 90%;
        backdrop-filter: blur(10px);
    }
    
    /* Main title */
    .main-title {
        color: #8B0A50 !important;
        font-size: 3rem;
        margin: 0 0 10px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9);
    }
    
    /* Subtitle */
    .subtitle {
        color: #D22B69 !important;
        font-size: 1.4rem;
        margin-bottom: 40px;
        font-family: 'Georgia', serif;
        text-align: center;
        font-style: italic;
    }
    
    /* Valentine question */
    .valentine-question {
        color: #8B0A50 !important;
        font-size: 3.2rem !important;
        text-align: center;
        margin: 50px 0 60px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
        line-height: 1.2;
        padding: 0 20px;
    }
    
    /* Response text */
    .response-text {
        color: #8B0A50 !important;
        font-size: 2.5rem;
        text-align: center;
        margin: 20px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.9);
    }
    
    /* Perfectly aligned buttons */
    .buttons-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin: 50px 0 30px 0;
        width: 100%;
    }
    
    .valentine-button {
        background: linear-gradient(135deg, #FF3366, #FF0066) !important;
        color: white !important;
        border: none !important;
        padding: 20px 45px !important;
        text-align: center !important;
        font-size: 1.8rem !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        min-width: 170px !important;
        height: 75px !important;
        box-shadow: 0 8px 20px rgba(255, 51, 102, 0.4) !important;
        transition: all 0.3s ease !important;
        margin: 0 !important;
    }
    
    .valentine-button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 0 15px 30px rgba(255, 51, 102, 0.6) !important;
    }
    
    .no-button {
        background: linear-gradient(135deg, #666666, #444444) !important;
        box-shadow: 0 8px 20px rgba(102, 102, 102, 0.4) !important;
    }
    
    .no-button:hover {
        background: linear-gradient(135deg, #555555, #333333) !important;
        box-shadow: 0 15px 30px rgba(68, 68, 68, 0.6) !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Music control */
    .music-control {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: linear-gradient(135deg, #FF3366, #D22B69);
        color: white;
        border: none;
        border-radius: 50%;
        width: 55px;
        height: 55px;
        font-size: 22px;
        cursor: pointer;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 5px 15px rgba(210, 43, 105, 0.4);
    }
    
    .music-control:hover {
        transform: scale(1.1);
    }
    
    /* GIF container */
    .gif-container {
        margin: 30px 0;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Action button */
    .action-button {
        background: linear-gradient(135deg, #FFB6C1, #FF8BA0) !important;
        color: #8B0A50 !important;
        border: none !important;
        padding: 15px 35px !important;
        font-size: 1.5rem !important;
        border-radius: 25px !important;
        margin-top: 30px !important;
        font-weight: bold !important;
    }
    
    /* Page containers */
    .page-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
        text-align: center;
        padding: 20px;
        width: 100%;
    }
    
    /* Make sure envelope stays on top */
    .wandering-envelope-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 5;
    }
    
    .wandering-envelope-container > div {
        pointer-events: auto;
    }
    </style>
    """, unsafe_allow_html=True)

def setup_audio():
    """Audio setup"""
    try:
        with open("music.mp3", "rb") as f:
            audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
        
        audio_html = f"""
        <audio id="valentineMusic" loop style="display: none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        
        <button id="musicBtn" class="music-control" onclick="toggleMusic()">🎵</button>
        
        <script>
            const audio = document.getElementById('valentineMusic');
            const musicBtn = document.getElementById('musicBtn');
            let isPlaying = false;
            
            function toggleMusic() {{
                if (isPlaying) {{
                    audio.pause();
                    musicBtn.innerHTML = '🎵';
                }} else {{
                    audio.volume = 0.6;
                    audio.play();
                    musicBtn.innerHTML = '🔊';
                }}
                isPlaying = !isPlaying;
            }}
            
            function tryPlay() {{
                audio.volume = 0.6;
                audio.play().then(() => {{
                    isPlaying = true;
                    musicBtn.innerHTML = '🔊';
                }});
            }}
            
            window.addEventListener('load', tryPlay);
            setTimeout(tryPlay, 1000);
            
            document.addEventListener('click', () => {{
                if (!isPlaying) tryPlay();
            }}, {{ once: true }});
            
            // Make envelope clickable
            document.addEventListener('DOMContentLoaded', function() {{
                const envelope = document.querySelector('.wandering-envelope');
                if (envelope) {{
                    envelope.addEventListener('click', function() {{
                        const openBtn = document.getElementById('openBtn');
                        if (openBtn) openBtn.click();
                    }});
                }}
            }});
        </script>
        """
        return audio_html
    except:
        return ""

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'response' not in st.session_state:
    st.session_state.response = None

# Apply CSS
local_css()

# Setup audio
st.markdown(setup_audio(), unsafe_allow_html=True)

# Main app logic
if st.session_state.page == 'landing':
    # Landing page with wandering envelope
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Wandering envelope that moves around entire screen
    st.markdown("""
    <div class="wandering-envelope-container">
        <div class="wandering-envelope" title="Click me!">💌</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered content
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    
    # Title
    st.markdown('<h1 class="main-title">For My Valentine ❤️</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Catch the floating envelope!</p>', unsafe_allow_html=True)
    
    # Heart
    st.markdown('<div class="heartbeat">❤️</div>', unsafe_allow_html=True)
    
    # Hidden button for envelope click
    if st.button(" ", key="openBtn", help="Click the floating envelope!"):
        st.session_state.page = 'valentine'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close centered-content
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

elif st.session_state.page == 'valentine':
    # Valentine question page
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    
    # Question only - NO heart
    st.markdown('<div class="valentine-question">Will you be my valentine, again?</div>', 
                unsafe_allow_html=True)
    
    # Perfectly aligned buttons
    st.markdown('<div class="buttons-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("YES 💖", key="yesBtn", use_container_width=True):
            st.session_state.response = 'yes'
            st.session_state.page = 'response'
            st.rerun()
    
    with col2:
        if st.button("NO", key="noBtn", use_container_width=True):
            st.session_state.response = 'no'
            st.session_state.page = 'response'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close buttons-container
    
    # Back button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back", key="backBtn"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close centered-content
    st.markdown('</div>', unsafe_allow_html=True)  # Close page-container

elif st.session_state.page == 'response':
    # Response page
    st.markdown('<div class="page-container">', unsafe_allow_html=True)
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    
    if st.session_state.response == 'yes':
        # YES response
        st.markdown('<div class="heartbeat">💖</div>', unsafe_allow_html=True)
        
        # GIF
        st.markdown('<div class="gif-container">', unsafe_allow_html=True)
        st.image(
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdT1n/12afltvVzJIesM/giphy.gif",
            use_column_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Text
        st.markdown('<div class="response-text">You gonna have more of me now!</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="response-text">I love you gullu pullu 💘</div>', 
                   unsafe_allow_html=True)
        
        # Effects
        st.balloons()
        
    else:
        # NO response
        st.markdown('<div class="heartbeat" style="color: #666;">💔</div>', 
                   unsafe_allow_html=True)
        
        # Text
        st.markdown('<div class="response-text" style="color: #666;">Oh...</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="response-text" style="color: #666;">You missed your chance</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="response-text" style="color: #666;">Better luck next time!</div>', 
                   unsafe_allow_html=True)
    
    # Restart button
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Start Over ✨", key="restartBtn", use_container_width=True):
        st.session_state.page = 'landing'
        st.session_state.response = None
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close centered-content
    st.markdown('</div>', unsafe_allow_html=True)  # Close page-container
