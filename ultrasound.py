import RPi.GPIO as gpio
import time
import pygame
gpio.setmode(gpio.BCM)

gpio.setwarnings(False)

pygame.mixer.init()

trig=23
echo=24

print("Distance measurement in progress....")
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

while True:
    gpio.output(trig,False)
    #print("waiting for sensor to settle")
    time.sleep(2)
    
    gpio.output(trig,True)
    time.sleep(0.00001)
    gpio.output(trig,False)
    
    while gpio.input(echo)==0:
        pulse_start=time.time()
        
    while gpio.input(echo)==1:
        pulse_end=time.time()
        
    pulse_duration=pulse_end-pulse_start
    
    distance=pulse_duration*17150
    
    print("distance=",distance)
    
    if(distance<=15):
        pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/obstacles ahead.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
           continue
        
    
gpio.cleanup()