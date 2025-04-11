while 1 :
    try :
        n = int(input())
        cnt = 1
        length = 1
        while 1:
            
            if cnt % n == 0:
                
                print(length)
                break
            else :
                
                length += 1
                cnt = (cnt*10+1)
    except :
        break