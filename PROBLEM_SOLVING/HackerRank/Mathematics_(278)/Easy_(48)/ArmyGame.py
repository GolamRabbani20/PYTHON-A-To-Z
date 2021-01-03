"""We can think like this : 2*2 's will need one drop: If any row or column is not divisible by 2 then one entire row or column will remain at the end ! Now suppose that row is odd :
Each 2 areas will need 1 drop: Now if we add additional row we are those will have 2*2 pairs again but it wont change the no of supplies(because 2 and 2*2 both require one drop) We can
imagine similar for column."""
n, m = map(int,input().split())
n = n + n % 2
m = m + m % 2
#k = ceil(n/2) * ceil(m/2)  Or p =  (n+1)//2 * (m+1)//2
print(n*m//4)