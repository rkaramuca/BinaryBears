scores = input()
a = 0
b = 0
n = len(scores)
i = 0
while i < n:
    if scores[i] == 'A':
        a += int(scores[i + 1])
    if scores[i] == 'B':
        b += int(scores[i + 1])
    i += 1
    
if a > b:
    print("A")
elif b > a:
    print("B")

        
