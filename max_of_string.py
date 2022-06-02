def largest_alphabet(a, n) :
	
	max = 'A'

	for i in range(n) :
		if (a[i] > max):
			max = a[i]

	return max

a = input()
size = len(a)
	
print(largest_alphabet(a, size))