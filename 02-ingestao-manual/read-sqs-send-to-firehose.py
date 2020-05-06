from kinesisHandler import KinesisHandler
import json
import uuid
import time



kinesis = KinesisHandler('teste2')
s3 = boto3.resource('s3')
urlSQS = 'https://sqs.us-east-1.amazonaws.com/474339980368/teste'


def getMessageFromQueue(urlSQS):
    response = sqs.receive_message(
        QueueUrl=urlSQS,
        MaxNumberOfMessages=1
    )
    print(json.dumps(response))
    if "Messages" in response:
        receiptHandle = response["Messages"][0]["ReceiptHandle"]
        message = response["Messages"][0]["Body"]
        return receiptHandle, message
    else:
        return None, None


def deleteMessageFromQueue(urlSQS, receiptHandle):
    response = sqs.delete_message(
        QueueUrl=urlSQS,
        ReceiptHandle=receiptHandle
    )
    print(json.dumps(response))


def readObjectAndSendToFirehose(bucket, key):
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

while True:
    receiptHandle, messageStr = getMessageFromQueue(urlSQS)
    if receiptHandle == None:
        print("acabou a fila")
        break
    else:
        receiptHandle, message = getMessageFromQueue(urlSQS)
        bucket = message["bucket"]
        key = message["key"]
        readObjectAndSendToFirehose(bucket, key)
        deleteMessageFromQueue(urlSQS,receiptHandle)
        print("processou mensage:" + str(message))

print("terminou com sucesso")


        

