##Prime Numbers
start=int(input("enter the starting interval"))
end=int(input("enter the ending interval"))

for n in range(start,end+1,1):
  if n > 1:
      for j in range(2,n):
          if(n%j == 0):
             break
      else:
           print(n)
##Factorial of Numbers
num=int(input("enter a number"))
fact=1
if num > 0:
    for i in range(1,num+1,1):
        fact=fact*i
    print("Factorial of number=",fact)
elif num <0:
    print("Factorial of Negative numbers can\'t find")
elif num == 0:
    print("0 factorial is 1")

##Sum of Numbers
num=int(input("enter a number"))
sum=0
while num!=0:
    sum=sum+(num%10)
    num=num//10
print("Sum of number is=",sum)