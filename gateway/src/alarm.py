#!/usr/bin/env python
#Call a specific phone number or send SMS via GA6 GSM module 
#Hardware connection method:
#Gateway(Pi)       GA6
#5V      <-->    5V
#GND     <-->    GND
#(#8)TX  <-->    URX
#Priyanshu Yadav 3rd ECE 220105038

#(#10)RX <-->    UTX

import serial   
se = serial.Serial("/dev/ttyS0", 115200) 

def alarm_call(num):
  se.write('ATD'+num.decode())

def alam_sms(num,content):
  se.write('AT+CMGF=1'.decode())
  se.write('AT+CSCS="GSM"'.decode())
  if '>' in se.read():
    se.write(0x1a)
  else:
    return

