import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title="My Valentine ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- CUSTOM CSS ----------
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

    /* Big red throbbing heart */
    @keyframes throb {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .throbbing-heart {
        animation: throb 1.5s infinite;
        color: #FF0000;
        font-size: 10rem;
        text-align: center;
        margin: 20px 0;
        filter: drop-shadow(0 0 10px rgba(255, 0, 0, 0.3));
    }

    /* Envelope bouncing animation */
    @keyframes bounce {
        0%, 100% { transform: translate(0,0) scale(1); }
        25% { transform: translate(30px,-20px) scale(1.1); }
        50% { transform: translate(-25px,30px) scale(1); }
        75% { transform: translate(20px,-15px) scale(1.1); }
    }
    .envelope {
        font-size: 8rem;
        cursor: pointer;
        animation: bounce 3s infinite ease-in-out;
        margin-bottom: 20px;
        filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2));
    }

    /* Question text */
    .question-text {
        color: #C2185B !important;
        font-size: 3.5rem;
        text-align: center;
        margin: 40px 0;
        font-family: 'Brush Script MT', cursive;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.9);
        line-height: 1.4;
    }

    /* Response text */
    .response-text {
        color: #C2185B !important;
        font-size: 2.5rem;
        text-align: center;
        margin: 30px 0;
        font-family: 'Brush Script MT', cursive;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.9);
        line-height: 1.4;
    }

    /* Centered layout */
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 80vh;
    }

    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* GIF container */
    .gif-container {
        margin: 30px 0;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        max-width: 400px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------- AUTOPLAY MUSIC ----------
def autoplay_music():
    try:
        with open("music.mp3", "rb") as f:
            audio_bytes = f.read()
            b64 = base64.b64encode(audio_bytes).decode()
        
        html = f"""
        <audio id="valentineMusic" autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
            const audio = document.getElementById('valentineMusic');
            audio.volume = 0.6;
            function forcePlay() {{
                const playPromise = audio.play();
                if (playPromise !== undefined) {{
                    playPromise.catch(() => {{
                        document.body.addEventListener('click', () => {{
                            audio.play();
                        }}, {{ once: true }});
                    }});
                }}
            }}
            window.addEventListener('load', forcePlay);
            setTimeout(forcePlay, 500);
        </script>
        """
        return html
    except:
        return ""

# ---------- SESSION STATE ----------
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# ---------- APPLY CSS AND MUSIC ----------
local_css()
st.markdown(autoplay_music(), unsafe_allow_html=True)

# ---------- APP LOGIC ----------
if st.session_state.page == 'landing':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.markdown('<div class="throbbing-heart">❤️</div>', unsafe_allow_html=True)
        st.markdown('<div class="envelope">✉️</div>', unsafe_allow_html=True)
        if st.button("Click me to open the envelope", key="open_envelope"):
            st.session_state.page = 'question'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'question':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.markdown('<div class="question-text">Will you be my valentine, again?</div>', unsafe_allow_html=True)

        col_yes, col_no = st.columns(2)
        with col_yes:
            if st.button("YES ❤️", key="yes_button", use_container_width=True):
                st.session_state.page = 'yes_response'
                st.rerun()
        with col_no:
            if st.button("NO 💔", key="no_button", use_container_width=True):
                st.session_state.page = 'no_response'
                st.rerun()
        
        if st.button("← Back", key="back_to_landing"):
            st.session_state.page = 'landing'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'yes_response':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.markdown('<div class="gif-container">', unsafe_allow_html=True)
        st.image(
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUxYmZiNmVyYmt2aTVlMHpxY3RnejRsa3M3dm9wNnAza2VwcTZtNSZlcD12MV9naWZzX3NlYXJjaCZjdT1n/12afltvVzJIesM/giphy.gif",
            use_column_width=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="response-text">Another year of you tolerating me,<br><br>I love you so much gullu pullu ❤️</div>', unsafe_allow_html=True)
        st.balloons()
        if st.button("✨ Start Over ✨", key="start_over_from_yes", use_container_width=True):
            st.session_state.page = 'landing'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'no_response':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.markdown('<div class="throbbing-heart" style="color:#666; animation:throb 2s infinite;">💔</div>', unsafe_allow_html=True)
        st.markdown('<div class="response-text">Oh,<br>You missed your chance 😌<br>Better luck next time!</div>', unsafe_allow_html=True)
        if st.button("✨ Start Over ✨", key="start_over_from_no", use_container_width=True):
            st.session_state.page = 'landing'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
