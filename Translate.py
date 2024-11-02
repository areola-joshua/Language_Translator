import streamlit as st
from langdetect import detect
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS

# Set page configuration to full screen
st.set_page_config(page_title="Language Detector & Translator", layout="wide")

# Dictionary of languages with names and codes
languages = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 
    'Chinese (Simplified)': 'zh-cn', 'Chinese (Traditional)': 'zh-tw', 
    'Arabic': 'ar', 'Russian': 'ru', 'Japanese': 'ja', 'Korean': 'ko', 
    'Hindi': 'hi', 'Portuguese': 'pt', 'Italian': 'it', 'Dutch': 'nl', 
    'Turkish': 'tr', 'Vietnamese': 'vi', 'Thai': 'th', 'Swedish': 'sv', 
    'Norwegian': 'no', 'Danish': 'da', 'Finnish': 'fi','English': 'en',
    'Yoruba': 'yo', 'Igbo': 'ig', 'Hausa': 'ha'
}

# Reverse dictionary to map language codes to language names
reverse_languages = {code: name for name, code in languages.items()}

# Title and description
st.title("🌍 Language Detectors & Translator")
st.write("Enter any text, and this app will detect the language and translate it into the language of your choice.")

# Input text from user
text = st.text_area("Enter text here", placeholder="Type your text here...", height=200)

# Target language selection
target_lang_name = st.selectbox(
    "Select target language for translation", 
    list(languages.keys()),  # Display language names in dropdown
    index=1  # Default to Spanish for demonstration
)
target_lang_code = languages[target_lang_name]  # Get language code from the dictionary

# Detect and Translate Function
def detect_and_translate(text, target_lang_code):
    # Detect language
    result_lang_code = detect(text)
    
    # Translate language
    translator = Translator()
    translate_text = translator.translate(text, dest=target_lang_code).text

    return result_lang_code, translate_text

# Button to trigger translation
if st.button("Translate Text"):
    if text:
        # Detect and translate
        result_lang_code, translate_text = detect_and_translate(text, target_lang_code)
        
        # Get the detected language name or default to the selected target language
        detected_language_name = reverse_languages.get(result_lang_code, target_lang_name)
        
        # Create a decorated box for output
        st.markdown("""
            <style>
            .output-box {
                padding: 10px;
                border: 1px solid #4CAF50;
                border-radius: 5px;
                background-color: #000;
                margin-top: 10px;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True)

        # Display results in a decorated box
        st.markdown(f'<div class="output-box"><h4>Detected Language:</h4><p>{detected_language_name}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="output-box"><h4>Translated Text:</h4><p>{translate_text}</p></div>', unsafe_allow_html=True)

    else:
        st.warning("Please enter some text to translate.")

# Speech Recognition Section
st.header("🎤 Speech Recognition")
if st.button("Record Audio"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please say something:")
        audio = recognizer.listen(source)

    # Recognize speech using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio)
        st.success("You said: " + text)
    except sr.UnknownValueError:
        st.error("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")

# Text-to-Speech Section
if st.button("Convert Text to Speech"):
    if text:
        # Create a gTTS object
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Save the converted audio to a file
        audio_file = "output.mp3"
        tts.save(audio_file)
        
        st.success("Audio file has been created. You can play it below:")
        
        # Play the audio file directly in the app
        st.audio(audio_file)

    else:
        st.warning("Please enter text before converting to speech.")
