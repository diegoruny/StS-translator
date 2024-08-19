# Audio to Speech Translator(EN)

AI-powered tool for seamless speech-to-text, translation, and speech synthesis. Built with modern NLP and text-to-speech technologies.

## Features

- **Transcription**: Converts audio to text using Whisper.
- **Translation**: Translates text to English.
- **Text-to-Speech**: Converts translated text to natural speech using ElevenLabs.
- **Gradio Interface**: Simple, intuitive UI.

## Getting Started

1. **Clone the Repo**
    ```bash
    git clone https://github.com/diegoruny/StS-translator
    cd StS-translator
    ```

2. **Install Dependencies**
    ```bash
    python -m venv .venv
    .venv\Scripts\Activate
    pip install -r requirements.txt
    ```

3. **Set Up API Key**
    - Create a `.env` file:
    ```
    ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
    ```

## Usage

1. **Run the App**
    ```bash
    python app.py
    ```

2. **Use the Interface**
    - Access the app at `http://127.0.0.1:7860/`.
    - Upload or record audio, receive translated speech.

## Tech Stack

- **Whisper** for transcription.
- **Translator** for language conversion.
- **ElevenLabs** for text-to-speech.
- **Gradio** for the user interface.

## Acnowledgements
*This project was inspired by a [YouTube](https://youtu.be/oxLvf2nDCvQ?si=6DjBbct7J5V0n8Od) based on a [post](https://blog.gopenai.com/create-a-simple-voice-to-voice-translation-app-with-python-83310c633a20) and has been extended and customized to enhance user experience and functionality.*


## License

MIT License. See `LICENSE` for details.
