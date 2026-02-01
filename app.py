import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Simple CSS - light and fast
def local_css():
    st.markdown("""
    <style>
    /* Simple baby pink background */
    .stApp {
        background-color: #FFE6E6 !important;
    }
    
    /* Big red throbbing heart animation */
    @keyframes throb {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    
    .throbbing-heart {
        animation: throb 1.5s infinite;
        color: #FF0000;
        text-align: center;
        font-size: 8rem;
        margin: 20px 0;
    }
    
    /* Simple floating envelope */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-30px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    
    .floating-envelope {
        animation: float 3s ease-in-out infinite;
        cursor: pointer;
        text-align: center;
        font-size: 8rem;
        margin: 30px 0;
        position: relative;
        transition: transform 0.3s;
    }
    
    .floating-envelope:hover {
        transform: scale(1.2);
    }
    
    .envelope-text {
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        color: #C2185B;
        font-weight: bold;
        font-size: 1.8rem;
        margin-top: 10px;
        white-space: nowrap;
        font-family: 'Comic Sans MS', cursive;
    }
    
    /* Valentine question - BIG dark pink text */
    .valentine-question {
        color: #C2185B !important;
        font-size: 3.5rem !important;
        text-align: center;
        margin: 40px 0;
        font-family: 'Brush Script MT', cursive;
        font-weight: bold;
    }
    
    /* Response text styling */
    .response-text {
        color: #C2185B !important;
        font-size: 2.5rem;
        text-align: center;
        margin: 20px 0;
        font-family: 'Comic Sans MS', cursive;
    }
    
    /* Buttons styling */
    .stButton > button {
        background-color: #FF4444;
        color: white;
        border: none;
        padding: 15px 30px;
        text-align: center;
        font-size: 20px;
        margin: 10px;
        border-radius: 25px;
        font-weight: bold;
        min-width: 150px;
    }
    
    .stButton > button:hover {
        background-color: #FF2222;
        transform: scale(1.05);
    }
    
    .no-button > button {
        background-color: #666666 !important;
    }
    
    .no-button > button:hover {
        background-color: #444444 !important;
    }
    
    /* Center content */
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
        text-align: center;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Music button */
    .music-btn {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #FF4444;
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
    }
    </style>
    """, unsafe_allow_html=True)

def setup_audio():
    """Simple audio setup"""
    try:
        with open("music.mp3", "rb") as f:
            audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
        
        audio_html = f"""
        <audio id="valentineMusic" loop style="display: none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        
        <button id="musicBtn" class="music-btn" onclick="toggleMusic()">🎵</button>
        
        <script>
            const audio = document.getElementById('valentineMusic');
            const btn = document.getElementById('musicBtn');
            let playing = false;
            
            function toggleMusic() {{
                if (playing) {{
                    audio.pause();
                    btn.innerHTML = '🎵';
                }} else {{
                    audio.volume = 0.5;
                    audio.play();
                    btn.innerHTML = '🔊';
                }}
                playing = !playing;
            }}
            
            // Try to play on load
            window.onload = function() {{
                audio.volume = 0.5;
                audio.play().then(() => {{
                    playing = true;
                    btn.innerHTML = '🔊';
                }}).catch(() => {{
                    btn.innerHTML = '▶️';
                }});
            }};
            
            // Play on any click
            document.addEventListener('click', function() {{
                if (!playing) {{
                    audio.play();
                    playing = true;
                    btn.innerHTML = '🔊';
                }}
            }}, {{once: true}});
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
    # Landing page
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    # Title
    st.markdown('<h1 style="color: #C2185B; font-size: 3rem; margin-bottom: 20px;">For My Valentine ❤️</h1>', 
                unsafe_allow_html=True)
    
    # Throbbing heart
    st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
    
    # Clickable envelope - FIXED
    st.markdown("""
    <div style="text-align: center; cursor: pointer;" onclick="document.getElementById('envelopeBtn').click();">
        <div class="floating-envelope">✉️</div>
        <div class="envelope-text">Open me!</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hidden button for envelope
    if st.button("Open Envelope", key="envelopeBtn", help="", type="primary"):
        st.session_state.page = 'valentine'
        st.rerun()
    
    # Add spacing at bottom
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'valentine':
    # Valentine question page - SIMPLE with just question and buttons
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    # Big dark pink question - NO throbbing heart here
    st.markdown('<div class="valentine-question">Will you be my valentine, again?</div>', 
                unsafe_allow_html=True)
    
    # Two buttons side by side
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("YES ❤️", key="yes_btn", use_container_width=True, type="primary"):
            st.session_state.response = 'yes'
            st.session_state.page = 'response'
            st.rerun()
    
    with col2:
        if st.button("NO", key="no_btn", use_container_width=True):
            st.session_state.response = 'no'
            st.session_state.page = 'response'
            st.rerun()
    
    # Simple back button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back", key="back_btn"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'response':
    # Response page
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    if st.session_state.response == 'yes':
        # YES response - shows heart, GIF, then text
        st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
        
        # GIF
        st.image(
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif",
            use_column_width=True
        )
        
        # Text
        st.markdown('<div class="response-text">You gonna have more of me now!</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="response-text">I love you gullu pullu 💖</div>', 
                   unsafe_allow_html=True)
        
        # Effects
        st.balloons()
        
    else:
        # NO response - simple text
        st.markdown('<div class="throbbing-heart" style="color: #666;">💔</div>', 
                   unsafe_allow_html=True)
        
        # Simple text (no emojis at start)
        st.markdown('<div class="response-text">Oh...</div>', unsafe_allow_html=True)
        st.markdown('<div class="response-text">You missed your chance</div>', unsafe_allow_html=True)
        st.markdown('<div class="response-text">Better luck next time!</div>', unsafe_allow_html=True)
    
    # Restart button
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Start Over", key="restart_btn", use_container_width=True):
        st.session_state.page = 'landing'
        st.session_state.response = None
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
