def rev(n):
 r=0
 while(n>0):

  d=n%10
  r=r*10+d
  n=n//10
 return r


a=int(input("enter the no.: "))
if a==rev(a):
 print("no. is palindrome")
else:
 print("no. is not palindrome")
print(rev(a))
