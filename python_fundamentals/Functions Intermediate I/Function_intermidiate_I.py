import random
def randInt(min =0, max=0 ):
    if min==0 and max==0:
       return int(random.random()*100)
    elif max>0 and min==0:
        return int(random.random()*max)
    elif max==0 and min>0:
        return int(random.random()*min+(100-min))
    elif max>0 and min>0:
        return int(random.random()*min+(max-min))

    
print (randInt())
print(randInt()) 	
print(randInt(max=50)) 	
print(randInt(min=50)) 	
print(randInt(min=50, max=500))   
 
