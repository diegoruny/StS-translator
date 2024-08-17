

import gradio as gr
import whisper
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs, VoiceSettings


# Load the API key from the .env file
config = dotenv_values(".env")
ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]

# Initialize the ElevenLabs client
client = ElevenLabs(
            api_key=ELEVENLABS_API_KEY,
        )

def transcriber(audio_file):
    # 1. Transcribe to text
    # Using openai whisper model
    # Alternative API online: assemblyai.com
    model = whisper.load_model("base")
    result = model.transcribe(audio_file, fp16=False)
    transcript = result["text"]
    return transcript

def translate_text(transcript):
    # Translate to text to english from different languages
    # using translate
    # Alternative API online: googletrans
    en_transcript = Translator(from_lang="",to_lang="en").translate(transcript)
    return en_transcript

def text_to_speech(en_transcript):
    # 3. Text to speech
    # using elevenlab's text to speech API
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=en_transcript,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Save the audio file
    save_file_path = "audio_files/en.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    return save_file_path

def translator(audio_file):

    
    try:
        transcript = transcriber(audio_file)
        translated_text = translate_text(transcript)
        audio_path_translated = text_to_speech(translated_text)
        return audio_path_translated
    except Exception as e:
        raise gr.Error(
            f"Error processing: {str(e)}")

# Create a Gradio interface
web = gr.Interface(
    fn= translator,
    inputs=gr.Audio(
        sources=["microphone", "upload"],
        type="filepath"
    ),
    outputs=[gr.Audio(label="Translated Audio")],
    title="Voice to Speech Translator",
    description="This is an AI powered app that can translate your voice to different languages."
)

# Launch the web interface
web.launch()
