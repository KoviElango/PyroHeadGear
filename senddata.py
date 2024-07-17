from lxml import etree
from w1thermsensor import W1ThermSensor
import jaydebeapi
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
	con=jaydebeapi.connect('com.mysql.jdbc.Driver',"jdbc:mysql://www.db4free.net:3306/gpstrackerapp?user=aravinddbz&password=tysontyson")
	cur=con.cursor()
	while (c==0):
		data=etree.Element('data')
		temp= etree.Element('temp')
		co2= etree.Element('co2')
		lat= etree.Element('lat')
		lon= etree.Element('lon')
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
		cur.execute("select lat,lon from location")
		gpsdata=cur.fetchone()
		latuser1=float(gpsdata[0])
		lonuser1=float(gpsdata[1])
		gpsdata=cur.fetchone()
		latuser2=float(gpsdata[0])
		lonuser2=float(gpsdata[1])
		lat.text=str(int((latuser1-latuser2)*10000000))
		lon.text=str(int((lonuser1-lonuser2)*10000000))
		data.append(temp)
		data.append(co2)
		data.append(lat)
		data.append(lon)
		filename = "data.xml"
		FILE = open(filename,"w")
		FILE.writelines(etree.tostring(data, pretty_print=True,xml_declaration=True, encoding='utf-8'))
		FILE.close()
		os.system("sudo adb push data.xml /sdcard/")
except KeyboardInterrupt:
	cur.close()
	con.close()
	GPIO.cleanup();
	sys.exit();