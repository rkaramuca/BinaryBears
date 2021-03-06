n = int(input())
case = input()
numbers = []

i = 0
j = 0
while j < n - 1:
    if j < 9:
        if i >= 1:
            if int(case[i]) != int(numbers[-1]) + 1 and int(case[i]) < int(numbers[-1]):
                numbers.append(case[i:i+2])
                i+=2
            else:
                numbers.append((case[i]))
                i+=1
        else:
            numbers.append(case[i])
            i+=1
    elif j < 98:
        numbers.append((case[i:i+2]))
        i+=2
    else:
        numbers.append((case[i:i+3]))
        i+=3
    j+=1

k = 0
while k <= len(numbers)-1:
    if int(numbers[-1]) != n:
        print(n)
        break
    elif int(numbers[0]) != 1:
        print(1)
        break
    elif int(numbers[k+1]) - int(numbers[k]) != 1:
        print(int(numbers[k+1]) - 1)
        break
    k+=1

