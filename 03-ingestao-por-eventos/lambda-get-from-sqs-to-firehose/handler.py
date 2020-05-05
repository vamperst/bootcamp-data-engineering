import boto3
import json
import os
from kinesisHandler import KinesisHandler
from io import StringIO

deliveryStream = os.environ['deliveryStream']
def handler(event, context):
    print(str(event))
    # print(str(context))

    kinesis = KinesisHandler(deliveryStream)
    s3 = boto3.resource('s3')
    
    for record in event['Records']:
        message=json.loads(record['body'])
        bucket = message["bucket"]
        key = message["key"]

        obj = s3.Object(bucket, key)

        cont = 0
        listLines = []
        for line in obj.get()['Body']._raw_stream:
            s = StringIO(line.decode("utf-8"))
            # print(type(s))
            # print(str(s))
            listLines.append(s.getvalue())

            if cont == 150:
                kinesis.put_record(listLines)
                cont = 0
                listLines = []
                # print("enviou")
            else:
                cont += 1
        if len(listLines) > 0:
            kinesis.put_record(listLines)
            print("enviou fora for")
    print("terminou com sucesso")



    
