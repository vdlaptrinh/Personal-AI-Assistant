import pvporcupine
import asyncio
import pyaudio
import struct
import sys
import os
import signal
import re
import json
import subprocess
import time
import RPi.GPIO as GPIO
from src.speech_to_text import recognize_speech
from src.text_to_speech import text_to_speech
from src.config import porcupine_access_key
from src.config import gemini_key
from src.yt_dlp_play_m3u8 import play_m3u8
#from src.pixels import Pixels
from src.lich_lam_viec import lich_lam_viec
from src.doc_truyen import doc_truyen
from src.loi_chuc_tet import chuc_tet
import google.generativeai as genai

# Cấu hình GPIO cho nút nhấn
#BUTTON_INCREASE = 5  # GPIO pin cho nút tăng âm lượng
#BUTTON_DECREASE = 25  # GPIO pin cho nút giảm âm lượng
BUTTON_WAKEUP = 17  # GPIO pin cho nút WAKEUP

GPIO.setmode(GPIO.BCM)
#GPIO.setup(BUTTON_INCREASE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(BUTTON_DECREASE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_WAKEUP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(BUTTON_WAKEUP, GPIO.IN)

# Cấu hình Generative AI
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel("gemini-1.5-flash")

interrupted = False

# Đọc tệp JSON chứa từ khóa
files = ['object.json']
data = {}
for file in files:
    with open('/home/pi/Personal-AI-Assistant/object.json') as json_file:
        data[file] = json.load(json_file)
obj_data = data.get('object.json', {})

obj_music = [p['value'] for p in obj_data['music']]
obj_work_calendar = [p['value'] for p in obj_data['work_calendar']]
obj_truyen_vui = [p['value'] for p in obj_data['truyen_vui']]
obj_chuc_tet = [p['value'] for p in obj_data['chuc_tet']]


# Hàm xử lý tín hiệu ngắt
def signal_handler(signal, frame):
    global interrupted
    interrupted = True


# Hàm điều chỉnh âm lượng
def change_volume(action):
    if action == "increase":
        #print("Tăng âm lượng")
        #subprocess.run(["amixer", "sset", "Master", "10%+"])
        subprocess.run(["amixer", "sset", "Playback", "5%+"])
        
    elif action == "decrease":
        #print("Giảm âm lượng")
        #subprocess.run(["amixer", "sset", "Master", "10%-"])
        subprocess.run(["amixer", "sset", "Playback", "5%-"])
        


# Hàm sinh phản hồi từ Generative AI
def generate_ai_response(query):
    response = model.generate_content(query)
    return response.text


def split_into_chunks(text):
    data = []
    if text:
        words = text.split()
        for i in range(len(words) - 1):
            data.append(" ".join(words[i:i+2]))
            if i + 2 < len(words):
                data.append(" ".join(words[i:i+3]))
    return data

def extract_song_name(text):
    match = re.search(r"(mở nhạc|mở bài hát)\s+(.*)", text, re.IGNORECASE)
    if match:
        return match.group(2).strip()
    return None
    

# Hàm xử lý khi nút nhấn WAKEUP
def wakeup_callback(channel):
    #print("Nút Wakeup được nhấn!")
    #GPIO.cleanup()
    #change_volume("decrease")
    #asyncio.run(wake_up_detect())
    tts_process_stt()

# Cấu hình ngắt ngoài
#GPIO.add_event_detect(BUTTON_INCREASE, GPIO.RISING, callback=increase_volume_callback, bouncetime=300)
#GPIO.add_event_detect(BUTTON_DECREASE, GPIO.RISING, callback=decrease_volume_callback, bouncetime=300)
#if not GPIO.event_detected(BUTTON_WAKEUP):
#    GPIO.remove_event_detect(BUTTON_WAKEUP)
GPIO.add_event_detect(BUTTON_WAKEUP, GPIO.RISING, callback=wakeup_callback, bouncetime=300)


def interrupt_callback():
    global interrupted
    return interrupted

def tts_process_stt():
    #Pixels().wakeup()
    os.system(f"aplay /home/pi/Personal-AI-Assistant/wake_up_sound.wav")
    #print("Hey Siri detected! Recognizing speech...")
    query = recognize_speech()

    data = split_into_chunks(query)
    answer_text = 'Không có câu trả lời cho tình huống này'

    try:
        if any(item in data for item in obj_music):
            song_name = extract_song_name(query)
            play_m3u8(song_name)

        elif any(item in data for item in obj_work_calendar):
            #print("calendar")
            lich_lam_viec(query)
            
        elif any(item in data for item in obj_truyen_vui):
            doc_truyen()
            
        elif any(item in data for item in obj_chuc_tet):
            chuc_tet(query)

        else:
            gemini_result = generate_ai_response(query)
            print("GPT:", gemini_result)
            text_to_speech(gemini_result, "vi")

    except Exception as e:
        print(f"Lỗi xử lý: {e}")
        answer_text = 'Không nhận dạng được câu lệnh'
        text_to_speech(answer_text, "vi")
    #Pixels().off()

# Chương trình chính
async def wake_up_detect():
    #signal.signal(signal.SIGINT, signal_handler)

    keyword_path = "/home/pi/Personal-AI-Assistant/models/hey_siri_raspberry-pi.ppn"

    porcupine = None
    audio_stream = None
    pa = None

    try:
        porcupine = pvporcupine.create(access_key=porcupine_access_key, keyword_paths=[keyword_path])
        
        pa = pyaudio.PyAudio()
        

        print("Danh sách các thiết bị âm thanh khả dụng:\n")
        for i in range(pa.get_device_count()):
            device_info = pa.get_device_info_by_index(i)
            print(f"ID: {i}, Tên: {device_info['name']}, Loại: {device_info['maxInputChannels']} kênh đầu vào")
            
        
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            #output_device_index=None,
            #input_device_index=0
            frames_per_buffer=512
        )

        print("Listening for 'Hey Siri'...")
        #text_to_speech("Xin chào, mời bạn ra khẩu lệnh.", "vi", "output_file.mp3")
        text_to_speech("Xin chào, mời bạn ra khẩu lệnh.", "vi")
        # Chạy vòng lặp phát hiện từ khóa và kiểm tra nút nhấn song song
        await asyncio.gather(
            #check_buttons(),
            detect_keywords(porcupine, audio_stream)
        )

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()
        GPIO.cleanup()


# Phát hiện từ khóa "Hey Siri"
async def detect_keywords(porcupine, audio_stream):
    while not interrupt_callback():
        pcm = audio_stream.read(512, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * 512, pcm)
        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            tts_process_stt()


# Khởi động chương trình
if __name__ == "__main__":
    asyncio.run(wake_up_detect())
