import os

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

tfile = open("/sys/bus/w1/devices/10-00080225f15a/w1_slave") 
text = tfile.read() 
tfile.close() 
secondline = text.split("\n")[1] 
temperaturedata = secondline.split(" ")[9] 
temperature = float(temperaturedata[2:]) 
temperature = temperature / 1000 
print temperature

