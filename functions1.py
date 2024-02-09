#ex1
grams = float(input())
def my_function(grams):
    return 28.3495231 * grams
ounces = my_function(grams)
print(ounces)
#ex2
F = float(input())
def my_func_fahr(F):
    return (5/9) * (F - 32)
C = my_func_fahr(F)
print(C)
#ex3
numheads = 35
numlegs = 94
def solve(numheads, numlegs):
    rab = int((numlegs - numheads * 2)/2)
    chick = int(numheads - rab)
    print("rabbits = ", rab)
    print("chikens = ", chick)
solve(numheads, numlegs)
#ex4
num_list=list(map(int, (input().split())))
def filter_prime(x):
    for x in num_list:
        if x==2:
            print(2)
        else:
            k=0
            for i in range(2, int(x/2)+1):
                if x%i==0:
                    k+=1
            if k==0 and x>2:
                print(x)
filter_prime(num_list)
#ex5
from itertools import permutations
string1 = input()
thislist = []
def permut(thislist):
    for x in string1:
        thislist.append(x)
    perm = permutations(thislist)
    for i in list(perm): 
        print (*i, sep='') 
permut(thislist)
#ex6
string1 = input()
def rev_str(string1):
    x = string1.split()
    x.reverse()
    for i in x:
        print(i)
rev_str(string1)
#ex7
nums=list(map(int, (input().split())))
def has_3_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_3_3(nums))
#ex8
def spy_game(nums):
    i=0
    a=0
    while i < len(nums)-1:
        if (nums[i]==0 and nums[i+1]==0 and nums[i+2]==7):
            a+=1
        i+=1
    if a>0:
        print ("Yes")
        return
    else:
        print ("No")
        return
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 
#ex9
def volume():
    rad=float(input("the radius: "))
    v=4*3.14*rad*rad*rad
    print("volume: ", v)
    return
volume()
#ex10
def unique():
    num_list=list(map(int, (input().split())))
    new_list=[]
    for x in num_list:
        if x in new_list:
            continue
        else:
            new_list.append(x)
    for x in new_list:
        print(x)
unique()
#ex11
def palindrome(s):
    k=0
    for x in range(0, len(s)):
        if s[x]!=s[len(s)-x-1]:
            print ("No")
            return
    print ("Yes")
    return
word=str(input())
palindrome(word)
#ex12
num_list=list(map(int, (input().split())))
def histogram(nums):
    for x in nums:
        print ('*'*x)
histogram(num_list)
#ex13
import random
n=random.randrange(1, 20)
new=[]
print("Hello! What is your name?")
name=str(input())
print("Well, ", name, "I am thinking of a number between 1 and 20.\nTake a guess.")
a=int(input())
new.append(a)
def guess(n, a, new):
    if n==a:
        print ("Good job, ", name, "! You guessed my number in ", len(new) , "guesses!")
        return
    if a>n:
        print ("Your guess is too much\nTake a guess.")
        a=int(input())
        new.append(a)
        return guess(n, a, new)
    if a<n:
        print ("Your guess is too low\nTake a guess.")
        a=int(input())
        new.append(a)
        return guess(n, a, new)
guess(n, a, new)
#ex14
from nine import volume

from ten import unique

from thirteen import guess