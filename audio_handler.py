import base64
import streamlit as st

def get_audio_html(file_path: str) -> str:
    """
    Generate HTML for autoplaying background music
    Returns HTML string with embedded audio
    """
    try:
        # Read and encode the audio file
        with open(file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
        
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        
        # HTML with JavaScript for audio playback
        audio_html = f'''
        <audio id="backgroundMusic" loop>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        
        <script>
            // Function to play audio
            function playAudio() {{
                var audio = document.getElementById('backgroundMusic');
                if (audio) {{
                    audio.volume = 0.7; // Set volume to 70%
                    audio.play().then(() => {{
                        console.log('Audio playing successfully');
                    }}).catch(error => {{
                        console.log('Audio play failed:', error);
                        // Try again on user interaction
                        document.addEventListener('click', function playOnClick() {{
                            audio.play();
                            document.removeEventListener('click', playOnClick);
                        }}, {{once: true}});
                    }});
                }}
            }}
            
            // Try to play when page loads
            window.addEventListener('load', playAudio);
            
            // Also try on any Streamlit event
            document.addEventListener('DOMContentLoaded', playAudio);
        </script>
        '''
        return audio_html
        
    except FileNotFoundError:
        st.error(f"Audio file '{file_path}' not found.")
        return ""
    except Exception as e:
        st.error(f"Error loading audio: {str(e)}")
        return ""
