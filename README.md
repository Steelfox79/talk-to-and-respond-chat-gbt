This Python script creates a voice-powered AI chatbot that uses OpenAI's GPT-3 for natural language processing. The chatbot listens to your voice commands, converts them to text, and responds with text-to-speech audio.

Requirements
OpenAI Python SDK: You will need to set up your OpenAI API key.
ElevenLabs Python SDK: You will need to set up your ElevenLabs API key.
SpeechRecognition: Used for speech recognition.
Keyboard: Used for key press detection.
Getting Started
API Keys Setup:

Obtain an API key from [Openai](https://platform.openai.com/account/api-keys)..
Obtain an API key from [ElevenLabs](https://elevenlabs.io/)..
Install Dependencies:

you will need these packets to work
pip install openai speech_recognition keyboard elevenlabs
Configuration:

Set your OpenAI API key by replacing "openAI API" with your actual API key in the script.
Set your ElevenLabs API key using the set_api_key function from ElevenLabs.
set your voice by buting the name of voice. in the your "voice of choice" bit
Running the Chatbot:

Run the Python script.
Press the F3 key to start/stop recording.
Start speaking, and the chatbot will listen and respond accordingly.
Say "exit" to quit the chatbot.
Usage
Press F3 to initiate voice input.
Start speaking after the prompt.
The chatbot will listen to your voice, convert it to text, and generate an AI response using GPT-3.
The AI response is played back in your chosen voice.
Limitations
Requires an internet connection to access the OpenAI and ElevenLabs APIs.
Speech recognition accuracy may vary based on ambient noise and pronunciation.

Feel free to contribute to this project by creating issues, suggesting improvements
