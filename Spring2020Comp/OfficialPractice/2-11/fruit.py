f = {}
p = {}

count = 0
fp = ""
while True:
    fp = input()
    if fp == "END_PRICES" or fp == "QUIT":
        break
    else:
        fp = fp.split()
        f[count] = fp[0]
        p[count] = float(fp[1])
        count += 1

fp = ""
total = 0.00
sent = "dont quit"
while sent != "QUIT":
    fp = input()
    fp = fp.split()
    for i in range(len(f)):
        if fp[0] == f[i]:
            total += (p[i] * int(fp[1]))  
    if fp[0] == "END_INVOICE":
        print(f"Total: {total}")
        total = 0.00
    if fp[0] == "QUIT":
        sent = "QUIT"
