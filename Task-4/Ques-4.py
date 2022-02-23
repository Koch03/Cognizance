num=int(input("enter a no: "))
original=num
reverse=0
while(num>0):
    dig=num%10
    reverse=reverse*10+dig
    num=num//10
if(original==reverse):
    print("The Given no is a palindrome Number")
else:
    print("The Given no is not a palindrome Number")