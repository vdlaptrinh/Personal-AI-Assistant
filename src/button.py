import RPi.GPIO as GPIO
import time

BUTTON = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
    
try:
    print("Chương trình đang chạy... Nhấn Ctrl+C để thoát.")
    while True:
        state = GPIO.input(BUTTON)
        if state:
            print("off")
        else:
            print("on")
        time.sleep(1)

except KeyboardInterrupt:
    print("Dừng chương trình.")
    GPIO.cleanup()  # Giải phóng GPIO khi kết thúc
