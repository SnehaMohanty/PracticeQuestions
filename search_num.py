def search(arr,n,x):
	for i in range(0,n):
		if(arr[i]==x):
			return i
	return -1



arr = [1,2,3,4,7,10]
x = 10
n = len(arr)

result = search(arr,n,x)
if(result == -1):
	print('Element not present in array')

else:
	print('Element present at', result)
