def bubbleSort(arr):
	n = len(arr)
	
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	print(arr)

arr = [9,2,5,2,7,3,7,2,1]

bubbleSort(arr)
