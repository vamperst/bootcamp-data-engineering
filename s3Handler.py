import boto3
import json
import uuid

s3 = boto3.client('s3')
sqs = boto3.client('sqs')

bucket = 'teste-dms-rafbarbo'
urlSQS = 'https://sqs.us-east-1.amazonaws.com/474339980368/teste'

def getListofKeyObjects(bucket,keyPrefix):

    response = s3.list_objects_v2(
        Bucket=bucket,
        Prefix=keyPrefix
    )

    listObjectKeys=[]
    for obj in response["Contents"]:
        listObjectKeys.append({"bucket":bucket,"key":obj["Key"]})
        # print(obj["Key"])
    print(len(listObjectKeys))
    # print(response)
    return listObjectKeys


def mountMessagesToSQS(listObjectKeys,numberMsgsByBatch=10):
    listEntriesSQS=[]
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


def sendToQueue(url, listToSend):
    response = sqs.send_message_batch(
        QueueUrl=url,
        Entries=listToSend
    )
    print(response)

listObjectKeys = getListofKeyObjects(bucket,'files-small/')   
listOfLists = mountMessagesToSQS(listObjectKeys)
for listToSend in listOfLists:
    sendToQueue(urlSQS,listToSend)
    
