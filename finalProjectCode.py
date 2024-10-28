#Importing
from machine import Pin 
import time
import machine

button = Pin(15, Pin.OUT) #retriving buzzer
buzzer = Pin(11, Pin.OUT)  #retriving button  
led = Pin(16, Pin.OUT)    #retriving LED
potentiometer = machine.ADC(26) #retriving potentiometer
conversion_factor = 3.3 / (65535) #3.3 is the volts we have avaliable 



buzzer.value(0) #Intilise button at off


while True:
    current = potentiometer.read_u16() * conversion_factor # setting voltage
    print(current)
    if current == 3.3:
        if button.value() == 1:# allows button to work for LED and buzzer if current = 3.3
            led.on()
            time.sleep(0.1) #buzzer and light turn on delay
            buzzer.value(1)
        else:
            led.off() #doesn't allow LED to turn on if current != 3.3
            buzzer.value(0) #doesn't allow buzzer to turn on if current != 3.3
    else:
        led.off()
        buzzer.value(0) 



