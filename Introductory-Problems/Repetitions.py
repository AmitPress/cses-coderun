sq = [i for i in input().split()] # ACCCGTC
s = set([sq[0]])
max_val = 1
cnt = 0
for i in range(1, len(sq)):
    if len(s) == 1:
        cnt += 1
        max_val = max(max_val, cnt)
        s.add(sq[i])
    else:
        s.pop(0)
        cnt = 0
print(max_val) # wrong ans
    