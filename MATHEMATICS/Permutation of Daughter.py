# Vowel gulo k pasha pashii na rekhe "Daughter" word tir permutation ber koro

def CalculatePermutation(word):
    vowel=0
    Len=len(word)
    for i in range(Len):
        if word[i]=='a' or word[i]=='e' or word[i]=='i' or  word[i]=='o' or word[i]=='u':
            vowel+=1

    return Factorial(Len)-(Factorial(Len-vowel+1)*Factorial(vowel))

def Factorial(n):
    if n==1:
        return 1
    return n*Factorial(n-1)

word=input().lower()
print(CalculatePermutation(word))