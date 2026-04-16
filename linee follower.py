import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIG = 27
ECHO = 22
GPIO.setup(TRIG,GPIO.OUT)     # Trig
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(4, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(18, GPIO.IN)

GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)


GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
GPIO.output(7, GPIO.LOW)

##from nanpy import Arduino
##from nanpy import serial_manager
##from time import sleep
##
##Arduino.pinMode(13, Arduino.OUTPUT)
##Arduino.pinMode(12, Arduino.INPUT)
##Arduino.pinMode(11, Arduino.INPUT)
##Arduino.pinMode(8, Arduino.INPUT)
d=1
g=1
M=1
while True :
              r=GPIO.input(18)
              c=GPIO.input(4)
              l=GPIO.input(23)
              GPIO.output(TRIG,False)                 #Set TRIG as LOW
              print ("Waitng For Sensor To Settle")
              time.sleep(0.1)                            #Delay of 2 seconds

              GPIO.output(TRIG, True)                  #Set TRIG as HIGH
              time.sleep(0.00001)                      #Delay of 0.00001 seconds
              GPIO.output(TRIG, False)                 #Set TRIG as LOW

              while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
                  pulse_start = time.time()              #Saves the last known time of LOW pulse

              while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
                  pulse_end = time.time()                #Saves the last known time of HIGH pulse 

              pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

              distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
              distance = round(distance, 2)
              print ("Distance:",distance - 0.5,"cm")

              if distance > 2 and distance < 400:      #Check whether the distance is within range
                 print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
              else:
                 print ("Out Of Range") 
    
              if (distance<30) :
                    print ("movestop")
                    GPIO.output(7, GPIO.LOW)
                    GPIO.output(8, GPIO.LOW)
                    GPIO.output(25,GPIO.LOW)
                    GPIO.output(24,GPIO.LOW)
                    time.sleep(1)
              else :
             
             
               
               if l==0:
                   g=0
               else:
                   g=1
                   
                   
               if r==0:
                   d=0
               else:     
                   d=1
                   
                   
               if c==0:
                   d=1
                   g=1
                   M=0

               if  (g==0) and (l==0):
                      print ("LEFT Black")
                      GPIO.output(24, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      time.sleep(0.1)                      
                      GPIO.output(7, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(25, GPIO.HIGH)
                      GPIO.output(24, GPIO.LOW)
                      time.sleep(1)
                      GPIO.output(24, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      g=0
                      d=1
                      M=1
                      
               if  (c==0):
                 if (l==0):
                      print ("LEFT Black")
                      GPIO.output(24, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      time.sleep(0.1)                      
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      GPIO.output(25, GPIO.HIGH)
                      GPIO.output(24, GPIO.LOW)
                      time.sleep(1)
                      GPIO.output(24, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      g=0
                      d=1
                      M=0

               if (d==0) and (r==0):
                      print ("RIGHT Black")
                      GPIO.output(24, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      time.sleep(0.1)
                      GPIO.output(8, GPIO.HIGH)
                      GPIO.output(7, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(24, GPIO.LOW)
                      time.sleep(1)
                      GPIO.output(24, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      d=0
                      g=1
                      M=1
                      
               if (c==0):
                 if (r==0):
                      print ("RIGHT Black")
                      GPIO.output(24, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      time.sleep(0.1)
                      GPIO.output(8, GPIO.HIGH)
                      GPIO.output(7, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(24, GPIO.LOW)
                      time.sleep(1)
                      GPIO.output(24, GPIO.LOW)
                      GPIO.output(25, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      d=0
                      g=1
                      M=0

               if (c==0):
                 if (r==1):
                    if (l==1):
                          print ("Middel Black")
                          GPIO.output(25, GPIO.HIGH)
                          GPIO.output(24, GPIO.LOW)
                          GPIO.output(8, GPIO.HIGH)
                          GPIO.output(7, GPIO.LOW)                       
                               
                             

               if (c==0):
                 if (r==0):
                    if (l==0):
                          print ("ALL BLACK STOP")
                          GPIO.output(24, GPIO.LOW)
                          GPIO.output(25, GPIO.LOW)
                          GPIO.output(8, GPIO.LOW)
                          GPIO.output(7, GPIO.LOW)
                          break


