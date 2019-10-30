def search(arr, l, r, x):
	if r >= l:
		m = (l+r)/2
		if arr[m] == x:
			return m

		if arr[m] > x:
			return search(arr, l, m-1, x)

		else:
			return search(arr, m, r, x)

	return -1

def exponentialSearch(arr, n, x):

	if arr[0] == x:
		return 0

	i = 1
	while i<n and arr[i] <=x:
		i = i*2

	return search(arr, i/2, min(n, i), x)

arr = [2, 3, 4, 7, 10, 40] 
n = len(arr) 
x = 10
r = exponentialSearch(arr, n, x) 
if r == -1: 
    print "Element not found"
else: 
    print "Element is present at index %d" %(r) 
