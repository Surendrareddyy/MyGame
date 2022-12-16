
import random

from deepdiff import DeepDiff

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

Dictionary1 = {1 : "Surendra", 2 : "Surendra", 3 : "Surendra", 4 : "Surendra" }
Dictionary2 = {5 : "Meera", 6 : "Meera", 7 : "Meera", 8 : "Meera"}

Dictionary = Dictionary1.copy()
Dictionary.update(Dictionary2)

print(Dictionary)


# shuffling values
temp = list(Dictionary.items())
random.shuffle(temp)
  
# reassigning to keys
res = dict(temp)

print("The shuffled dictionary : " + str(res))


# Using items() + len() + list slicing
# Split dictionary by half
res1 = dict(list(res.items())[len(res)//2:])
res2 = dict(list(res.items())[:len(res)//2])





# printing result 
print("The first half of dictionary : " + str(res1))
print("The second half of dictionary : " + str(res2))



while(res1 != Dictionary1 and res2 != Dictionary2 and res1 != Dictionary2 and res2 != Dictionary1 ):

    s = random.choice(list(res1.items()))

    s = Convert(s)

    res2.update(s)

    for key in s.keys():
        res1.pop(key,None)

    s = random.choice(list(res2.items()))

    s = Convert(s)

    res1.update(s)
    for key in s.keys():
        res2.pop(key,None)

    #print(DeepDiff(Dictionary1, res1))
    #print(DeepDiff(Dictionary2, res1))
    #print(DeepDiff(Dictionary1, res2))
    #print(DeepDiff(Dictionary2, res2))

    res1 = dict(sorted(res1.items()))
    res2 = dict(sorted(res2.items()))

    print(res1)
    print(res2)

    #print("Next ")
    

if res1 == Dictionary1 or res1 == Dictionary2:
   print("I win " + str(res1) )
elif res2 == Dictionary2 or res2 == Dictionary1:
   print("I win " + str(res2) )
else :
   print("Wrong System")





#def function(n):
#   from random import randrange
#   values = ['value1', 'value2']
#   mydict = {"key " + str(i): values[0] for i in range(n)}
#   mydict["key " + str(random.randrange(n))] = values[1]

#   return mydict

#mydict = function(4)

#print(mydict)
