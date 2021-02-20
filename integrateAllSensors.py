                             # Importing modules
import spidev                # To communicate with SPI devices
from numpy import interp     # To scale values
from time import sleep       #To add delay
import time
import RPi.GPIO as gpio
import pygame#To use GPIO pins
                             # Start SPI connection
spi = spidev.SpiDev()        # Created an object
spi.open(0,0)

gpio.setwarnings(False)
pygame.mixer.init()                               # Initializing LED pin as OUTPUT pin                              
led_pin = 20

trig=21
echo=16

trig_up=23
echo_up=24

ir_sens=17


gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

gpio.setup(18, gpio.IN) #PIR

gpio.setup(ir_sens,gpio.IN)

gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)
gpio.setup(trig_up,gpio.OUT)
gpio.setup(echo_up,gpio.IN)
                               # Creating a PWM channel at 100Hz frequency
pwm = gpio.PWM(led_pin, 100)
pwm.start(0) 
                               # Read MCP3008 data
while True:
    def analogInput(channel):
          spi.max_speed_hz = 1350000
          adc = spi.xfer2([1,(8+channel)<<4,0])
          data = ((adc[1]&3) << 8) + adc[2]
          return data

    while True:
        output = analogInput(0) # Reading from CH0
        output = interp(output, [0, 1023], [0, 100])
        print("wet=",output)
        pwm.ChangeDutyCycle(output)
        sleep(0.1)
        
        sens=gpio.input(ir_sens)
        time.sleep(0.01)
        print("sens=",sens)
        
        gpio.output(trig,False)
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
        
        gpio.output(trig_up,False)
    #print("waiting for sensor to settle")
        time.sleep(2)
    
        gpio.output(trig_up,True)
        time.sleep(0.00001)
        gpio.output(trig_up,False)
    
        while gpio.input(echo_up)==0:
            pulse_start=time.time()
        
        while gpio.input(echo_up)==1:
            pulse_end=time.time()
        
        pulse_duration_up=pulse_end-pulse_start
    
        distance_up=pulse_duration_up*17150
    
        print("distance_up=",distance_up)
        
        print("     ")
        
        a = gpio.input(18)
        if a:
            
            print("Motion Detected...")
            #time.sleep(5) #to avoid multiple detection
            pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/someone ahead.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            
        
        else:
            print("Motion not Detected...")
            #time.sleep(0.1) #loop delay, should be less than detection dela          

        
        if(distance_up<=50 and a==True):
            pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/someone.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            
        ### upstairs ir sensor
        if(sens==False):
            pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/upstairs.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            
           #wet surface
        if(output<=80.00):
            pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/wet.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
        
        
        ### downstairs ultrasound
        elif(distance>=10):
            pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/downstairs.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            
        ### upar wala ultrasound
        elif(distance_up<=50):
            pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/obstacles ahead.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            
        elif(distance_up<=50 and a==True):
            pygame.mixer.music.load("C:/Users/user/Downloads/KU HackFest/audio/someone.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            

gpio.cleanup()