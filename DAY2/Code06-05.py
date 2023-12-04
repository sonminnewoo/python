# csv 미사용 // 사용한건 usecsv 라는 파일
with open('./python/CSV/singer1.csv', 'r') as inFp:
    # 이파일 을 읽어서 
    with open('./python/CSV/singer1_out.csv', 'w') as outFp:
        header = inFp.readline() # inFp 파일을 한줄 읽고
        header = header.strip() # 읽은걸 공백제거하고
        header_list = header.split(',') # 헤더 지정하고 split 문자열을 끊어서 header_list 에 넣고 
        idx1=header_list.index('아이디') # 변수 만들어서 인덱스순으로 문자 아이디, 이름, 편균키 적음
        idx2=header_list.index('이름')  
        idx3=header_list.index('평균 키')
        header_list = [header_list[idx1],header_list[idx2],header_list[idx3],]
        # 리스트에 받는 인덱스를 넣고 
        # print(header_list)
        # list 를 문자열로 변환

        int(input())
        header_str = ','.join(map(str,header_list)) # map 은 함수를 넣고 반복되어야할 객체를 지정해준다 /문자열 함수를 넣고 
        outFp.write(header_str + '\n')
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            if int(row_list[idx3]) >= 165 : 
                row_list = [row_list[idx1],row_list[idx2],row_list[idx3]]
                #  list 를 문자열로 변환
                row_str = ','.join(map(str,row_list))
                outFp.write(row_str + '\n')