#map(function,list)

def squere(x):
    return x*x
n=[2,3,42,5,60]
result=list(map(squere,n))
"""
map function ta akta itareable object itself return kore
tai ata k list a convert korte hoy
"""
print(result)