from kinesisHandler import KinesisHandler
import json
import uuid
import time

kinesis = KinesisHandler('teste2')
# while(True):
raw = open('demofile2.json', 'r').read()
lines = raw.split('\n')
cont=0
listLines=[]
for line in lines:
    listLines.append(line)

    if cont == 150:
        kinesis.put_record(listLines)
        cont=0
        listLines=[]
        print("enviou")
    else:
        cont += 1
        


    # time.sleep(2)

        

