def has_duplicates_v1(arr):
    '''cach1: so sanh tung cap'''
    n=len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]==arr[j]:
                return True
    return False

def has_duplicates_v2(arr):
    '''cach 2:dung set'''
    seen=set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False
import time 
arr = list(range(10000))
arr.append(5000)

start = time.time()
result1 = has_duplicates_v1(arr)
time1 =time.time()-start
print(f"cach 1: {time1:.4f} giay ")

strar = time.time()
result2 = has_duplicates_v2(arr)
time2 =time.time()-strar
print(f"cach 2: {time2:.4f} giay ")