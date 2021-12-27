import serial

ser = serial.Serial(
    port='COM4',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

# success_bytes = ser.write(15)

# print (success_bytes)

#this will store the line
line = []
count =1
while True:
    for line in ser.read():
        print(str(count) + str(': ') + str(line) )
        count = count+1

ser.close()