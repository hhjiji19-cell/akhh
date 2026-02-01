import streamlit as st
import base64
from pathlib import Path
from streamlit_autoplay_audio import autoplay_audio

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
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'response' not in st.session_state:
    st.session_state.response = None

# Apply custom CSS
local_css()

# Main app logic
if st.session_state.page == 'landing':
    # Play background music
    try:
        autoplay_audio("music.mp3")
    except:
        st.warning("Could not play music. Make sure music.mp3 is in the same directory.")
    
    # Landing page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        # Big red throbbing heart
        st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
        
        # Floating envelope
        st.markdown(
            '<div class="floating-envelope" onclick="document.querySelector(\'[data-testid=stButton]\').click()">✉️</div>',
            unsafe_allow_html=True
        )
        
        # Hidden button to trigger envelope click
        if st.button("Click the envelope above!", key="envelope_trigger", help=""):
            st.session_state.page = 'valentine'
            st.rerun()
            
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
            if st.button("YES ❤️", key="yes_button", use_container_width=True):
                st.session_state.response = 'yes'
                st.session_state.page = 'response'
                st.rerun()
        
        with col_no:
            if st.button("NO", key="no_button", use_container_width=True):
                st.markdown('<div class="no-button">', unsafe_allow_html=True)
                st.session_state.response = 'no'
                st.session_state.page = 'response'
                st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'response':
    # Response page
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        
        if st.session_state.response == 'yes':
            # YES response
            st.markdown("### You gonna have more of me now!")
            st.markdown("### I love you gullu pullu ❤️")
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12afltvVzJIesM/giphy.gif", 
                    use_column_width=True)
            
            # Confetti effect
            st.balloons()
            
        else:
            # NO response
            st.markdown('<div class="throbbing-heart" style="color: #666;">❤️</div>', unsafe_allow_html=True)
            st.markdown("## Oh")
            st.markdown("## You missed your chance")
            st.markdown("## Better luck next time!")
            st.markdown("---")
            st.markdown("*The heart still throbs, waiting for you...*")
        
        # Button to go back
        if st.button("Back to Beginning", key="back_button"):
            st.session_state.page = 'landing'
            st.session_state.response = None
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
