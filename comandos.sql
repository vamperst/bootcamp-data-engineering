 mysql -u admin -p -h  test.cuxawkyva3nw.us-east-1.rds.amazonaws.com test --local-infile

LOAD DATA LOCAL INFILE '/home/ubuntu/environment/seattle-library-collection-inventory/library-collection-inventory.csv' 
INTO TABLE test3
FIELDS 
    TERMINATED BY ',' 
    ENCLOSED BY '"'
LINES 
    TERMINATED BY '\n'
IGNORE 1 LINES;


split -d -l 1000000 library-collection-inventory.csv files/inventory.part.

mysqlimport --fields-terminated-by=, --fields-enclosed-by='"' --lines-terminated-by=\n --verbose --local -h test-hackathon.cuxawkyva3nw.us-east-1.rds.amazonaws.com -u admin -pBushyto09 test inventory.part.00

for i in {01..35}
do
    mysqlimport --fields-terminated-by=, --fields-enclosed-by='"' --lines-terminated-by=\n --verbose --local -h test-hackathon.cuxawkyva3nw.us-east-1.rds.amazonaws.com -u admin -pBushyto09 test inventory.part.$i
done

CREATE EXTERNAL TABLE `test_fire`(
  `bibnum` int COMMENT 'from deserializer', 
  `title` string COMMENT 'from deserializer', 
  `author` string COMMENT 'from deserializer', 
  `isbn` string COMMENT 'from deserializer', 
  `publicationyear` string COMMENT 'from deserializer', 
  `publisher` string COMMENT 'from deserializer', 
  `subjects` string COMMENT 'from deserializer', 
  `itemtype` string COMMENT 'from deserializer', 
  `itemcollection` string COMMENT 'from deserializer', 
  `floatingitem` string COMMENT 'from deserializer', 
  `itemlocation` string COMMENT 'from deserializer', 
  `reportdate` string COMMENT 'from deserializer', 
  `itemcount` int COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'
LOCATION
  's3://teste-dms-rafbarbo/python'