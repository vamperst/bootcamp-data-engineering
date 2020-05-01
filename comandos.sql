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

insert into inventory2
(BibNum,Title,Author,ISBN,PublicationYear,Publisher,Subjects,ItemType,ItemCollection,FloatingItem,ItemLocation,ReportDate,ItemCount)
values
(),
(),
