batches={"ppa":16500,
         "lb":17000,
        "python":16500 ,
        "Angular":15000
        }
print("data  of dictonary is",batches)
print("-----------------------------------")
print("--------Data travsersal using loop---------------------")

for x in batches:
    print(x,end=" ")
print()
print("-----------To display dictionary key and value-----------------")
for x in batches:
    print(x,batches[x])
    
print("-------------using another method to get key value pair---------------")
for a in batches:
    print(x,batches.get(x))

print("-------------------to display the keys of dictionary------------------- ")
keysbatches=batches.keys()
print(keysbatches)
print(type(keysbatches))

print("---------To dipslay only values of dictionary-------------------")
valesbatches=batches.values()
print(valesbatches)

# for i in range(0,len(batches)):
#     print("Batches are:-",keysbatches[i],end=" ")
#     print("Fees are",valesbatches[i])