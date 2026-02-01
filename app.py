import streamlit as st
from pathlib import Path
from audio_handler import get_audio_html

# Page configuration
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for all the effects
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
    
    /* Floating envelope */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    
    .floating-envelope {
        animation: float 3s ease-in-out infinite;
        cursor: pointer;
        text-align: center;
        font-size: 6rem;
        margin: 40px 0;
        transition: all 0.3s ease;
    }
    
    .floating-envelope:hover {
        transform: scale(1.1);
        color: #FF4444;
    }
    
    /* Heart with text inside */
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
        color: white;
        font-weight: bold;
        font-size: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        width: 80%;
        line-height: 1.5;
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
    }
    
    /* Hide audio player and Streamlit default elements */
    audio {
        display: none !important;
    }
    
    .stAudio {
        display: none !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title styling */
    .title {
        color: #FF0000;
        font-size: 2.5rem;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'response' not in st.session_state:
    st.session_state.response = None
if 'music_played' not in st.session_state:
    st.session_state.music_played = False

# Apply custom CSS
local_css()

# Main app logic
if st.session_state.page == 'landing':
    # Landing page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Add background music - THIS IS THE INTEGRATION YOU ASKED FOR
        if Path("music.mp3").exists():
            audio_html = get_audio_html("music.mp3")
            st.markdown(audio_html, unsafe_allow_html=True)
        else:
            st.warning("music.mp3 file not found. Please add it to the same directory.")
        
        # Title
        st.markdown('<h1 class="title">For My Valentine ❤️</h1>', unsafe_allow_html=True)
        
        # Big red throbbing heart
        st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
        
        # Floating envelope
        st.markdown('<div class="floating-envelope">✉️</div>', unsafe_allow_html=True)
        
        # Instruction text
        st.markdown("### Click below to open the envelope!")
        
        # Button to open envelope
        if st.button("🎀 Open Envelope 🎀", key="envelope_trigger", 
                    use_container_width=True, type="primary"):
            st.session_state.page = 'valentine'
            st.rerun()
        
        # Music instructions
        st.markdown("---")
        st.markdown("*🎵 Music should play automatically. If not, click anywhere on the page.*")
            
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'valentine':
    # Valentine question page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Heart with text inside
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
            # Add custom class for no button
            st.markdown('<div class="no-button">', unsafe_allow_html=True)
            if st.button("NO 😢", key="no_button", use_container_width=True):
                st.session_state.response = 'no'
                st.session_state.page = 'response'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Back button
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Envelope", key="back_from_valentine"):
            st.session_state.page = 'landing'
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'response':
    # Response page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        if st.session_state.response == 'yes':
            # YES response
            st.markdown("## 🎉 You gonna have more of me now! 🎉")
            st.markdown("## 💖 I love you gullu pullu 💖")
            
            # Display the GIF
            st.image(
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif",
                use_column_width=True
            )
            
            # Celebration effects
            st.balloons()
            st.snow()
            
            # Additional romantic message
            st.markdown("---")
            st.markdown("### Every moment with you is special! ❤️")
            
        else:
            # NO response
            st.markdown('<div class="throbbing-heart" style="color: #666; animation: throb 2s infinite;">💔</div>', 
                       unsafe_allow_html=True)
            st.markdown("## 😔 Oh...")
            st.markdown("## 😢 You missed your chance")
            st.markdown("## 🍀 Better luck next time!")
            st.markdown("---")
            st.markdown("*💔 The heart still throbs, waiting for you...*")
            
            # Sad rain effect
            st.markdown("""
            <style>
            @keyframes rain {
                0% { transform: translateY(-100px); }
                100% { transform: translateY(100vh); }
            }
            </style>
            """, unsafe_allow_html=True)
        
        # Button to go back
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("✨ Start Over ✨", key="back_button", use_container_width=True):
            st.session_state.page = 'landing'
            st.session_state.response = None
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
