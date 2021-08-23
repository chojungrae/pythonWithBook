
# 선택정렬

ls = [5,2,3,1,4,9,6,7,8]


for i in range(len(ls)) :
    for j in range(i+1, len(ls)) :
        if ls[i] > ls[j] :
            ls[i], ls[j] = ls[j], ls[i]

print(ls)


