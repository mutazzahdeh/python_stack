# 1 Biggie Size 
print(1,"__"*30)
def BiggieSize(arr):
   
    for x in range  (0,len(arr),1):
        if arr[x]<0:
            arr[x]="big"
    return arr
print(BiggieSize([-1, 3, 5, -5]))
print(2,"__"*30)
def CountPositives(arr):
    count=0
    for x in range (0,len(arr),1):
        if arr[x]>0:
            count+=1
    arr[-1]=count
    return arr
print(CountPositives([-1,1,1,1]))
print(3,"__"*30)
# 3 Sum Total 
def SumTotal(arr):
    sum =0
    for x in range (0,len(arr)):
        sum+=arr[x]
    return sum
print(SumTotal([1,2,3,4]))
print(4,"__"*30)
# 4 Average

def Average(arr):
    sum =0
    for x in range (0,len(arr)):
        sum+=arr[x]
    return sum/len(arr)
print(Average([1,2,3,4]))
print(5,"__"*30)
# 5 Length 
def Length(arr):
    return len(arr)

print(Length([37,2,1,-9]))
print(6,"__"*30)
# 6 Minimum
def Minimum(arr):
    min=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<min:
            min=arr[i]
    return min
print(Minimum([37,2,1,-9]))
print(7,"__"*30)
# 7 Minimum
def maximum(arr):
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max
print(maximum ([37,2,1,-9]))
print(8,"__"*30)
# 8 Ultimate Analysis
def UltimateAnalysis(arr):
    max=arr[0]
    min=arr[0]
    sum=0
    for i in range (0,len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    sum+=arr[i]
    x=["sum Total:",sum,"Avarage:",sum/len(arr),"minimum:",min,"maximum:",max,"length:",len(arr)]
    return x
print (UltimateAnalysis([37,2,1,-9]))
print(9,"__"*30)
# 9 Reverse List 
def ReverseList(arr):
    
    x=arr[::-1]
    return x

print (ReverseList([37,2,1,-9]))
    