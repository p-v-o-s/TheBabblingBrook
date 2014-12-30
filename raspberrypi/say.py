import serial
import time

from subprocess import call

def sayPhrase(phrase):
    commandLine="/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols \"http://translate.google.com/translate_tts?tl=en&q="+ phrase + "\""
    print commandLine
    call(commandLine,shell=True)
    

ser=serial.Serial('/dev/ttyUSB0',115200)
while 1:
    x=ser.readline()
    print x
    x=x.replace(";","")
    xs= x.split()
    if len(xs)==12:
	heading=float(xs[5])
        alt=float(xs[7])
        temps=xs[10].split(".")
        temp0=temps[0]
        s=temps[1]
        s = " ".join(s[i:i+1] for i in range(0, len(s), 2)) 
        if (heading >= 315) or (heading < 45):
            card="North"
        if (heading >=45 ) and (heading < 135):
            card="East"
        if (heading >=135) and (heading < 225):
            card="South"
        if (heading >=225) and (heading < 315):
            card="West"
        temp1=s

        fullSentence = "It's " + temp0 + " point " + temp1 + " degrees Celsius, and I'm lookin " + card

        sayPhrase(fullSentence)

        print heading, alt 

        time.sleep(3)

   
