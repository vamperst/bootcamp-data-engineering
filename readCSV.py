
import csv
import json
from io import StringIO
import boto3


s3 = boto3.resource('s3')

collumns = ["BibNum", "Title", "Author",
            "ISBN", "PublicationYear", "Publisher", "Publisher", 
            "Subjects", "ItemType", "ItemCollection", "FloatingItem", 
            "ItemLocation", "ReportDate", "ItemCount"]

pathToFile='test.csv'
listRows = []
obj = s3.Object("teste-dms-rafbarbo", "files-small/inventory.part.00")

for line in obj.get()['Body']._raw_stream:
      s = StringIO(line.decode("utf-8"))
      linha = csv.reader(s, skipinitialspace=True)
      for row in linha:
        data={}
        for i in range(len(collumns)-1):
          data[collumns[i]] = row[i]
        
        listRows.append(data)
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
f = open("inventory.part.00.json", "a")
f.write(fileContent)
f.close()
# print(json.dumps(listRows))

# print(len(listRows))
