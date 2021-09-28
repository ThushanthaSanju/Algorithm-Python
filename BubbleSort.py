array1 = []

for v in range(8):
    array1.append(int(input("Enter the number : ")))

print(array1)

def bubbleSort(array):
    n=len(array)
    for i in range (0,n):
        for j in range(n-1,i,-1):
            if array[j]<array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]

bubbleSort(array1)
print("sorted array")
print(array1)























