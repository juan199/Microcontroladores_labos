#!/usr/bin/env python
#**********************************************************
#						Librerias
#**********************************************************
import matplotlib.pyplot as plt
import serial
import time
from serial import SerialException

#********************************************************
#					Macros y variables
#********************************************************
size=400
ser = serial.Serial('/dev/ttyACM0', 115200)
start_time = time.time()
voltage = []
tempo =[]

#*********************************************************
#				Se obtienen los datos
#*********************************************************
for x in range(0, size):
	serial_line = ' '
	try:
		serial_line = ser.readline()
	except KeyboardInterrupt:
		print " " 
		print "Sorry, Ctrl-C..."
	except SerialException:
			print"STM32F4 disconnected, cua cua"
	voltage.append(serial_line)
	t = (time.time() - start_time)
	tempo.append(t)
	print("--- %6.7s seconds ---" %t)
	print(serial_line)
  
voltage_float= map(float, voltage)

for y in range(0, size):
	voltage_float[y]=voltage_float[y]*1.6

#********************************************************
#				Codigo para Graficar
#********************************************************
plt.plot(tempo, voltage_float)
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
plt.axis([0,1, 0, 2.5]) #//Para definir el rango del eje x
plt.show()





	

   


