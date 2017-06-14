from machine import Pin
from time import sleep_ms
led = Pin(2, Pin.OUT)


def led_blink_th():
    print("เริ่มทำงาน ระบบไฟกระพริบ")
    led.off()
    sleep_ms(500)
    led.on()
    sleep_ms(500)
    print("กระพริบ")
