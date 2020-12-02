#To remove white space we use strip()
txt="    Banana      "
print(txt)
print(txt[2]) #print 2 no indexed value that is white space

k=txt.strip()
print(k)

txt2="           I love Islam        "
print(txt2)
print(txt2.strip())