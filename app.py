# -*- coding: utf-8 -*-
import streamlit as st
import base64


# Page configuration
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS with all fixes
def local_css():
    st.markdown("""
    <style>
    /* Baby pink checkered background */
    .stApp {
        background-color: #FFE6E6 !important;
        background-image: 
            linear-gradient(45deg, #ffb6c1 25%, transparent 25%),
            linear-gradient(-45deg, #ffb6c1 25%, transparent 25%),
            linear-gradient(45deg, transparent 75%, #ffb6c1 75%),
            linear-gradient(-45deg, transparent 75%, #ffb6c1 75%);
        background-size: 20px 20px;
        background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
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
        font-size: 10rem;
        margin: 20px 0;
        filter: drop-shadow(0 0 10px rgba(255, 0, 0, 0.3));
    }
    
    /* Envelope styling */
    .envelope-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-top: 50px;
    }
    
    .envelope {
        font-size: 8rem;
        cursor: pointer;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
        filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2));
    }
    
    .envelope:hover {
        transform: scale(1.1);
    }
    
    /* Question text styling - DARK PINK */
    .question-text {
        color: #C2185B !important;
        font-size: 3.5rem;
        text-align: center;
        margin: 40px 0;
        font-family: 'Brush Script MT', cursive;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.9);
        line-height: 1.4;
    }
    
    /* Response text styling */
    .response-text {
        color: #C2185B !important;
        font-size: 2.5rem;
        text-align: center;
        margin: 30px 0;
        font-family: 'Brush Script MT', cursive;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.9);
        line-height: 1.4;
    }
    
    /* Buttons styling */
    .stButton > button {
        background-color: #FF4444;
        color: white;
        border: none;
        padding: 20px 40px;
        text-align: center;
        font-size: 22px;
        margin: 10px;
        border-radius: 30px;
        transition: all 0.3s;
        font-weight: bold;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        box-shadow: 0 6px 12px rgba(255, 68, 68, 0.3);
    }
    
    .stButton > button:hover {
        background-color: #FF2222;
        transform: scale(1.08);
        box-shadow: 0 8px 20px rgba(255, 68, 68, 0.5);
    }
    
    /* Center content - FIXED ALIGNMENT */
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 100vh;
        width: 100%;
        position: relative;
        padding: 20px;
    }
    
    /* Main container for perfect centering */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        gap: 30px;
    }
    
    /* Hide audio player and Streamlit default elements */
    audio {
        display: none !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Music button */
    .music-play-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #FF4444;
        color: white;
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 24px;
        cursor: pointer;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* GIF styling */
    .gif-container {
        margin: 30px 0;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        max-width: 400px;
    }
    
    /* Make sure all text is dark pink */
    h1, h2, h3, h4, h5, h6, p, div, span {
        color: #C2185B !important;
    }
    
    /* Streamlit column centering fix */
    .st-emotion-cache-1v0mbdj {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    
    /* Fix for column alignment */
    [data-testid="column"] {
        display: flex !important;
        justify-content: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

def autoplay_audio():
    """Create audio autoplay"""
    try:
        # Read and encode the audio file
        with open("music.mp3", "rb") as f:
            audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
        
        # Create audio element
        audio_html = f"""
        <audio id="valentineMusic" loop style="display: none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        
        <button id="musicButton" class="music-play-button" onclick="toggleMusic()">🎵</button>
        
        <script>
            const audio = document.getElementById('valentineMusic');
            const musicButton = document.getElementById('musicButton');
            let isPlaying = false;
            
            function toggleMusic() {{
                if (isPlaying) {{
                    audio.pause();
                    musicButton.innerHTML = '🎵';
                    musicButton.style.background = '#FF4444';
                }} else {{
                    audio.volume = 0.7;
                    audio.play();
                    musicButton.innerHTML = '🔊';
                    musicButton.style.background = '#4CAF50';
                }}
                isPlaying = !isPlaying;
            }}
            
            // Try to play automatically
            function playMusic() {{
                if (audio) {{
                    audio.volume = 0.7;
                    const playPromise = audio.play();
                    
                    if (playPromise !== undefined) {{
                        playPromise
                            .then(_ => {{
                                isPlaying = true;
                                musicButton.innerHTML = '🔊';
                                musicButton.style.background = '#4CAF50';
                            }})
                            .catch(error => {{
                                musicButton.innerHTML = '▶️';
                                musicButton.style.background = '#FF4444';
                                musicButton.title = "Click to play music";
                            }});
                    }}
                }}
            }}
            
            // Try to play on load
            window.addEventListener('load', playMusic);
            setTimeout(playMusic, 1000);
        </script>
        """
        return audio_html
    except Exception as e:
        return f"<!-- Audio error: {str(e)} -->"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# Apply custom CSS
local_css()

# Add background music
st.markdown(autoplay_audio(), unsafe_allow_html=True)

# Main app logic
if st.session_state.page == 'landing':
    # Landing page - Simplified layout for better alignment
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    # Container for everything
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Big red throbbing heart
    st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
    
    # Envelope
    st.markdown("""
    <div class="envelope-container">
        <div class="envelope">✉️</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Button to open envelope
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Click me to open the envelope", key="open_envelope", use_container_width=True):
            st.session_state.page = 'question'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container
    st.markdown('</div>', unsafe_allow_html=True)  # Close centered

elif st.session_state.page == 'question':
    # Question page
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    # Container for everything
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Question text
    st.markdown('<div class="question-text">Will you be my valentine, again?</div>', unsafe_allow_html=True)
    
    # Create two columns for buttons
    col_yes, col_no = st.columns(2)
    
    with col_yes:
        if st.button("YES ❤️", key="yes_button", use_container_width=True):
            st.session_state.page = 'yes_response'
            st.rerun()
    
    with col_no:
        if st.button("NO 💔", key="no_button", use_container_width=True):
            st.session_state.page = 'no_response'
            st.rerun()
    
    # Back button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back", key="back_to_landing", use_container_width=False):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container
    st.markdown('</div>', unsafe_allow_html=True)  # Close centered

elif st.session_state.page == 'yes_response':
    # YES response page
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    # Container for everything
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Show the GIF
    st.markdown('<div class="gif-container">', unsafe_allow_html=True)
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif",
        use_column_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Text under GIF
    st.markdown('<div class="response-text">Another year of you having to put up with me<br><br> I'm so glad i met you, and I am sooooooooooooooo glad that we are together<br><br>I love you so much gullu pullu❤️</div>', 
               unsafe_allow_html=True)
    
    # Celebration effects
    st.balloons()
    
    # Button to go back
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("✨ Start Over ✨", key="start_over_from_yes", use_container_width=True):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container
    st.markdown('</div>', unsafe_allow_html=True)  # Close centered

elif st.session_state.page == 'no_response':
    # NO response page
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    
    # Container for everything
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Broken heart
    st.markdown('<div class="throbbing-heart" style="color: #666; animation: throb 2s infinite;">💔</div>', 
               unsafe_allow_html=True)
    
    # Text
    st.markdown('<div class="response-text">Oh,<br>You missed your chance 😌<br>Better luck next time!</div>', 
               unsafe_allow_html=True)
    
    # Button to go back
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("✨ Start Over ✨", key="start_over_from_no", use_container_width=True):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container
    st.markdown('</div>', unsafe_allow_html=True)  # Close centered
