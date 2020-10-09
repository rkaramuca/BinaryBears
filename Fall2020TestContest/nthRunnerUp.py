nth = input()
nth = int(nth)
scores = []

cases = input()
cases = int(cases)
for i in range(cases):
	score = input()
	if not score in scores:
		scores.append(int(score))
    
scores.sort(reverse=True)
scores.pop(0)
if nth > len(scores):
    print(f"The {nth}-th runner up score is -1.")
else:
    print(f"The {nth}-th runner up score is {scores[nth]}.")
