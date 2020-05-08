import csv
import json
from io import StringIO
import os
import boto3
import uuid


s3 = boto3.resource('s3')
s3Client = boto3.client('s3')
sqs = boto3.client('sqs')

collumns = ["BibNum", "Title", "Author",
            "ISBN", "PublicationYear", "Publisher", "Publisher", 
            "Subjects", "ItemType", "ItemCollection", "FloatingItem", 
            "ItemLocation", "ReportDate", "ItemCount"]


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
          data["id"]=str(uuid.uuid4())
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
 
  object = s3.Object(bucket, "json/"+filename)
  object.put(Body=fileContent.encode())


def handler(event, context):
    print(str(event))
    
    for record in event['Records']:
        message=json.loads(record['body'])
        bucket = message["bucket"]
        key = message["key"]
        
        createJsonFromCSVInS3(bucket,key)