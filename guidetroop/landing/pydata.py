import csv

def data(name):
    d = {}
    with open("massachusetts.csv") as fbi:
        reader = csv.reader(fbi, skipinitialspace=True)
        for row in reader:
            d[row[0]] = row[1:]
            for i in range(len(d[row[0]])):
                d[row[0]][i] = d[row[0]][i].replace(',','')
                if d[row[0]][i] == '':
                    d[row[0]][i] = 0
                else:
                    d[row[0]][i] = int(d[row[0]][i])
                
            
    if name in d:         
        return d[name][9]/d[name][0]
    else:
        return 0

    
