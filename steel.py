
import xlrd
from collections import OrderedDict
import simplejson as json
import boto3

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('/home/consultadd/Downloads/ISO10383_MIC.xls')
sh = wb.sheet_by_index(1)

# List to hold dictionaries
list = []

# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    cars = OrderedDict()
    row_values = sh.row_values(rownum)
    cars['ISO COUNTRY CODE (ISO 3166)'] = row_values[0]
    cars['COUNTRY'] = row_values[1]
    cars['MIC'] = row_values[2]
    cars['OPERATING MIC'] = row_values[3]
    cars['O/S'] = row_values[4]
    cars['NAME-INSTITUTION DESCRIPTION'] = row_values[5]
    cars['ACRONYM'] = row_values[6]
    cars['CITY'] = row_values[7]
    cars['WEBSITE'] = row_values[8]
    cars['STATUS DATE'] = row_values[5]
    cars['STATUS'] = row_values[6]
    cars['CREATION DATE'] = row_values[7]
    cars['COMMENTS'] = row_values[8]

    list.append(cars)

# Serialize the list of dicts to JSON
j = json.dumps(list)

# Write to file
with open('data.json', 'w') as f:
    f.write(j)

client = boto3.resource('s3')
client.Bucket('mybucket-steel').upload_file('/home/consultadd/Desktop/python/data.json', 'hello.json')