n = int(input("Enter a number: "))                      #count num of digits in a number
n = abs(n)
count = 0
for digit in str(n):
    count += 1
print("Number of digits:", count)


n = int(input("Enter a number: "))                         #count num of digits in a number
n = abs(n)
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1
print("Number of digits:", count)


n = int(input("Enter a number: "))                      #check if a number is prime or not
if n < 2:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


n = int(input("Enter a number: "))                      #reverse a number
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse:", rev)


n=int(input())                                          #count multiples of 3
count=0
for i in range(1,n+1):
  if i%3==0:
    count+=1
print(count)


n=int(input())                                          #sum of digits of a num
total=0
while n>0:
  digit=n%10
  total=total+digit
  n=n//10
print(total)


n=int(input())                                          #check palindrome
original=n
reverse=0
while n>0:
  digit=n%10
  reverse=reverse*10+digit
  n=n//10
if original==reverse:
  print("Palindrome")
else:
  print("Not")



n = int(input())                                        #armstrong of a number
temp = n
count = 0
if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp //= 10
print("Digit count:", count)
print("Powered sum:", total)

if total == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")