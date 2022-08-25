def add(x,y):

  return x+y

def sub(x,y):

  return x-y

def mul(x,y):

  return x*y

def div(x,y):

  return x/y

print("Select the operation")

print("1.add")

print("2.sub")

print("3.mul")

print("4.div")

#take input from user

choice=input("Enter the choice(1/2/3/4/5):")

num1 = int(input("Enter the first number"))

num2 = int(input("Enter the second number"))

if choice=='1':

 print(add(num1,num2))

elif choice=='2':

 print(sub(num1,num2))

elif choice=='3':

 print(mul(num1,num2))

elif choice=='4':

 print(div(num1,num2))

else:

  print("invalid input")
