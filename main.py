#creating an empty list

lst = []

#ask num of elements

n= int(input("Number of elements"))

print("Enter Numbers : ")
for i in range (0,n):
    ele=int(input())
    lst.append(ele)

print(lst)

#function to so insertionSort
def insertionSort(arr):
    #Traverse through 1 to lenth of array
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

#calling funtion
insertionSort(lst)
#printing
print("Sorted array : ")
for i in range(len(lst)):
    print("%d" %lst[i])
