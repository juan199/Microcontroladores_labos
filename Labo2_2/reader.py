#!/usr/bin/env python
#**********************************************************
#						Librerias
#**********************************************************
import matplotlib.pyplot as plt
import serial
import time
from serial import SerialException
import csv

#********************************************************
#					Macros y variables
#********************************************************
size=400
ser = serial.Serial('/dev/ttyACM0',115200)
start_time = time.time()
voltage = []
voltage_float = []
tempo =[]

#*********************************************************
#				Se obtienen los datos
#*********************************************************
f = open('file.log', 'r') # lee el file.log generado con el comando minicom -C file.log
listot = f.readlines()

for x in range(0, size):
	serial_line = ' '
	try:
		serial_line = ser.readline()
	except KeyboardInterrupt:
		print (" ") 
		print ("Sorry, Ctrl-C...")
	except SerialException:
			print("STM32F4 disconnected, cannot read the serial port...cua cua")		
	#voltage.append(serial_line)
	t = (time.time() - start_time)
	tempo.append(t)
	print("--- %6.7s seconds ---" %t)
	#print(serial_line)
	voltage_float.append(float(listot[x+5]))
	print(voltage_float[-1])
	
  
#voltage_float= map(float, voltage)

for y in range(0, size):
	voltage_float[y]=voltage_float[y]*1.6

#********************************************************
#				Codigo para Graficar
#********************************************************
plt.plot(tempo, voltage_float)
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
#plt.axis([0,1, 0, 2.5]) #//Para definir el rango del eje x
plt.show()




#********************************************************
#				Codigo para crear el log .csv
#********************************************************
with open('log.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['Voltage']  + ['Time'])
	for x in range(0, size):
		spamwriter.writerow([ voltage_float[x], tempo[x]])




	

   


