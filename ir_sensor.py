import RPi.GPIO as gpio
import time
import pygame 
gpio.setmode(gpio.BCM)

gpio.setwarnings(False)

pygame.mixer.init()

ir_sens=17

gpio.setup(ir_sens,gpio.IN)

while True:
    
    sens=gpio.input(ir_sens)
    time.sleep(0.01)
    print("sens=",sens)

    if(sens==False):
        pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/upstairs.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
           continue
    
gpio.cleanup()
