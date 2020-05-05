import boto3
import json
import os
from sqsHandler import SQS


def handler(event, context):
    print(str(event))
    # print(str(context))

    bucketName = event['Records'][0]['s3']['bucket']['name']
    bucketKey = event['Records'][0]['s3']['object']['key']

    print("Bucket name:" + bucketName)
    print("Bucket key:" + bucketKey)

    listSQS = [{
        "bucket": bucketName,
        "key": bucketKey
    }]

    sqs = SQS()
    sqs.sendToQueue(listSQS)