import boto3
import json


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
        response = self.__kinesis.put_record_batch(
            DeliveryStreamName=self.__streamName,
            Records=self.__prepareDataToFirehoseCall(listLine)
        )
