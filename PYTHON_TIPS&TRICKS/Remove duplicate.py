x = [1,2,3,5,56,6,56,85,5,5,5,5,5,3,312,2,3,3,32,21,2,1,21,2,1,12,25]
temp =  list(set(x))
print(temp)

most = max(set(x), key = x.count)
print(most)