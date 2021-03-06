#!/usr/bin/python 
##########################################################
# * Python code for generating square wave of programmable 
# * frquency using pwm on Beaglebone Black running Debian 7 Linux
##########################################################
# * Developed by MicroEmbedded Technologies
##########################################################


###########################################################
# NOTE: PWM drivers must be loaded before executing this program
# Load pwm drivers using following commands on BBB shell prompt:
# echo am33xx_pwm > /sys/devices/bone_capemgr.9/slots 
# echo bone_pwm_P8_13 > /sys/devices/bone_capemgr.9/slots
###########################################################

import sys
import os
import time

PWM_DIR = "/sys/devices/ocp.3/pwm_test_P8_13.15"
PWM_PERIOD = 20000000
PWM_DUTY =   19000000

def pwmWritePeriod(val):
	try: 
   		fo = open(PWM_DIR + "/period","w")  
   		fo.write(val)
   		fo.close()
   		return
   	except IOError:
 		return

def pwmWriteDuty(val):
	try: 
   		fo = open(PWM_DIR + "/duty","w")  
   		fo.write(val)
   		fo.close()
   		return
   	except IOError:
 		return
 		
def pwmReset():
	try: 
   		fo = open(PWM_DIR + "/run","w")  
   		fo.write("0")
   		fo.close()
   		return
   	except IOError:
 		return 		
 		
def pwmStart():
	try: 
   		fo = open(PWM_DIR + "/run","w")  
   		fo.write("1")
   		fo.close()
   		return
   	except IOError:
 		return




print "\nSquare wave of Programmable frequency using Python\n"
print  "--------------------------------------------------------------------------------------\n" 	
pwmWritePeriod(str(PWM_PERIOD))
pwmWriteDuty(str(PWM_DUTY))
pwmReset()
time.sleep(2)
pwmStart()
for i in range(0,9):
	PWM_DUTY = PWM_DUTY - 1000000
	pwmWriteDuty(str(PWM_DUTY))
	time.sleep(1)
	print "increasing duty"
print"------------------------"
for i in range(0,9):
	PWM_DUTY = PWM_DUTY + 1000000
	pwmWriteDuty(str(PWM_DUTY))
	time.sleep(1)
	print "decreasing duty"
pwmReset()	
exit()

