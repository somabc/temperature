#!/usr/bin/python
#Import modules
from datetime import datetime
from time import sleep
import smtplib
from email.mime.text import MIMEText
import os


#set values
warningcount = 0
max = 26.5
min = 5

#Open datafile for storing temperature data
datafile = open("/tmp/tempdata.log", "a")
#open sensor data and make into a useable string
while True:
   tfile = open("/sys/bus/w1/devices/10-00080225f15a/w1_slave")
   text = tfile.read()
   tfile.close()
   tempdata = text.split("\n")[1].split(" ")[9]
   temp = float(tempdata[2: ])
   temp = temp / 1000
   #Print on screen information
   print "Time", datetime.time(datetime.now())
   print
   print temp, "degrees celcius."
   print "................"
   #write temperature to log file
   time = datetime.time(datetime.now())
   datafile.write (str(time) + "\n")
   datafile.write(str(temp) + "\n")

   #Check temperature ranges
   if temp > max:
      print "WARNING!"
      print "temperature too hot."
      print "........................."
      warningcount = warningcount+1
      print "Warning count - ",  warningcount, "of 6."
      print
      print "........................."
   if temp < min:
      print "WARNING!"
      print "temperature too cold."
      print "........................."
      warningcount = warningcount+1
      print "Warning count - ",  warningcount, "of 6."
      print
      print "........................."

   #check for warnings
   if warningcount == 6:
   #Remove data file to archive
      datafile.close()
      os.system('rm /tmp/tempdata.log')
   #create email
      message = """Machine Room temperature outside of ideal range. %s """ % temp 
      msg = MIMEText (message)
      msg['Subject'] = 'LEVEL 10 TEMPERATURE WARNING!'
      msg['From'] = 'ee.service@imperial.ac.uk'
      msg['To'] = 'i.t.request@imperial.ac.uk'
      # send the email
      s = smtplib.SMTP('smarthost.cc.ic.ac.uk')
#      s.login('username', 'password')   # no need for auth on campus
      s.sendmail(msg['From'], msg['To'], msg.as_string())
      s.quit()
      #reset warningcount
      warningcount = 0
      #open datafile
      datafile = open("tempdata.log", "a")
      print
      print "The sensor has made six readings outside of the ideal range"
      print "Warning e-Mail sent!! Warnings reset."
      print "....................."
      print
      print

#sleep for 10 minutes
   sleep(600)
#close data file
datafile.close()

