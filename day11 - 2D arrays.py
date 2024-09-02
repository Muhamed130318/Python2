twoD = [] #empty 2D array

for _ in range(6):
    twoD.append(list(map(int, input().split()))) #for loop to input 6 lists in the 2D array

n = 0 #columns
m = 0 #rows
temp = 0 #temp sum of hourglass
res = -10000 #largest resulting hourglass, have to set it to large negative number because we could get all negative 2D array
for n in range(0, 4): #0-4 because we do n+2 on last column, 4+2=6 and this is a 6x6 2D array
    for m in range(0, 4): #0-4 because of same reason with rows
        top = twoD[n][m] + twoD[n][m+1] + twoD[n][m+2]
        mid = twoD[n+1][m+1]
        bottom = twoD[n+2][m] + twoD[n+2][m+1] + twoD[n+2][m+2]
        temp = ((top)+(mid)+(bottom))
        if temp > res:
            res = temp

print(res)