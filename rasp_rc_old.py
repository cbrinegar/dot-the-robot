#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

from getch import getch

import time
import atexit
import termios
import sys, tty

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
motor1 = mh.getMotor(1)
motor2 = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
motor1.setSpeed(250)
motor2.setSpeed(250)

# --- Enter a user controlled motion loop
while (True):
  #print "In the loop..."
  #char=sys.stdin.read(1)
  # --- This function eliminates the need for enter.
  char=getch()

  if (char=="w"):
    print "Forward"
    motor1.run(Adafruit_MotorHAT.RELEASE);
    motor2.run(Adafruit_MotorHAT.RELEASE);
    time.sleep(0.2);
    motor1.run(Adafruit_MotorHAT.FORWARD);
    motor2.run(Adafruit_MotorHAT.FORWARD);
    #time.sleep(3.0);
    #motor1.run(Adafruit_MotorHAT.RELEASE);
    #motor2.run(Adafruit_MotorHAT.RELEASE);

  if (char=="a"):
    print "Left"
    #motor1.run(Adafruit_MotorHAT.RELEASE);
    motor1.run(Adafruit_MotorHAT.BACKWARD);
    #motor2.run(Adafruit_MotorHAT.RELEASE);
    motor2.run(Adafruit_MotorHAT.FORWARD);
    time.sleep(0.5)
    motor1.run(Adafruit_MotorHAT.RELEASE);
    motor2.run(Adafruit_MotorHAT.RELEASE);

  if (char=="d"):
    print "Right"
    #motor1.run(Adafruit_MotorHAT.RELEASE);
    motor1.run(Adafruit_MotorHAT.FORWARD);
    #motor2.run(Adafruit_MotorHAT.RELEASE);
    motor2.run(Adafruit_MotorHAT.BACKWARD);
    time.sleep(0.5)
    motor1.run(Adafruit_MotorHAT.RELEASE);
    motor2.run(Adafruit_MotorHAT.RELEASE);

  if (char=="s"):
    print "Backward"
    motor1.run(Adafruit_MotorHAT.RELEASE);
    motor2.run(Adafruit_MotorHAT.RELEASE);
    time.sleep(0.2);
    motor1.run(Adafruit_MotorHAT.BACKWARD);
    motor2.run(Adafruit_MotorHAT.BACKWARD);
    #time.sleep(1.0);
    #motor1.run(Adafruit_MotorHAT.RELEASE);
    #motor2.run(Adafruit_MotorHAT.RELEASE);

  if (char=="x"):
    print "Stop"
    motor1.run(Adafruit_MotorHAT.RELEASE);
    motor2.run(Adafruit_MotorHAT.RELEASE);

  if (char=="q"):
    print "Quit"
    motor1.run(Adafruit_MotorHAT.RELEASE);
    motor2.run(Adafruit_MotorHAT.RELEASE);
    break

  char=""
# >>> EOF

