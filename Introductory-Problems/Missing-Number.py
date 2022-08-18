n = int(input())
arr = list(map(int, input().split()))


# run time error
#
# for i in range(n-1):
#     if i+1 not in arr:
#         print(i+1)
#         break

all_sum = sum(arr)
# print(all_sum)
ideal_sum = n * (n + 1) // 2
# print(ideal_sum)
ans = ideal_sum - all_sum
print(ans)