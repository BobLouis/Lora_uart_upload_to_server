import serial
import http.client


ser = serial.Serial(
    port='COM4',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

conn = http.client.HTTPConnection("140.116.245.242:7165")

print("connected to: " + ser.portstr)

life = 0
id = 0
rpm_R = 0
rpm_L = 0
voltage = 0
current = 0


headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "9f74b04f-dcdc-e793-5dcb-58015ab957e9"
}
# payload = "{\"name\":\"CK06\",\"lifeExpectancy\":4,\"type\":\"sporting\",\"origin\":\"Taiwan\"}\n\t"
# conn.request("POST", "/", payload, headers)
# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))
# success_bytes = ser.write(15)

# print (success_bytes)

#this will store the line
line = []
count =1
while True:
    for line in ser.read():
        print(str(count) + str(': ') + str(line) )
        if count == 1 :
            id = line
        elif count == 2:
            rpm_R = line
        elif count == 3:
            rpm_L = line
        elif count == 4:
            voltage = line
        elif count == 5:
            current = line
        
        if(count%8==0):
            print(life)
            payload = "{\"id\":%d,\"rpm_R\":%d,\"rpm_L\":%d,\"voltage\":%d,\"current\":%d}\n\t"%(id,rpm_R,rpm_L,voltage,current)
            conn.request("POST", "/", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))
            count = 1
        count += 1
        
    
ser.close()