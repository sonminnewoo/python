inFp = open('./python/CSV/singer1.csv', 'r') # input File 

intStr = inFp.readline()
print(intStr, end="")

intStr = inFp.readline()
print(intStr, end="")

intStr = inFp.readline()
print(intStr, end="")

inFp.close()
