#Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated
# Sequence after Sorting them Alphabetically

print("Enter s sequence:",end="")
lis=[n for n in input().split("-")]
lis.sort()
print("-".join(lis))

