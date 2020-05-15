import boto3
import json
import time

class KinesisHandler:
    def __init__(self, streamName):
        self.__kinesis = boto3.client('firehose')
        self.__streamName = streamName

    def __prepareDataToFirehoseCall(self, listLine):
        listData = []
        for line in listLine:
            listData.append(
                {
                    "Data": line
                }
            )

        # print(len(json.dumps(listData)))
        return listData

    def put_record(self, listLine):
        # print(self.__prepareDataToFirehoseCall(listLine))
        response = self.__kinesis.put_record_batch(
            DeliveryStreamName=self.__streamName,
            Records=self.__prepareDataToFirehoseCall(listLine)
        )
        if(response['FailedPutCount'] > 0):
            print("FailedPutCount: " + str(response['FailedPutCount']))
            if(response['FailedPutCount'] == len(listLine)):
                time.sleep(1)
                self.put_record(listLine)
            # print(response)
           
        # print(json.dumps(response))
