#Python Program to Generate Gray Codes using Recursion
def get_gray_codes(n):
    if n==0:
        return [""]
    else:
        first_half=get_gray_codes(n-1)
        second_half=first_half.copy()

        first_half=['0'+ code for code in first_half]
        second_half=['1'+ code for code in reversed(second_half)]
    return first_half + second_half

n=int(input("Enter a number:"))
p=get_gray_codes(n)
print("All {}-bit gray codes".format(n))
print(p)