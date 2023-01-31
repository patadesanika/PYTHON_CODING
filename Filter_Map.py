nums=[1,2,3,4,5,6,7,8,9,10]
even=list((filter(lambda n:n%2==0,nums)))
print(even)
doubles=list(map(lambda n:n*2,even))
print(doubles)
#sum=reduce(lambda a,b:a+b,nums)
#print(sum)