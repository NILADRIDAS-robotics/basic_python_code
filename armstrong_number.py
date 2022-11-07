n=int(input("enter a no:"))
sum=0

temp=n
while temp>0:
    d=temp%10
    sum+=d**3
    temp//=10
if n ==sum:
    print(n,'is an armstrong number')
else:
    print(n,'is not a armstrong no')