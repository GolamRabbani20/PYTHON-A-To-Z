import re
def hackerrankInString(s):
     print('YES' if re.search(r'.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*',s) else 'NO')
     #print( (re.search('.*'.join("hackerrank"), s) and "YES") or "NO")

for k in range(int(input())):
    hackerrankInString(input())