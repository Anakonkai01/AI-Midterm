def getState(state, size):
    for i in range(size):
        temp = ""    
        for z in range(size):
            if state[z] == i+1:
                temp += str(state[z]) + " "
            else:
                temp += "- "
        print(temp)
       
def fn(p):

    row = [0]*16
    up_cross = [0]*31
    down_cross = [0]*31
    count = 0

    for i in range(16):
        count += row[p[i]-1]
        count += up_cross[(p[i]-1) + i]
        count += down_cross[(p[i]-1) - i + 15]
        row[p[i]-1] += 1
        up_cross[(p[i]-1) + i] += 1
        down_cross[(p[i]-1) - i + 15] += 1
        
    return 120 - count

a = [1,3,5,2,13,9,14,12,15,6,16,7,4,11,8,10] #Trường hợp thỏa yêu cầucầu
b = [3, 15, 1, 3, 12, 6, 4, 6, 16, 16, 16, 5, 9, 5, 12, 1] #Trường hợp ngẫu nhiên 
c = [1]*16 #Toàn bộ hậu ăn nhau
d = [1, 7, 9, 3, 14, 2, 10, 15, 4, 12, 5, 13, 11, 6, 0, 2]
d = [a + 1 for a in d] #Trường hợp thỏa do Hưng tìm được, +1 vì khác quy ước
print(fn([10, 5, 7, 2, 15, 6, 14, 16, 4, 9, 12, 3, 1, 8, 11, 13]))

