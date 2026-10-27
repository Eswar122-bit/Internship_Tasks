# Problem: Set .symmetric_difference() Operation
# Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input()) 
arr = set(map(int,input().split())) 
b = int(input()) 
arr2 = set(map(int,input().split()))

result = arr.symmetric_difference(arr2) 
print(len(result))