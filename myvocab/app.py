import pyttsx3
import google.generativeai as genai

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



genai.configure(api_key="AIzaSyD1DZ8e58jdVu2tpAxLGlzhyiq8IuOzjoE")
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("generate a word and it's meaning also give a simple sentence with that word")
print(response.text)  
speak(response.text)