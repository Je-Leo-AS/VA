import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    
    
# Loop infinitely for user to
# speak

def listen_():
    try:
        with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.)      
                return r.listen(source2)
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
        
    except sr.UnknownValueError:
        print("unknown error occurred")
        return None


def recognizer(audio2):
    try:
        # 'language' parameter set to auto-detect multiple languages
        MyText = r.recognize_google(audio2, language="pt-BR,en-US,es-ES,fr-FR,de-DE,it-IT,zh-CN")
        # Return recognized text in lowercase
        return MyText.lower()
    except sr.UnknownValueError:
        return "I could not understand what you said."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"



while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    audio2 = listen_()
    if  audio2:
    # use the microphone as source for input.
       
        print(f"Did you say : {recognizer(audio2)}")
        
    