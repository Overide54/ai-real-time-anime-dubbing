import time
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

        start_time = time.time()

        os.makedirs("uploads", exist_ok=True)

        filepath = os.path.join(
            "uploads",
            audio_file.name
        )

        with open(filepath, "wb") as f:
            f.write(audio_file.getbuffer())

        st.success("Audio Saved")

        with st.spinner("Transcribing Japanese Audio..."):
            text = transcribe(filepath)

        with st.spinner("Translating to English..."):
            english_text = translate(text)

        st.subheader("Japanese Transcript")
        st.write(text)

        st.subheader("English Translation")
        st.write(english_text)

        audio_path = text_to_speech(english_text)

        st.subheader("English Audio")
        st.audio(audio_path)

        with open(audio_path, "rb") as file:
            st.download_button(
                label="📥 Download English Audio",
                data=file,
                file_name="english_audio.mp3",
                mime="audio/mpeg"
            )

        end_time = time.time()

        st.success(
            f"Completed in {end_time - start_time:.2f} seconds"
        )