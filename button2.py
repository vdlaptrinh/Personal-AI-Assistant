import RPi.GPIO as GPIO
import time

# Cấu hình GPIO
BUTTON_PIN = 17  # Chân GPIO 17

# Hàm callback sẽ được gọi khi có ngắt (nút bấm)
def button_callback(channel):
    print("Nút bấm đã được nhấn!")

# Cấu hình chế độ sử dụng BCM (Broadcom GPIO pin numbering)
GPIO.setmode(GPIO.BCM)

# Cấu hình GPIO 17 là input và sử dụng pull-up resistor
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Thêm sự kiện phát hiện cạnh (ngắt) trên GPIO 17 khi nút được nhấn (FALLING edge)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
    print("Chương trình đang chạy... Nhấn Ctrl+C để thoát.")
    while True:
        # Chương trình sẽ tiếp tục chạy, và chờ ngắt
        time.sleep(1)

except KeyboardInterrupt:
    print("Dừng chương trình.")
    
finally:
    GPIO.cleanup()  # Giải phóng GPIO khi kết thúc

