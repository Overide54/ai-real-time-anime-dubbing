from gtts import gTTS

def text_to_speech(text):

    tts = gTTS(
        text=text,
        lang="en"
    )

    output_file = "outputs/english_audio.mp3"

    tts.save(output_file)

    return output_file