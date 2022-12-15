

Dictionary1 = {1 : "Surendra", 2 : "Surendra", 3 : "Surendra", 4 : "Surendra" }
Dictionary2 = {5 : "Meera", 6 : "Meera", 7 : "Meera", 8 : "Meera"}

Dictionary = Dictionary1 + Dictionary2

print(Dictionary)



import random

Dictionary1 = {1 : "Surendra", 2 : "Surendra", 3 : "Surendra", 4 : "Surendra" }
Dictionary2 = {5 : "Meera", 6 : "Meera", 7 : "Meera", 8 : "Meera"}

Dictionary = Dictionary1.copy()
Dictionary.update(Dictionary2)

print(Dictionary)


# shuffling values
temp = list(Dictionary.values())
random.shuffle(temp)
  
# reassigning to keys
res = dict(zip(Dictionary, temp))

print("The shuffled dictionary : " + str(res))


# Using items() + len() + list slicing
# Split dictionary by half
res1 = dict(list(res.items())[len(res)//2:])
res2 = dict(list(res.items())[:len(res)//2])


# printing result 
print("The first half of dictionary : " + str(res1))
print("The second half of dictionary : " + str(res2))



for i in range(len(Dictionary1)):

    print(random.choice(list(Dictionary1.items())))
