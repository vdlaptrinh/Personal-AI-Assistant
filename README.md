# Final Project - Trợ lý ảo cá nhân trên Raspberry Pi
This project is an implementation of a voice-based AI assistant using Google Gemini on a Raspberry Pi. The assistant listens for the wake word "Hey Siri" and then processes the user's query, providing an appropriate response.

## Features
- Wake word detection using Porcupine
- Speech recognition with Google Speech Recognition
- AI-based chat using Google Gemini
- Text-to-Speech using edge_tts
- Open music
...
## Hardware
Create a voice AI assistant using a Raspberry Pi 4, a ReSpeaker 2Mic HAT and Speaker.
This tutorial should work for almost any Raspberry Pi and USB microphone. Audio enhancements and local wake word detection may require a 64-bit operating system, however.
https://wiki.keyestudio.com/Ks0314_keyestudio_ReSpeaker_2-Mic_Pi_HAT_V1.0

https://www.raspberrypi.com/products/raspberry-pi-4-model-b/
https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/
Project này cũng có thể dùng Raspberry Pi zero 2W, mạch AIO (2 mic, 4 button, 12 led) và cụm loa xiaodu https://www.youtube.com/shorts/2xxbX977_Ls

## Install OS
Follow instructions to install Raspberry Pi OS. Under "Choose OS", pick "Raspberry Pi OS (other)" and "Raspberry Pi OS (64-bit) Lite".

When asking if you'd like to apply customization settings, choose "Edit Settings" and:

Set a username/password
Configure the wireless LAN
Under the Services tab, enable SSH and use password authentication

## Install Software
After flashing and booting the OS, connect to it over SSH using the username/password you configured during flashing.

## WM8960 Audio HAT
BUTTON	P17	Custom buttons
Install Driver
Update system:
```bash
sudo apt-get update
sudo apt-get upgrade
```
Clone driver:
```bash
git clone https://github.com/waveshare/WM8960-Audio-HAT
```
Install WM8960 driver:
```bash
cd WM8960-Audio-HAT
sudo ./install.sh 
sudo reboot
```
Check if the driver is installed.
```bash
sudo dkms status
```
pi@raspberrypi:~ $ sudo dkms status 
wm8960-soundcard, 1.0, 4.19.58-v7l+, armv7l: installed


## Installation
1. Clone the repository
```bash
git clone https://github.com/vdlaptrinh/Personal-AI-Assistant.git
cd Personal-AI-Assistant
```
2. Update and install your Raspberry Pi packages:
```bash
sudo apt-get update
sudo apt-get upgrade
...
```
3. Set up a virtual environment and activate it
```bash
...
```
4. Install the required packages
```bash
...
```

## Configuration
Before running the project, you need to edit a `config.py` file in the `src` directory with your API keys. 
### Google Gemini
Refer to https://ai.google.dev/gemini-api/docs?hl=vi
### PicoVoice Access Key
Get your PicoVoice access key from the [PicoVoice Console](https://picovoice.ai/ "PicoVoice Console"). Add the access key to the `config.py` file.
### Audio setup
Refer to https://www.youtube.com/watch?v=vEMzN5RgXbw&ab_channel=AssemblyAI

## Usage
1. Run the main script:
```bash
python main.py
```
2. The assistant will listen for the wake word "Hey Siri". Once detected, it will prompt you to speak your query.

3. The assistant will process your query using Gemini and provide an appropriate response.

4. Mở bài hát + tên bài hát

5. Lịch làm việc + [thứ x]: x là thứ trong tuần

## Auto Run: https://github.com/vdlaptrinh/Personal-AI-Assistant/blob/main/autorun_ai_assistant.txt


## Sample Output
https://www.youtube.com/shorts/zOJwcwMTKwQ
....

Tham khảo: https://github.com/ivan00105/Voice-Based-AI-Assistant-with-ChatGPT-on-Raspberry-Pi
