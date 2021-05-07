# 1 Countdown 
def Countdown(num=5):
    x=[]
    y=0
    for y in range (num,0,-1):
      x.append(num)
      num-=1
       
    return x
print (Countdown())

# 2 Print and Return
def PrintandReturn(arr):
    print(arr[0])
    return arr[1]

print( PrintandReturn([1,2]))

# 3 First Plus Length

def FirstPlusLength(arr):
   return arr[0]+len(arr)

print( First Plus Length([1,2,3,4,5]))

# 4 Values Greater than Second 
def ValuesGreaterthanSecond (arr):
    if len(arr)<=2: 
        return "False"
    x=[]
    for y in range (0,len(arr),1):
        if arr[y]>arr[1]:
            x.append(arr[y])
    return x
print( ValuesGreaterthanSecond([5,2,3,4,1,0]))

# 5 This Length, That Value
def ThisLengthThatValue(num1,num2):
    x=[]
    for y in range (0,num1,1):
        x.append(num2)
    return x
print(ThisLengthThatValue(7,4))
    

