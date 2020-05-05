pip install kaggle
npm install -g serverless
pip3 install boto3

vim ~/.kaggle/kaggle.json
mkdir seattle-library-collection-inventory
kaggle datasets download -d city-of-seattle/seattle-library-collection-inventory
unzip seattle-library-collection-inventory.zip
rm seattle-library-collection-inventory.zip 
mkdir files-small
split -d -l 100000 library-collection-inventory.csv files-small/inventory.part.
sed -i '$d' files-small/inventory.part.00
aws s3 cp --recursive ~/environment/seattle-library-collection-inventory/files-small/ s3://bootcamp-fiap-rafael/files-small/
querys padrão ====> s3://bootcamp-fiap-rafael/querys-athena/