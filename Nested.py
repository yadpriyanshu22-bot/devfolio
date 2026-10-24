n=int(input())                    #print a right triangle
for i in range(1, n+1):
  for j in range(i):
    print("*",end=" ")
  print()


n=int(input())                    #print an inverted right triangle
for i in range(n,0,-1):
  for j in range(i):
    print("*",end=" ")
  print()


n = int(input())                  #print numbers in a row
for i in range(1, n + 1):         # 1
    for j in range(i):            # 22
        print(i, end=" ")         # 333
    print()


n=int(input())                    #print increasing numbers in a row
for i in range(1,n+1):            # 1
   for j in range(1,i +1):        # 1 2
      print(j,end=" ")            # 1 2 3 
print()                           # 1 2 3 4 


n=int(input())    
for i in range(1,n+1):
   for j in range(n-1):
      print(" ",end=" ")
   for j in range(i):
      print("*",end=" ") 
print()


n=int(input())                    #print a pyramid
for i in range(1,n+1):
   print(" "*(n-i) + "*"*(2*i-1))


n = int(input())                  #print a diamond
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)


n = int(input())                #print numbers in a triangle
num = 1                         #1
for i in range(1, n + 1):       #2 3
    for j in range(i):          #4 5 6
        print(num, end=" ")     #7 8 9 10
        num += 1
    print()

