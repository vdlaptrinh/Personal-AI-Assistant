from gtts import gTTS
import os
import subprocess
from edge_tts import Communicate
from pydub import AudioSegment
voice = "vi-VN-HoaiMyNeural"

def text_to_speech(text, language, filename="output_file"):
    #tts = gTTS(text, lang=language)
    #tts.save(filename)
    communicate = Communicate(text=text, voice=voice)
    communicate.save_sync(filename)
    sound = AudioSegment.from_mp3(filename)  # convert MP3 to WAV
    sound.export(f"{filename}.wav", format="wav")
    os.remove(filename)
    #print(f"Saved TTS output to {filename}")
    #subprocess.call(["aplay", filename])
    #subprocess.Popen(["cvlc", "--play-and-exit", "--no-repeat", filename])
    subprocess.call(["aplay", "output_file.wav"])
    