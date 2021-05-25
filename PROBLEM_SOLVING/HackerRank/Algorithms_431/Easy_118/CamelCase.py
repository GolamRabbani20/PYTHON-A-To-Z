import re
def CamelCaseUsingRegularExpression(s):
    return len(re.findall(r'[A-Z]', s)) + 1

def CamelCase(s):
    count = 1
    for i in range(len(s)):
        if s[i]>='A' and s[i]<='Z':
            count += 1
    return count

s = input().strip()

print(CamelCase(s))
print(CamelCaseUsingRegularExpression(s))

