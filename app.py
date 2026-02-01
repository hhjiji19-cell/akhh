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
    /* Baby pink background */
    .stApp {
        background-color: #FFE6E6 !important;
        background-image: linear-gradient(45deg, #ffb6c1 25%, transparent 25%),
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
    
    /* Floating envelope animation that moves around */
    @keyframes floatAround {
        0% { 
            transform: translate(0px, 0px) rotate(0deg);
        }
        25% { 
            transform: translate(150px, -80px) rotate(8deg);
        }
        50% { 
            transform: translate(-120px, 60px) rotate(-8deg);
        }
        75% { 
            transform: translate(80px, -40px) rotate(5deg);
        }
        100% { 
            transform: translate(0px, 0px) rotate(0deg);
        }
    }
    
    .floating-envelope {
        animation: floatAround 20s ease-in-out infinite;
        cursor: pointer;
        text-align: center;
        font-size: 10rem;
        margin: 40px 0;
        position: relative;
        transition: all 0.3s ease;
        filter: drop-shadow(0 10px 20px rgba(0,0,0,0.3));
    }
    
    .floating-envelope:hover {
        transform: scale(1.4);
        animation-play-state: paused;
        filter: drop-shadow(0 15px 30px rgba(0,0,0,0.4));
    }
    
    /* Envelope text */
    .envelope-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, 80px);
        color: #D81B60;
        font-weight: bold;
        font-size: 2rem;
        white-space: nowrap;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.9);
        font-family: 'Comic Sans MS', cursive, sans-serif;
        background: rgba(255, 255, 255, 0.8);
        padding: 5px 15px;
        border-radius: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Heart with text inside - DARK PINK TEXT in BIG letters */
    .heart-container {
        position: relative;
        display: inline-block;
        text-align: center;
    }
    
    .heart-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #C2185B !important;  /* Dark pink */
        font-weight: bold;
        font-size: 3.5rem !important;  /* BIG letters */
        text-shadow: 3px 3px 6px rgba(255,255,255,0.9);
        width: 90%;
        line-height: 1.3;
        font-family: 'Brush Script MT', cursive;
        text-align: center;
    }
    
    /* Response text for YES - BIG */
    .yes-response-text {
        color: #C2185B !important;
        font-size: 3rem !important;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.9);
        font-family: 'Brush Script MT', cursive;
        text-align: center;
        margin: 20px 0;
    }
    
    /* Response text for NO */
    .no-response-text {
        color: #C2185B !important;
        font-size: 2.5rem;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.9);
        font-family: 'Comic Sans MS', cursive;
        text-align: center;
        margin: 15px 0;
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
    
    /* No button specific styling */
    .no-button > button {
        background-color: #666666 !important;
        box-shadow: 0 6px 12px rgba(102, 102, 102, 0.3);
    }
    
    .no-button > button:hover {
        background-color: #444444 !important;
        box-shadow: 0 8px 20px rgba(68, 68, 68, 0.5);
    }
    
    /* Center content */
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 80vh;
        position: relative;
    }
    
    /* Title styling - DARK PINK */
    .title {
        color: #C2185B !important;  /* Dark pink */
        font-size: 4rem;
        margin-bottom: 30px;
        text-shadow: 3px 3px 6px rgba(255,255,255,0.9);
        font-family: 'Brush Script MT', cursive;
    }
    
    /* Hide audio player and Streamlit default elements */
    audio {
        display: none !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Music play button */
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
    
    .music-play-button:hover {
        background: #FF2222;
        transform: scale(1.1);
    }
    
    /* Make sure all text in the app is dark pink */
    h1, h2, h3, h4, h5, h6, p, div, span {
        color: #C2185B !important;
    }
    
    /* GIF container */
    .gif-container {
        margin: 30px 0;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

def autoplay_audio():
    """Create reliable audio autoplay with visible control"""
    try:
        # Read and encode the audio file
        with open("music.mp3", "rb") as f:
            audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
        
        # Create audio element with multiple play attempts
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
                                console.log("Music playing automatically");
                                isPlaying = true;
                                musicButton.innerHTML = '🔊';
                                musicButton.style.background = '#4CAF50';
                            }})
                            .catch(error => {{
                                console.log("Autoplay prevented");
                                musicButton.innerHTML = '▶️';
                                musicButton.style.background = '#FF4444';
                                // Show instruction
                                musicButton.title = "Click to play music";
                            }});
                    }}
                }}
            }}
            
            // Multiple attempts to play
            window.addEventListener('load', playMusic);
            setTimeout(playMusic, 500);
            setTimeout(playMusic, 1500);
            
            // Play on any click
            document.addEventListener('click', function() {{
                if (!isPlaying) {{
                    playMusic();
                }}
            }}, {{once: true}});
            
            // Ensure button is always visible
            musicButton.style.display = 'flex';
        </script>
        """
        return audio_html
    except Exception as e:
        return f"<!-- Audio error: {str(e)} -->"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'response' not in st.session_state:
    st.session_state.response = None

# Apply custom CSS
local_css()

# Add background music - THIS WILL PLAY
st.markdown(autoplay_audio(), unsafe_allow_html=True)

# Main app logic
if st.session_state.page == 'landing':
    # Landing page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Title with dark pink color
        st.markdown('<h1 class="title">For My Valentine ❤️</h1>', unsafe_allow_html=True)
        
        # Big red throbbing heart
        st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
        
        # Interactive floating envelope with "Open me" text
        st.markdown("""
        <div onclick="document.querySelector('button[key=\"envelope_trigger\"]').click()" 
             style="position: relative; display: inline-block; cursor: pointer;">
            <div class="floating-envelope">✉️</div>
            <div class="envelope-text">Open me!</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden button that gets triggered when envelope is clicked
        if st.button(" ", key="envelope_trigger", help="Click the envelope above!"):
            st.session_state.page = 'valentine'
            st.rerun()
        
        # Add some spacing
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'valentine':
    # Valentine question page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Heart with text inside - DARK PINK TEXT in BIG letters
        st.markdown('''
        <div class="heart-container">
            <div class="throbbing-heart">❤️</div>
            <div class="heart-text">Will you be my valentine, again?</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Create two columns for buttons
        col_yes, col_no = st.columns(2)
        
        with col_yes:
            if st.button("YES ❤️", key="yes_button", use_container_width=True, type="primary"):
                st.session_state.response = 'yes'
                st.session_state.page = 'response'
                st.rerun()
        
        with col_no:
            if st.button("NO 💔", key="no_button", use_container_width=True):
                st.session_state.response = 'no'
                st.session_state.page = 'response'
                st.rerun()
        
        # Back button (small and subtle)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back", key="back_from_valentine"):
            st.session_state.page = 'landing'
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'response':
    # Response page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        if st.session_state.response == 'yes':
            # YES response - BIG THROBBING HEART with text
            st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
            
            # Display the GIF
            st.markdown('<div class="gif-container">', unsafe_allow_html=True)
            st.image(
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif",
                use_column_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Text below GIF - Fixed format
            st.markdown('<div class="yes-response-text">You gonna have more of me now!</div>', 
                       unsafe_allow_html=True)
            st.markdown('<div class="yes-response-text">I love you gullu pullu 💖</div>', 
                       unsafe_allow_html=True)
            
            # Celebration effects
            st.balloons()
            st.snow()
            
        else:
            # NO response - Simple text without emojis in front
            st.markdown('<div class="throbbing-heart" style="color: #666; animation: throb 2s infinite;">💔</div>', 
                       unsafe_allow_html=True)
            
            # Text WITHOUT emojis in front - just the words
            st.markdown('<div class="no-response-text">Oh...</div>', unsafe_allow_html=True)
            st.markdown('<div class="no-response-text">You missed your chance</div>', unsafe_allow_html=True)
            st.markdown('<div class="no-response-text">Better luck next time!</div>', unsafe_allow_html=True)
            
            # Subtle rain effect
            st.markdown("""
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
                        pointer-events: none; z-index: -1; overflow: hidden; opacity: 0.3;">
                <style>
                    @keyframes rainFall {
                        0% { transform: translateY(-100px) translateX(0px); opacity: 0; }
                        10% { opacity: 0.5; }
                        90% { opacity: 0.5; }
                        100% { transform: translateY(100vh) translateX(20px); opacity: 0; }
                    }
                    .raindrop {
                        position: absolute;
                        width: 1px;
                        height: 40px;
                        background: linear-gradient(to bottom, transparent, #888888);
                        animation: rainFall 3s linear infinite;
                    }
                </style>
                <script>
                    // Create raindrops
                    const container = document.currentScript.parentElement;
                    for(let i=0; i<30; i++) {
                        const drop = document.createElement('div');
                        drop.className = 'raindrop';
                        drop.style.left = Math.random() * 100 + 'vw';
                        drop.style.animationDelay = Math.random() * 3 + 's';
                        container.appendChild(drop);
                    }
                </script>
            </div>
            """, unsafe_allow_html=True)
        
        # Button to go back
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("✨ Start Over ✨", key="back_button", use_container_width=True):
            st.session_state.page = 'landing'
            st.session_state.response = None
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)v
