import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Creative CSS with better background and alignments
def local_css():
    st.markdown("""
    <style>
    /* Creative baby pink background with soft hearts */
    .stApp {
        background-color: #FFE6E6 !important;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(255, 200, 200, 0.3) 0%, transparent 20%),
            radial-gradient(circle at 90% 80%, rgba(255, 200, 200, 0.3) 0%, transparent 20%),
            radial-gradient(circle at 50% 50%, rgba(255, 220, 220, 0.2) 0%, transparent 30%),
            radial-gradient(circle at 20% 70%, rgba(255, 180, 180, 0.2) 0%, transparent 25%),
            radial-gradient(circle at 80% 30%, rgba(255, 180, 180, 0.2) 0%, transparent 25%);
        background-attachment: fixed;
    }
    
    /* Glowing heart animation */
    @keyframes glowThrob {
        0% { 
            transform: scale(1); 
            filter: drop-shadow(0 0 5px rgba(255, 0, 0, 0.3));
        }
        50% { 
            transform: scale(1.2); 
            filter: drop-shadow(0 0 20px rgba(255, 0, 0, 0.6));
        }
        100% { 
            transform: scale(1); 
            filter: drop-shadow(0 0 5px rgba(255, 0, 0, 0.3));
        }
    }
    
    .glowing-heart {
        animation: glowThrob 2s infinite;
        color: #FF0000;
        text-align: center;
        font-size: 9rem;
        margin: 10px 0 30px 0;
    }
    
    /* Elegant floating envelope */
    @keyframes gentleFloat {
        0%, 100% { 
            transform: translateY(0) rotate(0deg);
            filter: drop-shadow(0 5px 15px rgba(210, 43, 105, 0.3));
        }
        33% { 
            transform: translateY(-15px) rotate(2deg);
            filter: drop-shadow(0 8px 20px rgba(210, 43, 105, 0.4));
        }
        66% { 
            transform: translateY(-8px) rotate(-1deg);
            filter: drop-shadow(0 6px 18px rgba(210, 43, 105, 0.35));
        }
    }
    
    .elegant-envelope {
        animation: gentleFloat 4s ease-in-out infinite;
        cursor: pointer;
        text-align: center;
        font-size: 7rem;
        margin: 30px 0 10px 0;
        position: relative;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        color: #D22B69;
    }
    
    .elegant-envelope:hover {
        transform: scale(1.25) rotate(5deg);
        animation-play-state: paused;
        filter: drop-shadow(0 12px 25px rgba(210, 43, 105, 0.5)) brightness(1.1);
    }
    
    /* Elegant envelope text with ribbon effect */
    .envelope-ribbon {
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg, #FF8BA0, #D22B69);
        color: white;
        font-weight: bold;
        font-size: 1.6rem;
        padding: 8px 25px;
        border-radius: 25px;
        white-space: nowrap;
        font-family: 'Georgia', serif;
        box-shadow: 0 4px 12px rgba(210, 43, 105, 0.25);
        margin-top: 15px;
        letter-spacing: 1px;
    }
    
    /* Valentine question - Elegant styling */
    .elegant-question {
        color: #8B0A50 !important;
        font-size: 3.8rem !important;
        text-align: center;
        margin: 50px 0 60px 0;
        font-family: 'Dancing Script', cursive;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.8);
        line-height: 1.2;
        padding: 0 20px;
    }
    
    /* Creative response text */
    .creative-response {
        color: #8B0A50 !important;
        font-size: 2.8rem;
        text-align: center;
        margin: 25px 0;
        font-family: 'Dancing Script', cursive;
        font-weight: 600;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.8);
    }
    
    /* Elegant buttons */
    .elegant-button {
        background: linear-gradient(135deg, #FF6B9D, #FF3366) !important;
        color: white !important;
        border: none !important;
        padding: 18px 45px !important;
        text-align: center !important;
        font-size: 1.8rem !important;
        margin: 15px !important;
        border-radius: 35px !important;
        font-weight: 600 !important;
        font-family: 'Segoe UI', sans-serif !important;
        box-shadow: 0 6px 15px rgba(255, 107, 157, 0.3) !important;
        transition: all 0.3s ease !important;
        min-width: 180px !important;
        letter-spacing: 0.5px !important;
    }
    
    .elegant-button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 10px 25px rgba(255, 107, 157, 0.5) !important;
        background: linear-gradient(135deg, #FF3366, #FF0066) !important;
    }
    
    /* No button styling */
    .no-button-style > button {
        background: linear-gradient(135deg, #888888, #666666) !important;
        box-shadow: 0 6px 15px rgba(102, 102, 102, 0.3) !important;
    }
    
    .no-button-style > button:hover {
        background: linear-gradient(135deg, #666666, #444444) !important;
        box-shadow: 0 10px 25px rgba(68, 68, 68, 0.5) !important;
    }
    
    /* Perfect center alignment */
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
    
    /* Main title */
    .main-title {
        color: #8B0A50 !important;
        font-size: 3.5rem;
        margin-bottom: 10px;
        font-family: 'Dancing Script', cursive;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9);
    }
    
    /* Subtitle */
    .subtitle {
        color: #D22B69 !important;
        font-size: 1.5rem;
        margin-bottom: 40px;
        font-family: 'Georgia', serif;
        font-style: italic;
    }
    
    /* Music control */
    .music-control {
        position: fixed;
        bottom: 25px;
        right: 25px;
        background: linear-gradient(135deg, #FF8BA0, #D22B69);
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
        box-shadow: 0 4px 12px rgba(210, 43, 105, 0.3);
        transition: all 0.3s;
    }
    
    .music-control:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 18px rgba(210, 43, 105, 0.4);
    }
    
    /* GIF container with border */
    .gif-frame {
        margin: 30px 0;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        border: 8px solid white;
        max-width: 500px;
    }
    
    /* Back/restart button */
    .action-button {
        background: linear-gradient(135deg, #FFB6C1, #FF8BA0) !important;
        color: #8B0A50 !important;
        border: none !important;
        padding: 12px 30px !important;
        font-size: 1.4rem !important;
        border-radius: 25px !important;
        margin-top: 20px !important;
        font-weight: 600 !important;
    }
    
    /* Container for buttons to ensure proper alignment */
    .button-container {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin: 30px 0;
        flex-wrap: wrap;
        width: 100%;
        max-width: 600px;
    }
    </style>
    """, unsafe_allow_html=True)

def setup_audio():
    """Audio setup with reliable playback"""
    try:
        with open("music.mp3", "rb") as f:
            audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
        
        audio_html = f"""
        <audio id="valentineMusic" loop style="display: none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        
        <button id="musicControl" class="music-control" onclick="toggleMusic()" title="Toggle Music">🎵</button>
        
        <script>
            const audio = document.getElementById('valentineMusic');
            const musicBtn = document.getElementById('musicControl');
            let isPlaying = false;
            
            function toggleMusic() {{
                if (isPlaying) {{
                    audio.pause();
                    musicBtn.innerHTML = '🎵';
                    musicBtn.style.background = 'linear-gradient(135deg, #FF8BA0, #D22B69)';
                }} else {{
                    audio.volume = 0.6;
                    audio.play();
                    musicBtn.innerHTML = '🔊';
                    musicBtn.style.background = 'linear-gradient(135deg, #4CAF50, #2E7D32)';
                }}
                isPlaying = !isPlaying;
            }}
            
            // Multiple attempts to play
            function tryPlay() {{
                audio.volume = 0.6;
                audio.play().then(() => {{
                    isPlaying = true;
                    musicBtn.innerHTML = '🔊';
                    musicBtn.style.background = 'linear-gradient(135deg, #4CAF50, #2E7D32)';
                }}).catch(e => {{
                    console.log('Auto-play prevented');
                }});
            }}
            
            window.addEventListener('load', tryPlay);
            setTimeout(tryPlay, 1000);
            
            // Play on first interaction
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
    # Landing page - Clean with ONE "Open me" button
    st.markdown('<div class="perfect-center">', unsafe_allow_html=True)
    
    # Main title
    st.markdown('<h1 class="main-title">My Dearest Valentine 💝</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">A special message awaits you...</p>', unsafe_allow_html=True)
    
    # Glowing heart
    st.markdown('<div class="glowing-heart">❤️</div>', unsafe_allow_html=True)
    
    # Interactive envelope - ONLY ONE "Open me" text
    # Using a container to make the entire area clickable
    envelope_container = st.container()
    with envelope_container:
        st.markdown("""
        <div onclick="document.querySelector('button[id=\"openEnvelope\"]').click();" 
             style="cursor: pointer; display: inline-block;">
            <div class="elegant-envelope">💌</div>
            <div class="envelope-ribbon">Open Me</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden button that gets clicked via JavaScript
        if st.button("Open Envelope", key="openEnvelope", type="primary", help=""):
            st.session_state.page = 'valentine'
            st.rerun()
    
    # Romantic quote at bottom
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p style="color: #D22B69; font-style: italic; font-size: 1.2rem;">"Love is not about how many days, months, or years you have been together. Love is about how much you love each other every single day."</p>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'valentine':
    # Valentine question page - Elegant and centered
    st.markdown('<div class="perfect-center">', unsafe_allow_html=True)
    
    # Elegant question - NO heart, just beautiful text
    st.markdown('<div class="elegant-question">Will you be my valentine, again?</div>', 
                unsafe_allow_html=True)
    
    # Button container for perfect alignment
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        # Use custom CSS class for YES button
        if st.button("YES 💖", key="yesValentine", use_container_width=True):
            st.session_state.response = 'yes'
            st.session_state.page = 'response'
            st.rerun()
    
    with col2:
        # Use custom CSS class for NO button
        st.markdown('<div class="no-button-style">', unsafe_allow_html=True)
        if st.button("NO", key="noValentine", use_container_width=True):
            st.session_state.response = 'no'
            st.session_state.page = 'response'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Simple back button
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("← Return", key="goBack", type="secondary"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'response':
    # Response page
    st.markdown('<div class="perfect-center">', unsafe_allow_html=True)
    
    if st.session_state.response == 'yes':
        # YES response - Romantic celebration
        st.markdown('<div class="glowing-heart">💖</div>', unsafe_allow_html=True)
        
        # GIF in fancy frame
        st.markdown('<div class="gif-frame">', unsafe_allow_html=True)
        st.image(
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif",
            use_column_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Romantic messages
        st.markdown('<div class="creative-response">You gonna have more of me now!</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="creative-response">I love you gullu pullu 💘</div>', 
                   unsafe_allow_html=True)
        
        # Celebration effects
        st.balloons()
        st.snow()
        
    else:
        # NO response - Elegant but sad
        st.markdown('<div class="glowing-heart" style="color: #888; filter: grayscale(0.5);">💔</div>', 
                   unsafe_allow_html=True)
        
        # Simple elegant text (no emojis at start)
        st.markdown('<div class="creative-response" style="color: #666;">Oh...</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="creative-response" style="color: #666;">You missed your chance</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="creative-response" style="color: #666;">Better luck next time!</div>', 
                   unsafe_allow_html=True)
        
        # Subtle sad message
        st.markdown('<p style="color: #999; font-style: italic; margin-top: 20px;">The heart remembers what the mind forgets...</p>', 
                   unsafe_allow_html=True)
    
    # Restart button
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Start New Journey ✨", key="restartJourney", use_container_width=True, type="primary"):
        st.session_state.page = 'landing'
        st.session_state.response = None
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
