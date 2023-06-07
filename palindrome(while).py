n=int(input("Enter the number:"))
temp=n
Rev=0
while(n>0):
    dig=n%10
    Rev=Rev*10+dig
    n=n//10
if(temp==Rev):
   print("Num is palindrome")
else:
    print("num is not a palindrome")