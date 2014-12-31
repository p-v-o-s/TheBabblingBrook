import serial
import time

from subprocess import call

locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',
'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']  

def sayPhrase(phrase):
    commandLine="/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols \"http://translate.google.com/translate_tts?tl=en&q="+ phrase + "\""
    #print commandLine
    call(commandLine,shell=True)
    


# connect on the serial port
for device in locations:  
    try:  
        print "Trying...",device
        arduino = serial.Serial(device, 9600) 
        break
    except:  
        print "Failed to connect on",device   


while 1:


    try:
        arduino.write('Y')
        time.sleep(1)
        x = arduino.readline()
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

            print fullSentence
            #print heading
            sayPhrase(fullSentence)

    except:
        print "Failed to communicate!"
        time.sleep(1)

