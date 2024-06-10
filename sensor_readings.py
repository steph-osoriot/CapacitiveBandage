import serial
import datetime
import keyboard

f = open('noamp_noise.txt', 'w')
data = []
print("hit arduino reset and press space to start reading")
keyboard.wait('space')
ser = serial.Serial(port='COM17', baudrate=115200)
print("connected to: " +  ser.portstr)
while True:
  l = str(ser.readline())[2:-5]
  data.append(l + "\n")
  # CODE TO ALSO PRINT DATE:
  # print(l)
  # data.append(str(datetime.datetime.now().time()) + " " + l + '\n')
  # CODE FOR low and high being printed SEPARATELY
  # vals = l.split(" ")
  # if (len(vals) == 2) :
  #  datahigh.append(vals[0] + '\n')
  #  datalow.append(vals[1] + '\n')
  if (keyboard.is_pressed('esc')):  
    break

ser.close()
f.writelines(data)
f.close()
#seperate accumulator for high and low signal