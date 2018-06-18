import csv

list = []
def read_file(project = '', row1='', row2=''):
    with open(project) as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             # print row
             print(row[row1], row[row2])
             list.append(row[row1])
    return(list)
