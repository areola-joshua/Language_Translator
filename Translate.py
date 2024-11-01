import streamlit as st
from langdetect import detect
from googletrans import Translator

# Set page configuration to full screen
st.set_page_config(page_title="Language Detector & Translator", layout="wide")

# Title and description
st.title("🌍 Language Detector & Translator")
st.write("Enter any text, and this app will detect the language and translate it into the language of your choice.")

# Input text from user
text = st.text_area("Enter text here", placeholder="Type your text here...", height=200)

# Target language selection
target_lang = st.selectbox(
    "Select target language for translation", 
    ["es", "fr", "de", "zh-cn", "ja", "ru", "it", "ar", "ko"],  # List popular language codes
    index=0
)

# Detect and Translate Function
def detect_and_translate(text, target_lang):
    # Detect language
    result_lang = detect(text)
    
    # Translate language
    translator = Translator()
    translate_text = translator.translate(text, dest=target_lang).text

    return result_lang, translate_text

# Button to trigger translation
if st.button("Translate Text"):
    if text:
        # Detect and translate
        result_lang, translate_text = detect_and_translate(text, target_lang)
        
        # Display results
        st.subheader("Detected Language:")
        st.write(result_lang)
        
        st.subheader("Translated Text:")
        st.write(translate_text)
        
        # Celebrate with balloons
        st.balloons()
    else:
        st.warning("Please enter some text to translate.")
