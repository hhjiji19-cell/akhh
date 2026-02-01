import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS with checkered background and perfect alignments
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
        font-size: 8rem;
        margin: 10px 0 20px 0;
        filter: drop-shadow(0 0 10px rgba(255, 0, 0, 0.3));
    }
    
    /* Floating envelope with checkered pattern */
    @keyframes floatCheckered {
        0% { 
            transform: translate(0px, 0px) rotate(0deg);
            background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        }
        33% { 
            transform: translate(80px, -40px) rotate(5deg);
            background-position: 5px 5px, 5px 15px, 15px -5px, -5px 5px;
        }
        66% { 
            transform: translate(-60px, 30px) rotate(-3deg);
            background-position: -5px -5px, -5px 5px, 5px -15px, -15px -5px;
        }
        100% { 
            transform: translate(0px, 0px) rotate(0deg);
            background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        }
    }
    
    .checkered-envelope {
        animation: floatCheckered 15s ease-in-out infinite;
        cursor: pointer;
        text-align: center;
        font-size: 7rem;
        margin: 30px 0 5px 0;
        position: relative;
        transition: all 0.3s ease;
        color: #D22B69;
        background-image: 
            linear-gradient(45deg, rgba(255, 182, 193, 0.3) 25%, transparent 25%),
            linear-gradient(-45deg, rgba(255, 182, 193, 0.3) 25%, transparent 25%),
            linear-gradient(45deg, transparent 75%, rgba(255, 182, 193, 0.3) 75%),
            linear-gradient(-45deg, transparent 75%, rgba(255, 182, 193, 0.3) 75%);
        background-size: 20px 20px;
        background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        width: 120px;
        height: 120px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-left: auto;
        margin-right: auto;
    }
    
    .checkered-envelope:hover {
        transform: scale(1.2);
        animation-play-state: paused;
        box-shadow: 0 10px 25px rgba(210, 43, 105, 0.4);
    }
    
    /* Envelope icon */
    .envelope-icon {
        font-size: 5rem;
        z-index: 2;
    }
    
    /* Main title */
    .main-title {
        color: #8B0A50 !important;
        font-size: 3.2rem;
        margin: 10px 0 5px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9);
    }
    
    /* Subtitle */
    .subtitle {
        color: #D22B69 !important;
        font-size: 1.3rem;
        margin-bottom: 30px;
        font-family: 'Georgia', serif;
        text-align: center;
        font-style: italic;
    }
    
    /* Valentine question - Perfectly centered */
    .valentine-question {
        color: #8B0A50 !important;
        font-size: 3.5rem !important;
        text-align: center;
        margin: 60px 0 70px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
        line-height: 1.2;
        padding: 0 20px;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9);
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
    
    /* Perfectly aligned button container */
    .aligned-buttons {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 40px;
        margin: 40px 0;
        width: 100%;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Button styling - SAME SIZE for perfect alignment */
    .valentine-button {
        background: linear-gradient(135deg, #FF3366, #FF0066) !important;
        color: white !important;
        border: none !important;
        padding: 18px 40px !important;
        text-align: center !important;
        font-size: 1.8rem !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        font-family: 'Arial', sans-serif !important;
        box-shadow: 0 6px 15px rgba(255, 51, 102, 0.3) !important;
        transition: all 0.3s ease !important;
        min-width: 160px !important;
        height: 70px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 !important;
    }
    
    .valentine-button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 25px rgba(255, 51, 102, 0.5) !important;
        background: linear-gradient(135deg, #FF0066, #CC0052) !important;
    }
    
    /* No button - SAME SIZE as YES */
    .no-button {
        background: linear-gradient(135deg, #666666, #444444) !important;
        box-shadow: 0 6px 15px rgba(102, 102, 102, 0.3) !important;
    }
    
    .no-button:hover {
        background: linear-gradient(135deg, #555555, #333333) !important;
        box-shadow: 0 10px 25px rgba(68, 68, 68, 0.5) !important;
    }
    
    /* Center everything perfectly */
    .perfect-center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
        text-align: center;
        padding: 20px;
        width: 100%;
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
        width: 50px;
        height: 50px;
        font-size: 20px;
        cursor: pointer;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 10px rgba(210, 43, 105, 0.3);
    }
    
    .music-control:hover {
        transform: scale(1.1);
    }
    
    /* GIF container */
    .gif-container {
        margin: 30px 0;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        max-width: 500px;
    }
    
    /* Action buttons */
    .action-button {
        background: linear-gradient(135deg, #FFB6C1, #FF8BA0) !important;
        color: #8B0A50 !important;
        border: none !important;
        padding: 12px 30px !important;
        font-size: 1.4rem !important;
        border-radius: 25px !important;
        margin-top: 30px !important;
        font-weight: bold !important;
    }
    
    /* Make sure Streamlit columns are properly aligned */
    .stButton > button {
        width: 100% !important;
        margin: 0 !important;
    }
    
    /* Custom column styling for perfect alignment */
    .stColumn {
        display: flex;
        justify-content: center;
        align-items: center;
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
    # Landing page - Clean with NO "Open me" text
    st.markdown('<div class="perfect-center">', unsafe_allow_html=True)
    
    # Title
    st.markdown('<h1 class="main-title">For My Special Valentine 💝</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Click the envelope below...</p>', unsafe_allow_html=True)
    
    # Heart
    st.markdown('<div class="heartbeat">❤️</div>', unsafe_allow_html=True)
    
    # Interactive envelope - NO "Open me" text, just the envelope
    # The envelope itself is clickable
    st.markdown("""
    <div onclick="document.getElementById('openBtn').click();" style="cursor: pointer; display: inline-block;">
        <div class="checkered-envelope">
            <div class="envelope-icon">✉️</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hidden button - NO visible text
    if st.button("Open", key="openBtn", help=""):
        st.session_state.page = 'valentine'
        st.rerun()
    
    # Add spacing
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'valentine':
    # Valentine question page - Perfect alignment
    st.markdown('<div class="perfect-center">', unsafe_allow_html=True)
    
    # Question only - NO heart
    st.markdown('<div class="valentine-question">Will you be my valentine, again?</div>', 
                unsafe_allow_html=True)
    
    # PERFECTLY ALIGNED BUTTONS using custom container
    st.markdown('<div class="aligned-buttons">', unsafe_allow_html=True)
    
    # Create two equal columns
    col1, col2 = st.columns(2)
    
    with col1:
        # YES button with custom styling
        if st.button("YES 💖", key="yesBtn"):
            st.markdown("""
            <style>
            div[data-testid="stButton"] > button[kind="primary"] {
                background: linear-gradient(135deg, #FF3366, #FF0066) !important;
                color: white !important;
                padding: 18px 40px !important;
                font-size: 1.8rem !important;
                border-radius: 30px !important;
                min-width: 160px !important;
                height: 70px !important;
            }
            </style>
            """, unsafe_allow_html=True)
            st.session_state.response = 'yes'
            st.session_state.page = 'response'
            st.rerun()
    
    with col2:
        # NO button with custom styling
        st.markdown("""
        <style>
        div[data-testid="stButton"] > button[kind="secondary"] {
            background: linear-gradient(135deg, #666666, #444444) !important;
            color: white !important;
            padding: 18px 40px !important;
            font-size: 1.8rem !important;
            border-radius: 30px !important;
            min-width: 160px !important;
            height: 70px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        if st.button("NO", key="noBtn"):
            st.session_state.response = 'no'
            st.session_state.page = 'response'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Back button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back", key="backBtn"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'response':
    # Response page
    st.markdown('<div class="perfect-center">', unsafe_allow_html=True)
    
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
        
        # Text (no quotes)
        st.markdown('<div class="response-text" style="color: #666;">Oh...</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="response-text" style="color: #666;">You missed your chance</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="response-text" style="color: #666;">Better luck next time!</div>', 
                   unsafe_allow_html=True)
    
    # Restart button
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Start Over ✨", key="restartBtn"):
        st.session_state.page = 'landing'
        st.session_state.response = None
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
