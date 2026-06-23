from gtts import gTTS
import os

def text_to_speech(text):

    os.makedirs("outputs", exist_ok=True)

    output_file = "outputs/english_audio.mp3"

    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.save(output_file)

    return output_file