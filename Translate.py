import streamlit as st
from langdetect import detect
from googletrans import Translator

# Function to detect and translate text
def detect_and_translate(text, target_lang):
    # Detect language
    result_lang = detect(text)
    
    # Translate language
    translator = Translator()
    translate_text = translator.translate(text, dest=target_lang).text

    return result_lang, translate_text

# Streamlit app layout
st.title("Language Detection and Translation App 🌎")
st.write("This app detects the language of your input text and translates it to the language of your choice.")

# Input text
text = st.text_area("Enter text to detect and translate", placeholder="Type or paste your text here...")

# Select target language
languages = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Chinese': 'zh-cn',
    'Arabic': 'ar', 'Russian': 'ru', 'Japanese': 'ja', 'Korean': 'ko', 'Hindi': 'hi'
}
target_lang = st.selectbox("Choose the target language", options=list(languages.keys()))

# Perform detection and translation when button is clicked
if st.button("Detect Language and Translate"):
    if text:
        result_lang, translated_text = detect_and_translate(text, languages[target_lang])
        st.write(f"**Detected Language:** {result_lang.capitalize()}")
        st.write(f"**Translated Text in {target_lang}:**")
        st.write(translated_text)
    else:
        st.error("Please enter some text for detection and translation.")

# Add a footer
st.markdown("---")
st.markdown("### About")
st.write("This app uses the `langdetect` library for language detection and `googletrans` for translation. Built with Streamlit.")
