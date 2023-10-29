import openai
import speech_recognition as sr
from elevenlabs import generate, play
import keyboard

# Set your OpenAI GPT-3 API key
openai.api_key = "openAI API"

# Set your ElevenLabs API key
from elevenlabs import set_api_key
set_api_key("Elevenlabs API")

# Function to generate speech and play it
def generate_and_play(text):
   voice = "your voice of choice"
   audio = generate(text, voice=voice)
   play(audio)

# Function to recognize speech and return text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Press F3 to start/stop recording...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Recognizing speech...")
        try:
            user_input = recognizer.recognize_google(audio)
            return user_input
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand your speech."
        except sr.RequestError as e:
            return f"Speech recognition request failed: {str(e)}"

while True:
    # Use F3 key to start/stop recording
    keyboard.wait('F3')
    
    if keyboard.is_pressed('F3'):
        print("You can start speaking now...")
        user_input = recognize_speech()
        print(f"You: {user_input}")

        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"You: {user_input}\nAI:",
            max_tokens=50
        )

        ai_response = response.choices[0].text
        print(f"AI: {ai_response}")
        generate_and_play(ai_response)