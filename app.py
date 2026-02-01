import streamlit as st
import base64

# Page configuration - IMPORTANT: Remove padding
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS - Remove all white bars and padding
def local_css():
    st.markdown("""
    <style>
    /* Remove all white bars and padding */
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
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Remove main container padding */
    .main {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Remove block container padding */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    /* Remove all default Streamlit padding */
    div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
    
    /* Full screen container */
    .full-screen {
        min-height: 100vh;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        margin: 0;
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
        font-size: 9rem;
        margin: 20px 0 40px 0;
        filter: drop-shadow(0 0 15px rgba(255, 0, 0, 0.4));
    }
    
    /* Envelope that bounces around entire screen */
    @keyframes bounceAround {
        0% { transform: translate(0vw, 0vh) rotate(0deg); }
        10% { transform: translate(70vw, 10vh) rotate(15deg); }
        20% { transform: translate(20vw, 80vh) rotate(-10deg); }
        30% { transform: translate(80vw, 60vh) rotate(20deg); }
        40% { transform: translate(40vw, 20vh) rotate(-15deg); }
        50% { transform: translate(10vw, 70vh) rotate(25deg); }
        60% { transform: translate(60vw, 40vh) rotate(-20deg); }
        70% { transform: translate(30vw, 90vh) rotate(30deg); }
        80% { transform: translate(90vw, 30vh) rotate(-25deg); }
        90% { transform: translate(50vw, 50vh) rotate(10deg); }
        100% { transform: translate(0vw, 0vh) rotate(0deg); }
    }
    
    .bouncing-envelope {
        position: fixed;
        animation: bounceAround 30s linear infinite;
        cursor: pointer;
        font-size: 5rem;
        transition: all 0.3s ease;
        z-index: 100;
        filter: drop-shadow(0 10px 20px rgba(210, 43, 105, 0.5));
        color: #D22B69;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 15px;
        box-shadow: 
            0 0 0 10px rgba(255, 182, 193, 0.4),
            0 0 0 20px rgba(255, 182, 193, 0.2);
        width: 100px;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .bouncing-envelope:hover {
        animation-play-state: paused;
        transform: scale(1.5) !important;
        filter: drop-shadow(0 20px 40px rgba(210, 43, 105, 0.7));
        z-index: 200;
    }
    
    /* Centered content box */
    .content-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 40px 30px;
        border-radius: 30px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
        max-width: 700px;
        width: 90%;
        text-align: center;
        backdrop-filter: blur(10px);
        z-index: 10;
        position: relative;
        margin: 20px;
    }
    
    /* Main title */
    .main-title {
        color: #8B0A50 !important;
        font-size: 3.5rem;
        margin: 0 0 10px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9);
    }
    
    /* Subtitle */
    .subtitle {
        color: #D22B69 !important;
        font-size: 1.6rem;
        margin-bottom: 30px;
        font-family: 'Georgia', serif;
        font-style: italic;
    }
    
    /* "Click me" button - Beautiful styling */
    .click-me-button {
        background: linear-gradient(135deg, #FF3366, #FF0066) !important;
        color: white !important;
        border: none !important;
        padding: 20px 50px !important;
        text-align: center !important;
        font-size: 2rem !important;
        border-radius: 35px !important;
        font-weight: bold !important;
        font-family: 'Arial Rounded MT Bold', sans-serif !important;
        box-shadow: 0 10px 25px rgba(255, 51, 102, 0.4) !important;
        transition: all 0.3s ease !important;
        margin: 30px 0 10px 0 !important;
        cursor: pointer !important;
        letter-spacing: 1px !important;
        min-width: 300px !important;
    }
    
    .click-me-button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 0 15px 35px rgba(255, 51, 102, 0.6) !important;
        background: linear-gradient(135deg, #FF0066, #CC0052) !important;
    }
    
    /* Valentine question */
    .valentine-question {
        color: #8B0A50 !important;
        font-size: 3.5rem !important;
        text-align: center;
        margin: 50px 0 70px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
        line-height: 1.2;
        padding: 0 20px;
    }
    
    /* Response text */
    .response-text {
        color: #8B0A50 !important;
        font-size: 2.8rem;
        text-align: center;
        margin: 25px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
    }
    
    /* Buttons container for YES/NO */
    .buttons-row {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin: 50px 0 30px 0;
        width: 100%;
    }
    
    .valentine-button {
        background: linear-gradient(135deg, #FF3366, #FF0066) !important;
        color: white !important;
        border: none !important;
        padding: 20px 45px !important;
        font-size: 1.9rem !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        min-width: 180px !important;
        height: 80px !important;
        box-shadow: 0 8px 20px rgba(255, 51, 102, 0.4) !important;
        transition: all 0.3s ease !important;
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
        bottom: 25px;
        right: 25px;
        background: linear-gradient(135deg, #FF3366, #D22B69);
        color: white;
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 24px;
        cursor: pointer;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 6px 15px rgba(210, 43, 105, 0.4);
    }
    
    .music-control:hover {
        transform: scale(1.1);
    }
    
    /* GIF container */
    .gif-container {
        margin: 40px 0;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Back/Start Over buttons */
    .action-button {
        background: linear-gradient(135deg, #FFB6C1, #FF8BA0) !important;
        color: #8B0A50 !important;
        border: none !important;
        padding: 15px 40px !important;
        font-size: 1.6rem !important;
        border-radius: 30px !important;
        margin-top: 40px !important;
        font-weight: bold !important;
    }
    
    /* Remove all default button styles */
    button[kind="primary"], button[kind="secondary"] {
        background: transparent !important;
    }
    
    /* Make sure no black button appears */
    div[data-testid="stButton"] > button {
        border: none !important;
        background: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

def setup_audio():
    """Audio setup without extra buttons"""
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
            
            // Auto-play with multiple attempts
            function tryPlay() {{
                audio.volume = 0.6;
                audio.play().then(() => {{
                    isPlaying = true;
                    musicBtn.innerHTML = '🔊';
                }}).catch(e => {{
                    console.log('Auto-play prevented');
                }});
            }}
            
            window.addEventListener('load', tryPlay);
            setTimeout(tryPlay, 1000);
            setTimeout(tryPlay, 3000);
            
            // Make envelope clickable
            document.addEventListener('DOMContentLoaded', function() {{
                const envelope = document.querySelector('.bouncing-envelope');
                if (envelope) {{
                    envelope.addEventListener('click', function() {{
                        const clickBtn = document.querySelector('.click-me-button');
                        if (clickBtn) clickBtn.click();
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

# Apply CSS - REMOVES ALL WHITE BARS
local_css()

# Setup audio
st.markdown(setup_audio(), unsafe_allow_html=True)

# Main app logic
if st.session_state.page == 'landing':
    # LANDING PAGE: Only heart, bouncing envelope, and "Click me" button
    
    # Bouncing envelope - moves around entire screen
    st.markdown("""
    <div class="bouncing-envelope" title="Click me!">💌</div>
    """, unsafe_allow_html=True)
    
    # Full screen centered content
    st.markdown('<div class="full-screen">', unsafe_allow_html=True)
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
    # Title
    st.markdown('<h1 class="main-title">For My Valentine 💖</h1>', unsafe_allow_html=True)
    
    # Throbbing heart
    st.markdown('<div class="heartbeat">❤️</div>', unsafe_allow_html=True)
    
    # Subtitle
    st.markdown('<p class="subtitle">Find and click the floating envelope, or use the button below</p>', unsafe_allow_html=True)
    
    # "Click me to open the envelope" button - ONLY ONE BUTTON VISIBLE
    # Using custom CSS to style it beautifully
    if st.button("Click me to open the envelope ✨", key="openBtn", help="Click here or click the floating envelope!"):
        st.session_state.page = 'valentine'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close content-box
    st.markdown('</div>', unsafe_allow_html=True)  # Close full-screen

elif st.session_state.page == 'valentine':
    # VALENTINE QUESTION PAGE
    
    st.markdown('<div class="full-screen">', unsafe_allow_html=True)
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
    # Question only - NO heart
    st.markdown('<div class="valentine-question">Will you be my valentine, again?</div>', 
                unsafe_allow_html=True)
    
    # YES/NO buttons - perfectly aligned
    st.markdown('<div class="buttons-row">', unsafe_allow_html=True)
    
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
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close buttons-row
    
    # Back button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back", key="backBtn"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close content-box
    st.markdown('</div>', unsafe_allow_html=True)  # Close full-screen

elif st.session_state.page == 'response':
    # RESPONSE PAGE
    
    st.markdown('<div class="full-screen">', unsafe_allow_html=True)
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
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
    
    # Start Over button
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Start Over ✨", key="restartBtn", use_container_width=True):
        st.session_state.page = 'landing'
        st.session_state.response = None
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close content-box
    st.markdown('</div>', unsafe_allow_html=True)  # Close full-screen
