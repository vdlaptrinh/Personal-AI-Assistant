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
Create a voice AI assistant using a Raspberry Pi 4 or zero 2W, a ReSpeaker 2Mic HAT and Speaker.
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

https://github.com/vdlaptrinh/Personal-AI-Assistant/blob/main/01_C%C3%A0i%20%C4%91%E1%BA%B7t%20vibot%20t%E1%BB%AB%20%C4%91%E1%BA%A7u.md

## Usage

1. The assistant will listen for the wake word "Hey Siri". Once detected, it will prompt you to speak your query.

2. The assistant will process your query using Gemini and provide an appropriate response.

3. xin chào

- Chào bạn, Xin chào, Bạn tên gì, biết làm gì

4. HASS

- thực hiện/thực thi/ kích hoạt  + tên kịch bản

- ví dụ kích hoạt kịch bản đi ngủ

- bật/tắt đèn/quạt + tên thiết bị (friendly name)

- ví dụ bật đèn bàn học

- ví dụ tắt quạt phòng khách

5. Chúc tết

- chúc tết + ông bà/ bố mẹ/ sếp/ đồng nghiệp/ gia đình/ thầy cô/ người yêu/ vợ chồng

- ví dụ chúc tết ông bà giúp anh

6. mở nhạc, phát nhạc

- mở nhạc/ mở bài hát + tên bài hát (tiêu đề youtube)

- ví dụ: mở bài hát đông lạnh mới nhớ tới xuân oanh tạ

7. truyện hay

- đọc 1 truyện hay/ truyện ý nghĩa

- ví dụ: kể 1 truyện hay đi em

8. lịch làm việc

- lịch làm việc/ lịch công tác tuần + [thứ 3]

- ví dụ: lịch làm việc => hôm  nay

- ví dụ: lịch công tác tuần thứ 4

9. other

- data khác các từ khoá trên => gemini


## Sample Output
https://www.youtube.com/@VDLapTrinh/shorts

https://www.youtube.com/shorts/zOJwcwMTKwQ
...

Tham khảo: https://github.com/ivan00105/Voice-Based-AI-Assistant-with-ChatGPT-on-Raspberry-Pi
