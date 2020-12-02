def StrangeCounter(t,n):
    while 3*(n-1)<t:                    # ai loop ar kaj hoilo 2^n calculate kara
        n*=2
    return 3*(n-1)-t+1

t=int(input())
n=2
print(StrangeCounter(t,n))

"""
Explanation:

If you look carefully, the last 'time' value of cycle1 is 3, which is 3*1=3*(2^1-1), the last 'time' value of cycle2 is 9, which is 3*3=3*(2^2-1), 
the last 'time' value of cycle3 is 21, which is 3*7=3*(2^3-1). So, we should keep doubling n, which represents the 2^1, 2^2, 2^3 part. Hence the while loop. 
The loop stops when it reaches to a cycle whose max time is greater than the real time t, then we know that it has reached the last cycle.And taking the second 
cycle as an example, 'time' 7 has 'value' 3, and the max time of the second cycle is 9. We find the relationship between them is 3 = 9 - 7 + 1, 
which is why we print (3 * (n - 1) - t + 1) to get the output of 3 when t is 7.

Last time of cycle1 is 3 = 3*1 =3*(2^1-1)
Last time of cycle2 is 9 = 3*2 =3*(2^2-1)
Last time of cycle3 is 21 = 3*7 =3*(2^3-1)
Last time of cycle4 is 45 = 3*15 =3*(2^4-1)
Last time of cycle5 is 93 = 3*31 =3*(2^5-1)
...........................................
...........................................
Last time of cycle-n is 3 = 3*n =3*(2^n-1)

max_time_of_the_nth_cycle - real_time + 1
           3*(n-1)        -   t       + 1       (result)
"""