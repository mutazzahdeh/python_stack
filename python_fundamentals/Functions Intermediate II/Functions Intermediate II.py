 # 1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
print(x)
students[0]['last_name']="Bryant"
print(students)
sports_directory['soccer'][0]="Andres"
print(sports_directory)
z[0]['y']=30
print(z)

# 2 Iterate Through a List of Dictionaries

def iterateDictionary(arr):
    for i in range(0,len(arr)):
        print(f"first name - {arr[i]['first_name']}, Last-name- {arr[i]['last_name']}")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# 3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name,arr):
    for i in range (0,len(arr)):
        print(arr[i][key_name])
iterateDictionary2('first_name', students)
# 4 Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    y=7
    r=list(some_dict.keys())
    print(r)
    for i in range (0,len(r)):
        print(f"{y} {r[i]}")
        for j in range (0,len(some_dict[r[i]])):
            print(some_dict[r[i]][j])
        y+=1
    

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)