def printList(pList):
    for data in pList:
        print(data, end='\t')
    print()


with open("../CSV/SINGER1.CSV", "r") as inFp:
    header = inFp.readline()
    print(header)
    header = header.strip()
    header_list = header.split(',')
    printList(header_list)
    for inStr = inFp.readline()
        inStr = inStr.strip()
    row_list = inStr.split(",")
    printList(row_list)
