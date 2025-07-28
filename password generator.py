import random,string
letters=string.ascii_letters
num=string.digits
sym="@#$%^&!"
print("welcome to the password generator!")
n=int(input("how many letters would you like in your password"  ))
p=int(input("enter how many digits you want"))
l=int(input("enter how many symbols you want "))
s=" "
for i in range(1,n+1):
   s+=random.choice(letters)
for j in range (1,n+1):
    s+=random.choice(num)
for k in range(1,n+1):
    s+=random.choice(sym)
print(s)
