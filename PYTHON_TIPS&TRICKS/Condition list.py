like = 10000
comment = 2000
share = 5000

#if like > 5000 and comment > 1500 and share > 3000:
conditions = [
    like > 5000,
    comment > 1500,
    share > 30000
]
if all(conditions):
    print("Awesome video")

#if like > 5000 or comment > 1500 or share > 3000:
if any(conditions):
    print("Awesome video2")

x = 500
y = 100
conditions2 = [
    x > 120,
    y < 150
]

if all(conditions) and all(conditions2):
    print("Awesome120")

if all(conditions) or all(conditions2):
    print("Good")