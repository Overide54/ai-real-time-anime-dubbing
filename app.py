from tts import text_to_speech
from speech import transcribe
from translator import translate
import streamlit as st
import os

st.set_page_config(
    page_title="AI Real-Time Anime Dubbing System",
    page_icon="🎌"
)

st.title("🎌 AI Real-Time Anime Dubbing System")

audio_file = st.file_uploader(
    "Upload Japanese Audio",
    type=["wav", "mp3"]
)

if audio_file:

    st.audio(audio_file)

    if st.button("Translate"):

        # Create uploads folder
        os.makedirs("uploads", exist_ok=True)

        # Save uploaded file
        filepath = os.path.join(
            "uploads",
            audio_file.name
        )

        with open(filepath, "wb") as f:
            f.write(audio_file.getbuffer())

        st.success("Audio Saved")

        # Speech to Text
        with st.spinner("Transcribing Japanese Audio..."):
            text = transcribe(filepath)

        # Translation
        with st.spinner("Translating to English..."):
            english_text = translate(text)

        # Display Results
                # Display Results
        st.subheader("Japanese Transcript")
        st.write(text)

        st.subheader("English Translation")
        st.write(english_text)

        # Generate English Audio
        audio_path = text_to_speech(english_text)

        st.subheader("English Audio")
        st.audio(audio_path)