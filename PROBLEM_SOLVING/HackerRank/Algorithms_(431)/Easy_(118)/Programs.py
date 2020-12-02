from string import ascii_lowercase as x
def Program(str):
    return set(x)-set(str.lower())

if Program(input()):
    print("not pangram")
else:
    print("pangram")