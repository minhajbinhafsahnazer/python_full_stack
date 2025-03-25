# 1 
# 2 4 
# 3 6 9 
# 4 8 12 16 
# 5 10 15 20 25

n = 6
num = 1
for i in range(n):
    for j in range(1,i+1):
        print(i*j,end=" ")
        num+=1
    print()



