import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
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
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
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
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# Apply custom CSS
local_css()

# ---------- DIRECT MUSIC AUTOPLAY ----------
# Load the music file directly
try:
    # Read the music file
    with open("music.mp3", "rb") as f:
        audio_bytes = f.read()
    
    # Encode to base64
    b64 = base64.b64encode(audio_bytes).decode()
    
    # Create HTML audio element with autoplay
    audio_html = f"""
    <audio id="valentineMusic" autoplay loop style="display: none;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    
    <script>
    // Get the audio element
    var audio = document.getElementById('valentineMusic');
    
    // Set volume
    audio.volume = 0.7;
    
    // Try to play immediately
    audio.play().catch(function(e) {{
        console.log("Autoplay failed initially:", e);
    }});
    
    // Play on any user interaction
    document.addEventListener('click', function playOnInteraction() {{
        if (audio.paused) {{
            audio.play();
        }}
        // Remove listener after first successful play
        document.removeEventListener('click', playOnInteraction);
    }});
    </script>
    """
    
    # Add the audio to the page
    st.markdown(audio_html, unsafe_allow_html=True)
    
except Exception as e:
    st.error(f"Could not load music.mp3: {e}")
    # Add fallback silent audio to avoid errors
    st.markdown("""
    <audio id="valentineMusic" style="display: none;"></audio>
    <script>
    console.log("Music file not found");
    </script>
    """, unsafe_allow_html=True)

# Main app logic
if st.session_state.page == 'landing':
    # Landing page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Big red throbbing heart
        st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
        
        # Envelope and button
        st.markdown("""
        <div class="envelope-container">
            <div class="envelope">✉️</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Button to open envelope
        if st.button("Click me to open the envelope", key="open_envelope"):
            st.session_state.page = 'question'
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'question':
    # Question page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
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
        if st.button("← Back", key="back_to_landing"):
            st.session_state.page = 'landing'
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'yes_response':
    # YES response page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Show the GIF
        st.markdown('<div class="gif-container">', unsafe_allow_html=True)
        st.image(
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif",
            use_column_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Text under GIF
        st.markdown('<div class="response-text">Another year of you tolerating me,<br><br>I love you so much gullu pullu ❤️</div>', 
                   unsafe_allow_html=True)
        
        # Celebration effects
        st.balloons()
        
        # Button to go back
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("✨ Start Over ✨", key="start_over_from_yes", use_container_width=True):
            st.session_state.page = 'landing'
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'no_response':
    # NO response page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
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
        
        st.markdown('</div>', unsafe_allow_html=True)

# Add a simple play button as last resort
st.markdown("""
<div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
    <button onclick="playValentineMusic()" style="
        background: #FF4444;
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 20px;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
    " title="Play music">▶️</button>
</div>

<script>
function playValentineMusic() {
    var audio = document.getElementById('valentineMusic');
    if (audio) {
        audio.play();
        // Change button to pause
        event.target.innerHTML = '⏸️';
        event.target.title = "Pause music";
        event.target.onclick = function() {
            audio.pause();
            this.innerHTML = '▶️';
            this.title = "Play music";
            this.onclick = playValentineMusic;
        };
    }
}

// Also try to play when user clicks ANY button
document.addEventListener('click', function(e) {
    if (e.target.tagName === 'BUTTON') {
        var audio = document.getElementById('valentineMusic');
        if (audio && audio.paused) {
            setTimeout(function() {
                audio.play();
            }, 100);
        }
    }
});
</script>
""", unsafe_allow_html=True)
