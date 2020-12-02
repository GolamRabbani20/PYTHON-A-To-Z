n=[1,2,3,4,5,6,10,12]

result=list(filter(lambda x:x%2==0,n))
r=list(filter(lambda x:x%2==1,n))

"""
filter function ta akta itareable object itself return kore
tai ata k list a convert korte hoy
"""
print(result)
print(r)