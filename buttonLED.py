
from time import sleep  
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
button1=20              
button2=16
button3=12
LED1=26
LED2=22
LED3=18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(LED1,GPIO.OUT) 
GPIO.setup(LED2,GPIO.OUT) 
GPIO.setup(LED3,GPIO.OUT) 

BS1=False
BS2=False
BS3=False

#pwm1=GPIO.PWM(LED1,1000) 
#pwm2=GPIO.PWM(LED2,1000)  
#pwm3=GPIO.PWM(LED2,1000)
#pwm1.start(0)                     
#pwm2.start(0) 
#pwm2.start(0)              
#bright=1                   
while(1):                 
	if GPIO.input(button1)==0:             
		print "Button 1 was Pressed"   
		 if BS1==False:                
                        GPIO.output(LED1,True)
                        BS1=True              
                        sleep(.5)           
                else:                         
                        GPIO.output(LED1,False)
                        BS1=False               
                        sleep(.5)

#		bright=bright/2.               
#		pwm1.ChangeDutyCycle(bright)   
#		pwm2.ChangeDutyCycle(bright)   
#		pwm3.ChangeDutyCycle(bright)   
#		sleep(.25)                     
#		print " Brightness is: ",bright 

	if GPIO.input(button2)==0:            
		print "Button 2 was Pressed"  
		 if BS2==False:                
                        GPIO.output(LED2,True)
                        BS2=True             
                        sleep(.5)            
                else:                         
                        GPIO.output(LED2,False) 
                        BS2=False               
                        sleep(.5)
#		bright=bright*2                
#		if bright>100:                 
#			bright=100
#			print " Full Bright"
#		pwm1.ChangeDutyCycle(bright) 
#		pwm2.ChangeDutyCycle(bright)  
#		pwm3.ChangeDutyCycle(bright)   
#		sleep(.25)                   
#		print " Brightness is: ",bright
 
	if GPIO.input(button3)==0:            
		print "Button 3 was Pressed"  
		 if BS3==False:                
                        GPIO.output(LED3,True)
                        BS3=True             
                        sleep(.5)            
                else:                         
                        GPIO.output(LED3,False) 
                        BS3=False               
                        sleep(.5)

