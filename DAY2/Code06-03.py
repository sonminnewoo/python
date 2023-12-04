def printList(pList):
    for data in pList:
        print(data, end='\t')
    print()

with open('./python/CSV/singer1.csv', 'r') as inFp:
    # 절대 위치도 이런 방식으로 지정할수 있다 .
    header = inFp.readline()
    # print(header)
    header = header.strip()
    header_list = header.split(',')
    printList(header_list)

    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)

#  test06 보다 훨씬더 간결하게 표현할수 있다 
    