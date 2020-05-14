from kinesisHandler import KinesisHandler
import json
import uuid
import time
import boto3



kinesis = KinesisHandler('ingest-json')
s3 = boto3.resource('s3')
sqs = boto3.client('sqs')
urlSQS = 'https://sqs.us-east-1.amazonaws.com/764597347320/raw-json'


def getMessageFromQueue(urlSQS):
    response = sqs.receive_message(
        QueueUrl=urlSQS,
        MaxNumberOfMessages=1
    )
    if "Messages" in response:
        receiptHandle = response["Messages"][0]["ReceiptHandle"]
        message = response["Messages"][0]["Body"]
        return receiptHandle, json.loads(message)
    else:
        return None, None


def deleteMessageFromQueue(urlSQS, receiptHandle):
    response = sqs.delete_message(
        QueueUrl=urlSQS,
        ReceiptHandle=receiptHandle
    )
    print("message deleted: " + json.dumps(response))


def readObjectAndSendToFirehose(bucket, key):
    obj = s3.Object(bucket, key)
    cont = 0
    listLines = []
    for line in obj.get()['Body']._raw_stream:
        # s = StringIO(line.decode("utf-8"))
        listLines.append(line.decode("utf-8"))
        if cont == 149:
            kinesis.put_record(listLines)
            cont = 0
            listLines = []
        else:
            cont += 1
    if len(listLines) > 0:
        kinesis.put_record(listLines)
        print("enviou fora for")

while True:
    receiptHandle, message = getMessageFromQueue(urlSQS)
    if receiptHandle == None:
        print("acabou a fila")
        break
    else:
        print("received message: " + str(message))
        bucket = message["bucket"]
        key = message["key"]
        readObjectAndSendToFirehose(bucket, key)
        deleteMessageFromQueue(urlSQS,receiptHandle)

print("terminou com sucesso")


        

