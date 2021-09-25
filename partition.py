#creating an empty list

lst = []

#ask num of elements

n= int(input("Number of elements quick sort"))

print("Enter Numbers : ")
for i in range (0,n):
    ele=int(input())
    lst.append(ele)

print(lst)

#partition function
def partition(Array,low,high):
    i=(low-1)
    pivot=Array[high]#pivot

    for j in range(low,high):
        #if current is smaller
        if Array[j]<=pivot:
            i=i+1
            Array[i],Array[j]=Array[j],Array[i]
    Array[i+1],Array[high]=Array[high],Array[i+1]
    return (i+1)

def quickSort(arr,low,high):
    if low<high:
        #partition index
        pi=partition(arr,low,high)
        #after partition
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

#call quicksort
quickSort(lst,0,n-1)
print(lst)