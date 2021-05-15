def sort(arr):
    for i in range (0,len(arr)):
        for j in range (0,len(arr)):
            if(arr[i]<arr[j]):
                arr[i]=arr[j]+arr[i]
                arr[j]=arr[i]-arr[j]
                arr[i]=arr[i]-arr[j]
    return arr


print( sort([5,3,4,8,7,9,6,7]))