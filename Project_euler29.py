''' Project Euler num 29: Distinct Powers '''



ls = []
for i in range(2, 101):
    #print('Current i is', i)
    for j in range(2, 101):
        num = i**j
        if(num not in ls):
            ls.append(num)

print('\n')
print("Number of distinct powers is ",len(ls))

