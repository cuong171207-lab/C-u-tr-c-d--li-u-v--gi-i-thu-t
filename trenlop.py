# def has_duplicates_v1(arr):
#     '''cach1: so sanh tung cap'''
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i]==arr[j]:
#                 return True
#     return False

# def has_duplicates_v2(arr):
#     '''cach 2:dung set'''
#     seen=set()
#     for item in arr:
#         if item in seen:
#             return True
#         seen.add(item)
#     return False
# import time
# arr = list(range(10000))
# arr.append(5000)

# start = time.time()
# result1 = has_duplicates_v1(arr)
# time1 =time.time()-start
# print(f"cach 1: {time1:.4f} giay ")

# strar = time.time()
# result2 = has_duplicates_v2(arr)
# time2 =time.time()-strar
# print(f"cach 2: {time2:.4f} giay ")


# def two_sum_v1(arr, target):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == target:
#                 return (i, j)
#     return None


# def two_sum_v2(arr, target):
#     seen = {}
#     for i in range(len(arr)):
#         complement = target - arr[i]
#         if complement in seen:
#             return (seen[complement], i)
#         seen[arr[i]] = i
#     return None


# import time

# arr = list(range(10000))
# arr.append(5000)
# target = 15000  # Cần định nghĩa target để truyền vào hàm

# start = time.perf_counter()
# result1 = two_sum_v1(arr, target)  # Thêm tham số target
# time1 = time.perf_counter() - start
# print(f"cach 1: {time1:.4f} giay ")

# start = time.perf_counter()  # Sửa lỗi chính tả strar
# result2 = two_sum_v2(arr, target)  # Thêm tham số target
# time2 = time.perf_counter() - start
# print(f"cach 2: {time2:.4f} giay ")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# def sum_to_n(n):
#     if n == 1:
#         return 1
#     return n + sum_to_n(n - 1)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(3))

# def infinite_recursion():
#     return infinite_recursion()

# infinite_recursion()

# def binary_seach_iterative(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# def binary_seach_recursive(arr, target, left, right):
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_seach_recursive(arr, target, mid + 1, right)
#     else:
#         return binary_seach_recursive(arr, target, left, mid - 1)
# Sắp xếp 
# def meger_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#     left_half = meger_sort(left_half)
#     right_half = meger_sort(right_half)
#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# arr=[15,34,21,11,42,53,98]
# print(meger_sort(arr))

# def quick_sort_inplace(arr, low, high):
#     if low<high:
#         pi=partition(arr, low, high)
#         quick_sort_inplace(arr, low, pi-1)
#         quick_sort_inplace(arr, pi+1, high)

# def partition(arr, low, high):
#     pivot=arr[high]
#     i=low-1
#     for j in range(low, high):
#         if arr[j]<=pivot:
#             i+=1
#             arr[i], arr[j]=arr[j], arr[i]
#     arr[i+1], arr[high]=arr[high], arr[i+1]
#     return i+1
# arr=[15,34,21,11,42,53,98]
# quick_sort_inplace(arr, 0, len(arr)-1)
# print(arr)

def permutation(nums):
    result = []
    def backtrack(path, remaining):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in remaining:
            path.append(num)
            remaining.remove(num)
            backtrack(path, remaining)
            path.pop()
            remaining.append(num)
    backtrack([], nums)
    return result

print(permutation([1,2,3]))

def is_safe(board, row, col, n):
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
            return False
        return
def solve_n_queens(n):
    result = []
    board = []
    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board.append(col)
                backtrack(row + 1)
                board.pop()
# backtrack(0)
# return result