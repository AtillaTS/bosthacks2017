import csv

def data():
    d = {}
    with open("massachusetts.csv") as fbi:
        for line in fbi:
            x = line.rstrip("\n")
            x = x.split(",")
            d[x[0]] = x[1:]
            
    return d

    
