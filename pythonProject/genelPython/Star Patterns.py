#1
for i in range(5):
    for i in range(5):
        print("*", end="")
    print()#satırı atla demek

"""" 
*****
*****
*****
*****
*****    """
print("--------------------------")
#2
k=1
for i in range(5):
    print("*"*k, end="")
    k += 1
    print()

for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()
""" 
*
**
***
****
*****  """

print("--------------------------")
#3
k=5
for i in range(5):
    print("*"*k, end= "")
    k -= 1
    print()

for i in range(1,5):
    for j in range(5-i):
        print("*", end="")
    print()
"""      
*****
****
***
**
*

"""
print("--------------------------")
#4

k=0
p=5
for i in range(0,6):
    print(" "*p, end="")
    p -= 1
    print("*"*k)
    k += 1

n = 7
for i in range(1, n+1):
    for j in range(2*n - 2*i):
        print(end=" ")
    for j in range(0,i):
        print(end="* ")
    print()

n = 5
for i in range(i, n+1):
    print((2*n - 2*i)* " " + i*"* ")
"""     
    *
   **
  ***
 ****
*****
            * 
          * * 
        * * * 
      * * * * 
    * * * * * 
  * * * * * * 
* * * * * * * 
"""


#5

i = 0
for i in range(1,6):
    print(" "*(2*i-2), end="")
    print("* "* (6-i))
    i += 1
n=5
for i in range(1, n+1):
    for j in range((2*i)-2):
        print(end=" ")
    for j in range(0,n+1-i):
        print(end="* ")
    print()

"""  
* * * * * 
  * * * * 
    * * * 
      * * 
        *   """
#6
n = 5
for i in range(0,n):
    for j in range(0,i+1):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print(end="* ")
    print()

n = 5
for i in range(1, 2*n):
    if i <= n:
        print(i*"* ")
    else:
        print((2*n-i)*"* ")

""" 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
    """
#7
n = int(input("lütfen bir sayı giriniz"))
for i in range(1,n):
    print(" "*n, end=" ")
    n -= 1
    print("* "*i)
n = 5
k = n+2
for i in range(n):
     for j in range(k):
         print(end=" ")
     k -= 1
     for j in range(i+1):
         print(end="* ")
     print()

"""     * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 

Process finished with exit code 0
                      """
#8

n = 6
k = n+2

for i in range(1,n+1):
    for j in range(k):
        print(end=" ")
    k -= 1
    for j in range(i):
        print(end="* ")
    print()
for i in range(n-1,0,-1):
    for j in range(k+2):
        print(end=" ")
    k += 1
    for j in range(i):
        print(end="* ")
    print()
    """     
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        *                """

#9
n = 5
char = 65
for i in range(n):
    ch = chr(char)
    char += 1
    for j in range(0,i+1):
        print(ch, end=" ")
    print()


"""   
A 
B B 
C C C 
D D D D 
E E E E E
             """
#10
n = 6
k = n + 2
for i in range(n):
    print(end=" "*k)
    k -= 1
    x = 65
    for j in range(0,i+1):
        ch = chr(x)
        print(ch, end=" ")
        x += 1
    print()
for i in range(n, 1,-1):
    print(end=" "*(k+2))
    k += 1
    x = 65
    for j in range(0,i-1):
        ch = chr(x)
        print(ch, end=" ")
        x += 1
    print()
"""           
        A 
       A B 
      A B C 
     A B C D 
    A B C D E 
   A B C D E F 
    A B C D E 
     A B C D 
      A B C 
       A B 
        A       """






