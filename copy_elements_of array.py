arr1=[1,2,3,4,5,10,20,30]
arr2=[None]*len(arr1)

for i in range(0,len(arr1)):
    arr2[i]=arr1[i]
    
print('elements of original array:')

for i in range(0,len(arr2)):
    print(arr1[i])
    
print()

print("elements of new array:")
for i in range(0,len(arr2)):
    print(arr2[i])