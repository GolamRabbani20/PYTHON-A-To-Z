#Python program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple
def last(n):
    return n[-1]


def sort(tuples):
    return sorted(tuples, key=last)

a = input("Enter a list of tuples:")
print("Sorted list is:",sort(a))