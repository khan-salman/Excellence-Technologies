#sum of List
def sumOfList(x):
    sumList=0
    for i in x:
        sumList=sumList+i
    return sumList

y=[1,2,3]
#sumOfList(y)


dic1={"1" : 50,"2" : 60,"3" : 70,"4":23,"5":90}

#maximum in Dictionary
def maxDic(dic1):
    maximum=0
    key=0
    k={}
    for i,j in dic1.items():
        if(j>maximum):
            maximum=j
            key=i
            
    
    print({key:maximum})
            
#maxDic(dic1)

#Consecutive one's

list1=[0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1]

def consecutiveOne(x):
    slow, fast, glo_max, loc_max = 0, 0, 0, 0
    while fast < len(x):
        if x[fast] == 0:
            loc_max = fast - slow  
            glo_max = max(glo_max, loc_max)
            slow = fast + 1      # need to add one more because we haven't incremented fast yet

        fast += 1
    loc_max = fast - slow        # end check for cases that end with 1
    return print(max(loc_max, glo_max))
    
            
consecutiveOne(list1)
