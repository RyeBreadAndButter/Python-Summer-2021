word = 'ABAC'
len(word)
x = 0
y = 1

while y < len(word):
    print(word[0+x:y+x])
    x = x + 1
    if (x >= len(word)):
        y = y + 1
        x = 0