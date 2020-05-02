import boto3
import json
import os
import uuid



class SQS:

    def __init__(self):
        super().__init__()
        self.__URL = os.environ['urlSQS']
        self.__sqs = boto3.client('sqs')


    def getMessageFromQueue(self):
        response = self.__sqs.receive_message(
            QueueUrl=self.__URL,
            MaxNumberOfMessages=1
        )
        print(json.dumps(response))
        if "Messages" in response:
            receiptHandle = response["Messages"][0]["ReceiptHandle"]
            message = response["Messages"][0]["Body"]
            return receiptHandle,message
        else:
            return None,None


    def deleteMessageFromQueue(self,receiptHandle):
        response = self.__sqs.delete_message(
            QueueUrl=self.__URL,
            ReceiptHandle=receiptHandle
        )
        print(json.dumps(response))


    def __mountMessagesToSQS(self,listObjectKeys, numberMsgsByBatch=10):
        listEntriesSQS = []
        for obj in listObjectKeys:
            listEntriesSQS.append(
                {
                    "Id": str(uuid.uuid1()),
                    'MessageBody': json.dumps(obj)
                }
            )
        listOfLists = [listEntriesSQS[i * numberMsgsByBatch:(i + 1) * numberMsgsByBatch]
                    for i in range((len(listEntriesSQS) + numberMsgsByBatch - 1) // numberMsgsByBatch)]
        return listOfLists

    def sendToQueue(self, listObjectKeys, numberMsgsByBatch=10):
        
        listToSend = self.__mountMessagesToSQS(
            listObjectKeys, numberMsgsByBatch)

        response = self.__sqs.send_message_batch(
            QueueUrl=self.__URL,
            Entries=listToSend[0]
        )
        print(response)
        
