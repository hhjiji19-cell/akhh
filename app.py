import streamlit as st
import base64
import random

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
        font-size: 8rem;
        margin: 20px 0;
    }
    
    /* Floating envelope animation that moves around */
    @keyframes floatAround {
        0% { 
            transform: translate(0px, 0px) rotate(0deg);
        }
        25% { 
            transform: translate(100px, -50px) rotate(5deg);
        }
        50% { 
            transform: translate(-80px, 30px) rotate(-5deg);
        }
        75% { 
            transform: translate(50px, -30px) rotate(3deg);
        }
        100% { 
            transform: translate(0px, 0px) rotate(0deg);
        }
    }
    
    .floating-envelope {
        animation: floatAround 15s ease-in-out infinite;
        cursor: pointer;
        text-align: center;
        font-size: 8rem;
        margin: 40px 0;
        position: relative;
        transition: all 0.3s ease;
        filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2));
    }
    
    .floating-envelope:hover {
        transform: scale(1.3);
        animation-play-state: paused;
        filter: drop-shadow(0 10px 25px rgba(0,0,0,0.3));
    }
    
    /* Envelope text */
    .envelope-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, 50px);
        color: #D81B60;
        font-weight: bold;
        font-size: 1.5rem;
        white-space: nowrap;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    /* Heart with text inside - DARK PINK TEXT */
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
        font-size: 1.8rem;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
        width: 80%;
        line-height: 1.5;
        font-family: 'Brush Script MT', cursive;
    }
    
    /* Buttons styling */
    .stButton > button {
        background-color: #FF4444;
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        font-size: 18px;
        margin: 10px;
        border-radius: 25px;
        transition: all 0.3s;
        font-weight: bold;
        font-family: 'Arial Rounded MT Bold', sans-serif;
    }
    
    .stButton > button:hover {
        background-color: #FF2222;
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255, 68, 68, 0.4);
    }
    
    /* No button specific styling */
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
        text-align: center;
        min-height: 80vh;
        position: relative;
    }
    
    /* Title styling - DARK PINK */
    .title {
        color: #C2185B !important;  /* Dark pink */
        font-size: 3rem;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
        font-family: 'Brush Script MT', cursive;
    }
    
    /* Hide audio player and Streamlit default elements */
    audio {
        display: none !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Response text - DARK PINK */
    .response-text {
        color: #C2185B !important;
        font-size: 2rem;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
        font-family: 'Comic Sans MS', cursive;
    }
    
    /* Music player styling */
    .music-player {
        position: fixed;
        bottom: 10px;
        right: 10px;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

def autoplay_audio():
    """Create audio autoplay with multiple attempts"""
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
        
        <script>
            function playMusic() {{
                const audio = document.getElementById('valentineMusic');
                if (audio) {{
                    audio.volume = 0.7;
                    
                    // Try to play immediately
                    const playPromise = audio.play();
                    
                    if (playPromise !== undefined) {{
                        playPromise
                            .then(_ => console.log("Music playing automatically"))
                            .catch(error => {{
                                console.log("Autoplay prevented:", error);
                                // Show a play button that user can click
                                createPlayButton();
                            }});
                    }}
                }}
            }}
            
            function createPlayButton() {{
                const button = document.createElement('button');
                button.innerHTML = '🎵 Click to Play Music';
                button.style.position = 'fixed';
                button.style.bottom = '10px';
                button.style.right = '10px';
                button.style.zIndex = '1000';
                button.style.padding = '10px 15px';
                button.style.background = '#FF4444';
                button.style.color = 'white';
                button.style.border = 'none';
                button.style.borderRadius = '20px';
                button.style.cursor = 'pointer';
                button.onclick = function() {{
                    document.getElementById('valentineMusic').play();
                    button.remove();
                }};
                document.body.appendChild(button);
            }}
            
            // Try to play when page loads
            window.addEventListener('load', playMusic);
            
            // Also try when user interacts with the page
            document.addEventListener('click', function() {{
                const audio = document.getElementById('valentineMusic');
                if (audio && audio.paused) {{
                    audio.play();
                }}
            }});
            
            // Try after a short delay
            setTimeout(playMusic, 1000);
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

# Add background music
st.markdown(autoplay_audio(), unsafe_allow_html=True)

# Main app logic
if st.session_state.page == 'landing':
    # Landing page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Title with dark pink color
        st.markdown('<h1 class="title">For My Special Someone ❤️</h1>', unsafe_allow_html=True)
        
        # Big red throbbing heart
        st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
        
        # Interactive floating envelope with "Open me" text
        st.markdown("""
        <div style="position: relative; display: inline-block;">
            <div class="floating-envelope" id="envelope">✉️</div>
            <div class="envelope-text">Open me!</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden button that gets triggered when envelope is clicked
        # Using HTML to make the entire envelope area clickable
        st.markdown("""
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const envelope = document.querySelector('.floating-envelope');
                const parentDiv = envelope.closest('div[style*="position: relative"]');
                
                if (parentDiv) {
                    parentDiv.style.cursor = 'pointer';
                    parentDiv.addEventListener('click', function() {
                        // Find and click the Streamlit button
                        const buttons = document.querySelectorAll('button');
                        const envelopeButton = Array.from(buttons).find(btn => 
                            btn.textContent.includes('envelope') || 
                            btn.id.includes('envelope')
                        );
                        if (envelopeButton) {
                            envelopeButton.click();
                        }
                    });
                }
            });
        </script>
        """, unsafe_allow_html=True)
        
        # This button will be triggered when envelope is clicked
        if st.button("Open Envelope", key="envelope_trigger", help="Click the envelope above!"):
            st.session_state.page = 'valentine'
            st.rerun()
        
        # Add some spacing
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'valentine':
    # Valentine question page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Heart with text inside - DARK PINK TEXT
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
            # YES response - DARK PINK TEXT
            st.markdown('<div class="response-text">🎉 You gonna have more of me now! 🎉</div>', 
                       unsafe_allow_html=True)
            st.markdown('<div class="response-text">💖 I love you gullu pullu 💖</div>', 
                       unsafe_allow_html=True)
            
            # Display the GIF
            st.image(
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif",
                use_column_width=True
            )
            
            # Celebration effects
            st.balloons()
            st.snow()
            
        else:
            # NO response - DARK PINK TEXT
            st.markdown('<div class="throbbing-heart" style="color: #666; animation: throb 2s infinite;">💔</div>', 
                       unsafe_allow_html=True)
            st.markdown('<div class="response-text">😔 Oh...</div>', unsafe_allow_html=True)
            st.markdown('<div class="response-text">😢 You missed your chance</div>', unsafe_allow_html=True)
            st.markdown('<div class="response-text">🍀 Better luck next time!</div>', unsafe_allow_html=True)
            
            # Rain effect for sad mood
            st.markdown("""
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
                        pointer-events: none; z-index: -1; overflow: hidden;">
                <style>
                    @keyframes rainFall {
                        0% { transform: translateY(-100px) translateX(var(--start-x)); }
                        100% { transform: translateY(100vh) translateX(var(--end-x)); }
                    }
                    .raindrop {
                        position: absolute;
                        width: 2px;
                        height: 20px;
                        background: linear-gradient(to bottom, transparent, #888);
                        animation: rainFall 2s linear infinite;
                        opacity: 0.6;
                    }
                </style>
                <script>
                    for(let i=0; i<50; i++) {
                        const drop = document.createElement('div');
                        drop.className = 'raindrop';
                        drop.style.left = Math.random() * 100 + 'vw';
                        drop.style.setProperty('--start-x', (Math.random() * 40 - 20) + 'px');
                        drop.style.setProperty('--end-x', (Math.random() * 40 - 20) + 'px');
                        drop.style.animationDelay = Math.random() * 2 + 's';
                        document.currentScript.parentElement.appendChild(drop);
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
        
        st.markdown('</div>', unsafe_allow_html=True)
