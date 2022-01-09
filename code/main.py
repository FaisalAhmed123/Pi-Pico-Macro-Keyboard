# Write your code here :-)
import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
led.value = True

led = digitalio.DigitalInOut(board.GP17)
led.direction = digitalio.Direction.OUTPUT
led.value = True

led = digitalio.DigitalInOut(board.GP21)
led.direction = digitalio.Direction.OUTPUT
led.value = True

btn1_pin = board.GP1                                                                                                                                                                                                                   
btn2_pin = board.GP2
btn3_pin = board.GP3
btn4_pin = board.GP4
btn5_pin = board.GP5                                                                                                                                                                                                                   
btn6_pin = board.GP6
btn7_pin = board.GP7
btn8_pin = board.GP8
btn9_pin = board.GP9

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN


print("on")

while True:
    
    if btn1.value:
        print("button 1 pressed")
        keyboard.press(Keycode.F3)
        while btn1.value:
            time.sleep(0.01)
        keyboard.release(Keycode.F3)


    if btn2.value:
        print("button 2 pressed")
        keyboard.press(Keycode.F3)
        while btn2.value:
            time.sleep(0.01)
        keyboard.release(Keycode.F3)


    if btn3.value:
        print("button 3 pressed")
        keyboard.press(Keycode.RIGHT_ARROW)
        while btn3.value:
            time.sleep(0.01)
        keyboard.release(Keycode.RIGHT_ARROW)


    if btn4.value:
        print("button 4 pressed")
        keyboard.press(Keycode.KEYPAD_ENTER)
        while btn4.value:
            time.sleep(0.01)
        keyboard.release(Keycode.KEYPAD_ENTER)

    if btn5.value:
        print("button 5 pressed")
        keyboard.press(Keycode.W)
        while btn5.value:
            time.sleep(0.01)
        keyboard.release(Keycode.W)


    if btn6.value:
        print("button 6 pressed")
        keyboard.press(Keycode.O)
        while btn6.value:
            time.sleep(0.01)
        keyboard.release(Keycode.O)

    if btn7.value:
        print("button 7 pressed")
        keyboard.press(Keycode.A)
        while btn7.value:
            time.sleep(0.01)
        keyboard.release(Keycode.A)

    if btn8.value:
        print("button 8 pressed")
        keyboard.press(Keycode.S)
        while btn8.value:
            time.sleep(0.01)
        keyboard.release(Keycode.S)

    if btn9.value:
        print("button 9 pressed")
        keyboard.press(Keycode.D)
        while btn9.value:
            time.sleep(0.01)
        keyboard.release(Keycode.D)



