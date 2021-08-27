for i in range(int(input())):
	nums = {
		'1': '1',
		'2': '2',
		'5': '5',
		'6': '9',
		'8': '8',
		'9': '6',
		'0': '0'
	}
	x = input()
	y = ""
	for n in x:
		if n in nums:
			y += nums[n]
	if y[::-1] == x:
		print("Yes")
	else:
		print("No")
