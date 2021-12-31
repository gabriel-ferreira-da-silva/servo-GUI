import serial
import os
import time
while 1:
	file=open("status",'w')
	file.write("waiting")
	file.close()
	try:
		ser=serial.Serial('/dev/ttyACM0', 9600)
		ser.timeout = 1.0
		o='o'
		ser.write(o.encode("utf_8"))
		line=ser.readline()
		if line.decode("utf_8")=="comecei":
			file=open("status",'w')
			file.write("ok")
			file.close()

			while 1:
				line=ser.readline()
				if line.decode("utf_8"):
					file=open("buffer",'w')
					file.write(line.decode("utf_8"))
					file.close()

		ser.close()

	except:

		ser=serial.Serial('/dev/ttyACM1', 9600)
		ser.timeout = 1.0
		ser.write(b'o')
		line=ser.readline()
		if line.decode("utf_8")=="comecei":
			file=open("status",'w')
			file.write("ok")
			file.close()
			ser.write(b'o')
			while 1:
				line=ser.readline()
				if line.decode("utf_8"):
					file=open("buffer",'w')
					file.write(line.decode("utf_8"))
					file.close()

		ser.close()

