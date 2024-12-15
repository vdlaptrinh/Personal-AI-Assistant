import time
from rpi_ws281x import PixelStrip, Color

# Số lượng đèn LED và các cấu hình GPIO
LED_COUNT = 30        # Số lượng đèn LED
LED_PIN = 18          # Chân GPIO cho tín hiệu Data (Chân GPIO hợp lệ cho WS281x)
LED_CLOCK_PIN = 21    # Chân GPIO cho tín hiệu Clock (Có thể thay đổi nếu cần)
LED_FREQ_HZ = 800000  # Tần số PWM
LED_DMA = 10          # DMA channel
LED_INVERT = False    # Không đảo ngược tín hiệu
LED_BRIGHTNESS = 255  # Độ sáng tối đa

# Khởi tạo đèn LED
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CLOCK_PIN)
strip.begin()

# Chức năng để thay đổi màu của các đèn LED
def color_wipe(color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

# Hiệu ứng màu sắc "wakeup" - thay đổi màu liên tục
def wakeup_effect():
    colors = [Color(255, 0, 0), Color(0, 255, 0), Color(0, 0, 255)]  # Đỏ, Xanh lá, Xanh dương
    for color in colors:
        color_wipe(color, wait_ms=100)

# Đèn LED bắt đầu sáng với màu đỏ
color_wipe(Color(255, 0, 0))  # Đỏ
time.sleep(1)

# Sau đó chuyển sang hiệu ứng wakeup
wakeup_effect()

# Tắt đèn LED
strip.fill(Color(0, 0, 0))
strip.show()
