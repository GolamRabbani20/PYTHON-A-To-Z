def multipole_parameter(*a):
    result = 0
    for i in a:
        result += i
    return result

sum = multipole_parameter(2,5,6,8,9,10)
print(sum)  