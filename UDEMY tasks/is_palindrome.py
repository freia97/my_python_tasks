number = int(input("Enter number:"))
temp = number
rev = 0
while number > 0:
    dig = number % 10
    rev = rev * 10 + dig
    print(rev)
    number = number // 10
if temp == rev:
    print("palindrome")
else:
    print("no palindrome!")