import speech_recognition as sr

rec = sr.Recognizer()
rec.energy_threshold = 400 



def recognize_speech():
    # Use the microphone as source for input (specify the microphone index)
    with sr.Microphone() as source:  
        # Adjusting for ambient noise
        rec.adjust_for_ambient_noise(source, duration=1)      
        print("Listening...")
        audio = rec.listen(source, timeout=5)
 
        try:
            # Recognize speech using Google Web Speech API
            text = rec.recognize_google(audio, language="vi-VN")
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            return None
            

