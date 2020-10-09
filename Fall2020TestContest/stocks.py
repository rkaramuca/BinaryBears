stocks = {
	'Goog' : 5200.54,
	'FB'   : 76.45,
	'yhoo' : 39.28,
	'AMZN' : 306.21,
	'APPL' : 99.76
	}

zipped_1 = zip(stocks.values(), stocks.keys())
print(sorted(zipped_1))

