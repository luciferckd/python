list=[20,45,34,76,89,345,5,678,9,4]  # list inside the data using the sort the value..
list.sort() # its use the command the sort
print(list)

english=int(input("enter the eng marks:"))
maths=int(input("enter the math marks:"))
science=int(input("enter the science marks:"))
total=english+maths+science     # there three subjects marks total using the assign operator
print(total)
if total>230:
  print("maximum")    # this is order of maximum value
else:
  print("poor")


english=int(input("enter the eng marks:"))
maths=int(input("enter the math marks:"))
science=int(input("enter the science marks:"))
total=english+maths+science
if total>=270:
  print("topper")
elif total>=198:
  print("good")
else:
  print('average')




a=int(input("enter the a value\n"))
b=float(input("enter the b value\n"))
c=int(input("enter the c value\n"))
if (a>b) and (a>c):
  print(a,"is a bigger" )
elif (b>a) and (b>c):
  print(b,"is a bigger")
else:
  print(c,"is a bigger")

c=int(input("Enter the c value:"))
d=int(input("Enter the d value:"))
y=int(input("Enter the y value:"))
x=c+d*y
print(x)



from ast import Div
x=(2,4,6,8,10)
n=(5)
div = x*n
print(div)


num=int(input("enter the number:"))
if(num>0):
  print(num,"is a positive")
elif (num<0):
  print(num,"is a negative")
else:
  print("the given num is zero")



vowels=["a","e","i","o","u"]
ch=input("please enter the small character in small case:")
if ch in vowels:
  print(ch,"is a vowels")
#elif ch and vowels:
  #print("enter the small case")
else:
  print("enter the correct vowels")



x=input()
id(x)
y=input()
id(y)
if x in y:
  print("is a true")
else:
  print("is a false")



# student marks total calucated the len.. using tuple datatype
marks=(77,89,78,56,90,77)
cs_marks=(99,67,87,56,89,88)
total=marks+cs_marks  #...(+) is a concatedinaton.. but this allow
len(total)



set_1={1,3,4,5,6,7}
set_2={8,9,0,1,2,3}
print(len(set_1.union(set_2)))


# for-loops statement
a=[5656]
b=[8,9,6,5,4,43,3]
for i in a:
  print(i)
print("hi")


a=[6,7,8,5,3,3]
i=0
while i < len(a):
  val_i=a[i]
if val_i % 2==0:
  print("even")
else:
  print("odd")
i+=1


def exp (a,b,c,d,e):
  s=(2*a)+(3*b)-2*c*((4*d)-e)
  print(s)
exp(3,4,5,6,8)


from __future__ import print_function
def aoc(r,pi=3.14):
  result=pi*r**2
  print(result)
aoc(6)


dict_1={1:"vinoth",2:"raju", 3:"sathish", 4:"malliga"}
dict_1.update({6:"football", 7:"reading", 8:"cooking", 9:"housewife"})
for i,j in dict_1.items():
  print(i,j)


b={1:'a', 2:'b', 3:'c', 4:'d'}
for i,j in b.items():   #is using for dictonary in built the key & values
  print(i*4,j*6)


city=['madurai', 'chennai', 'theni']
for i in city:
  if i == "madurai":
   print(i)
else:
  print(i*1)


# lambda 

def func_build(x):
    return lambda num : num + x

add = func_build(10)
add_t = func_build(20)

print(add(7))
print(add_t(7))

numbers = [3, 4, 5, 6, 7, 8, 20]

square_nums = map(lambda num : num * num, numbers)
print(list(square_nums))

odd_nums = filter(lambda num : num % 2 !=0, numbers)
print(list(odd_nums))

from functools import reduce

numb = [1, 3, 5, 7, 8]
total = reduce(lambda acc, curr : acc + curr, numb)
print(total)
print(sum(numb))

names = ['suren', 'kannan', 'massu']

char_count = reduce(lambda acc, cuur : acc + len(cuur), names, 0)

print(char_count)

# three sum closet

def threesum_closet(nums, target):
    
    nums.sort()
    close = float('inf')

    for i in range(len(nums) - 2):
        if i < 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums) - 1
        
        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]
            
            if current_sum == target:
                return current_sum
                
            elif abs(current_sum - target) < abs(close - target):
                close = current_sum
                
            if current_sum < target:
                l += 1
            else:
                r -= 1
                
    return close
    
nums = [-1, 2, 1, -4]
target = 1
result = threesum_closest(nums, target)
print("Closest sum:", result)
        

