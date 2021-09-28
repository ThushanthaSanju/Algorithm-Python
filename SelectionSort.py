array1 = []

for v in range(6):
    array1.append(int(input("Enter the number : ")))

print(array1)
def selectionSort(array):
    n = len(array)
    for j in range(0,n-1):
        smallest=j
        for i in range(j+1,n):
            if array[i]<array[smallest]:
                smallest=i
        array[j],array[smallest]=array[smallest],array[j]

selectionSort(array1)
print("sorted array")
print(array1)


















