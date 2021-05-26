#Find sub Array

def sub_array(list1):
    sub_list=[[],]
    n=len(list1)+1
    for i in range(n):
        for k in range(i+1,n):
            m=list1[i:k]
            sub_list.append(m)
    return sub_list

s=[1,2,3,4]
print(sub_array(s))