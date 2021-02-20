import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN) #PIR
pygame.mixer.init()



try:
    time.sleep(2) 
    while True:
        a = GPIO.input(18)
        if a:
            
            print("Motion Detected...")
            
            pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/someone ahead.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            
        
        else:
            print("Motion not Detected...")
            #time.sleep(0.1) #loop delay, should be less than detection dela          

except:
    GPIO.cleanup()
