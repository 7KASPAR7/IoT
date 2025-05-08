import machine
from machine import SoftI2C,Pin
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import random
import time
from keypad import Keypad

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

digits = [0,1,2,3,4,5,6,7,8,9]

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

def init_keypad():
    rows = [Pin(12, Pin.IN, Pin.PULL_UP), Pin(13, Pin.IN, Pin.PULL_UP), 
        Pin(14, Pin.IN, Pin.PULL_UP), Pin(27, Pin.IN, Pin.PULL_UP)]
    cols = [Pin(32, Pin.OUT), Pin(33, Pin.OUT), 
            Pin(25, Pin.OUT), Pin(26, Pin.OUT)]

    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']]

    keypad = Keypad(rows, cols, keys)
    return keypad

def show_start_message():
    lcd.move_to(3,0)
    lcd.putstr("Let's play")

    lcd.move_to(1,1)
    lcd.putstr("Bulls and cows!")
    time.sleep(1)

def shuffle_array(array):
    for i in range(len(array) - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
    return array

def show_code_is_screen():
    lcd.clear()
    lcd.move_to(2,0)
    lcd.putstr("Code is ")

def generate_code():
    shuffled_digits = shuffle_array(digits.copy())
    code = ""
    for i in range(4):
        code += (str(shuffled_digits[i]))
    print("Generated code is: ", code)
    show_code_is_screen()
    return code

def win():
    lcd.clear()
    lcd.move_to(4,0)
    lcd.putstr("You won!")
    lcd.move_to(3,1)
    lcd.putstr("Game over!")

def calculate_bulls_and_cows(code, correct_code):
    bulls = sum(s == g for s, g in zip(correct_code, code))
    cows = sum(min(correct_code.count(x), code.count(x)) for x in set(code)) - bulls
    print("Your guess is: ", code)
    print("bulls:" + str(bulls) + ", cows:" + str(cows))
    return bulls, cows

def reset(code, correct_code):
    bulls, cows = calculate_bulls_and_cows(code, correct_code)
    lcd.move_to(0,1)
    lcd.putstr("bulls:" + str(bulls) + ", cows:" + str(cows))
    time.sleep(2)
    show_code_is_screen()

def is_code_correct(code, correct_code):
    return correct_code == code

        
def main():
    keypad = init_keypad()

    player_code = ""
    generated_code = ""
    show_start_message()
   
    generated_code = generate_code()
    while True:
        key_pressed = keypad.read_keypad()
        if key_pressed:
            lcd.putstr(key_pressed)
            player_code += key_pressed
            if len(player_code) == 4:
                time.sleep(0.5)
                if is_code_correct(player_code, generated_code):
                    win()
                else:
                    reset(player_code, generated_code)
                    player_code = ""
        time.sleep(0.15)


main() 