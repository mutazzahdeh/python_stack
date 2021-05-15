def Insertion_Sort(arr):
    temp=0
    loc=0
    for i in range (1,len(arr)):
        if arr[i]<arr[i-1]:
            temp=arr[i]
            loc=i
            
            arr[loc]=arr[loc-1]
            loc-=1

            while loc>0 and arr[loc-1]>temp:
                arr[loc]=temp
                arr[loc]=arr[loc-1]
                loc-=1
    return arr
print(Insertion_Sort([2,5,8,4,8,36,4,65]))