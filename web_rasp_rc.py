#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

from getch import getch

import time
import atexit
import termios
import sys, tty

import web
from web import form

# Define motor controls and setup

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)


def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

motor1 = mh.getMotor(1)
motor2 = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
motor1.setSpeed(250)
motor2.setSpeed(250)

# --- -----------------------------------------------------------------------
# --- Web interface
# Define the pages (index) for the site
urls = ('/', 'index')
render = web.template.render('templates')

app = web.application(urls, globals())

# Define the buttons that should be shown on the form
my_form = form.Form(
 form.Button("btn", id="btnR", value="R", html="Red", class_="btnRed"),
 form.Button("btn", id="btnG", value="G", html="Green", class_="btnGreen"),
 form.Button("btn", id="btnO", value="0", html="-Off-", class_="btnOff")
)

# Define actions
class index:
  def GET(self):
    form = my_form()
    return render.index( form, "Raspberry Pi Python Remote Control" )

  def POST(self):
    userData = web.input()

    if userData.btn == "R":
      print "Stop"
      motor1.run(Adafruit_MotorHAT.RELEASE);
      motor2.run(Adafruit_MotorHAT.RELEASE);
    elif userData.btn == "G":
      print "Forward"
      motor1.run(Adafruit_MotorHAT.FORWARD);
      motor2.run(Adafruit_MotorHAT.FORWARD);
    elif userData.btn == "0":
      print "Quit"
      motor1.run(Adafruit_MotorHAT.RELEASE);
      motor2.run(Adafruit_MotorHAT.RELEASE);
    else:
      print "nothing"

    # --- Do other actions

    # --- reload web form
    raise web.seeother('/')

if __name__ == "__main__":
  app.run()

# >>> EOF

