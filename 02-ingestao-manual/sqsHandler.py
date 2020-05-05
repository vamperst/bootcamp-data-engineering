import boto3
import json

sqs = boto3.client('sqs')

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
        return receiptHandle,message
    else:
        return None,None


def deleteMessageFromQueue(urlSQS, receiptHandle):
    response = sqs.delete_message(
        QueueUrl=urlSQS,
        ReceiptHandle=receiptHandle
    )
    print(json.dumps(response))


receiptHandle, message = getMessageFromQueue(urlSQS)
if receiptHandle == None:
   print("nada")
else:
    print(json.dumps(message))
    deleteMessageFromQueue(urlSQS,receiptHandle)
    
    
