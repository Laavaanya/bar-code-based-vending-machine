from gpiozero import AngularServo
from time import sleep
servo=AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
servo.angle=0
sleep(2)
servo.detach()

#from RaspberryMotors.motors import servos
#s1=servos.servo(18)
#s1.setAngleAndWait(45)
#s1.shutdown()
#import cv2
#print("hello")
