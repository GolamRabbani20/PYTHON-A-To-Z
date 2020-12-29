like = 150
love = 200
print(like,love)

temp = like
like = love
love = temp

print(like,love)

like = 200
love = 300
like, love = love, like
print(like,love)