
import csv
import json
from io import StringIO
import os
import boto3
import uuid


s3 = boto3.resource('s3')
s3Client = boto3.client('s3')
sqs = boto3.client('sqs')
bucket = 'teste-dms-rafbarbo'
urlSQS = 'https://sqs.us-east-1.amazonaws.com/474339980368/teste'

collumns = ["BibNum", "Title", "Author",
            "ISBN", "PublicationYear", "Publisher", "Publisher", 
            "Subjects", "ItemType", "ItemCollection", "FloatingItem", 
            "ItemLocation", "ReportDate", "ItemCount"]


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


def createJsonFromCSVInS3(bucket,key):
  listRows = []
  obj = s3.Object(bucket, key)

  # countLine = 1
  for line in obj.get()['Body']._raw_stream:
        s = StringIO(line.decode("utf-8"))
        linha = csv.reader(s, skipinitialspace=True)
        
        for row in linha:
          data={}
          # print("linha: "+str(countLine))
          data["id"]=str(uuid.uuid4()
          for i in range(len(collumns)-1):
            # print("coluna: " + str(i))
            data[collumns[i]] = row[i]
          
          listRows.append(data)
          # countLine += 1
          

  fileContent=""
  escapeChar = "\n"
  for row in listRows:
        fileContent += json.dumps(row)
        fileContent += escapeChar

  removal = escapeChar
  reverse_removal = removal[::-1]

  replacement = ""
  reverse_replacement = replacement[::-1]
  fileContent = fileContent[::-1].replace(reverse_removal,
                                    reverse_replacement, 1)[::-1]
  filename = key.split("/")[1] + ".json"
  print(filename)
  # tmpFile = "/tmp/" + filename 
  # print(tmpFile)
  # f = open(tmpFile, "a")
  # f.write(fileContent)
  # f.close()
  object = s3.Object(bucket, "json/"+filename)
  object.put(Body=fileContent.encode())
  # response = s3Client.put_object(
  #     Body=tmpFile,
  #     Bucket=bucket,
  #     Key="json/"+filename,
  # )

  # os.remove(tmpFile)


while True:
  receiptHandle, messageStr = getMessageFromQueue(urlSQS)
  if receiptHandle == None:
    print("nada")
    break
  else:
      print(messageStr)
      message = json.loads(messageStr)
      createJsonFromCSVInS3(message["bucket"], message["key"])
      deleteMessageFromQueue(urlSQS, receiptHandle)
# createJsonFromCSVInS3("teste-dms-rafbarbo", "files-small/inventory.part.00")
