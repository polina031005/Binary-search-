import sys
col1, col2 = input().split()
spisok1, spisok2 = sorted(list(map(int, input().split()))), list(map(int, input().split()))

if int(col1) == 1:
    for _ in range(int(col2)):
        print(spisok1[0])
    sys.exit()
        
for i in range(int(col2)):
    co, s_k1 = int(col1), spisok1 
    
    while len(s_k1) > 2:
        co = round(co/2)
        
        if s_k1[co] > spisok2[i]:
            s_k1 = s_k1[:co + 1]
        elif s_k1[co] < spisok2[i]:
            s_k1 = s_k1[co:]
        else:
            result = spisok2[i]
            break

    if abs(s_k1[0] - spisok2[i]) <= abs(s_k1[1] - spisok2[i]):
        result = s_k1[0]
    elif abs(s_k1[0] - spisok2[i]) > abs(s_k1[1] - spisok2[i]):
        result = s_k1[1]
    else:
        break
    
    print(result)
