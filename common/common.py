import sys
sys.path.append("..")
import csv

def getCsv(file_name):
    rows=[]
    with open(file_name,encoding='utf-8') as f:
        readers = csv.reader(f)
        for row in readers:
            rows.append(row)
    rows.pop(0)
    return rows


# getCsv('../TestData/testadd.csv')
