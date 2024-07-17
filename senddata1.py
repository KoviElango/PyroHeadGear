from lxml import etree
from w1thermsensor import W1ThermSensor
import os
import sys
import RPi.GPIO as GPIO
try:
	sensor = W1ThermSensor()
except:
	temperature="not detected"
c=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
#GPIO.add_event_detect(7, GPIO.RISING)
try:
	data=etree.Element('data')
	temp= etree.Element('temp')
	co2= etree.Element('co2')
	posuser1= etree.Element('posuser1')
	posuser2= etree.Element('posuser2')
	try:
		temperature=sensor.get_temperature()
	except:
		temperature="not detected"
	temp.text= str(temperature)
	if GPIO.input(7)==0:
		co2State="CAUTION!"
	else:
		co2State="Normal"
	co2.text=str(co2State)
	posuser1.text="400"
	posuser2.text="500"
	data.append(temp)
	data.append(co2)
	data.append(posuser1)
	data.append(posuser2)
	filename = "data.xml"
	FILE = open(filename,"w")
	FILE.writelines(etree.tostring(data, pretty_print=True,xml_declaration=True, encoding='utf-8'))
	FILE.close()
	os.system("sudo adb push data.xml /sdcard/")
except KeyboardInterrupt:
	GPIO.cleanup();
	sys.exit();
