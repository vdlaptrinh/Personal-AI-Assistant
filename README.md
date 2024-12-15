# Final Project - Trợ lý ảo cá nhân trên Raspberry Pi
This project is an implementation of a voice-based AI assistant using OpenAI's google Gemini on a Raspberry Pi. The assistant listens for the wake word "Hey Siri" and then processes the user's query, providing an appropriate response.

## Features
- Wake word detection using Porcupine
- Speech recognition with Google Speech Recognition
- AI-based chat using Google Gemini
- Text-to-Speech using edge_tts
- Open music
...

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

## Sample Output
....

This project uses code from https://github.com/ivan00105/Voice-Based-AI-Assistant-with-ChatGPT-on-Raspberry-Pi
