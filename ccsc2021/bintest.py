num1 = "0b100"
num2 = "0b110"

sum = bin(int(num1, 2) + int(num2, 2))
print(sum[2:])
isum = str(sum[2:])
print(int(isum, 2))
