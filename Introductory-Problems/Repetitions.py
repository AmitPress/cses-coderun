# I, here, have tried to implement this with a stack
# the idea is to push consequtive chars in a stack a keep count of it

sq = [i for i in input().split()][0] # ACCCGTC
s = []
maxx = 1
current_letter = sq[0]
for i in range(0, len(sq)):
    if sq[i] == current_letter:
        s.append(sq[i])
        maxx = max(maxx, len(s))
    else:
        current_letter = sq[i]
        s.clear()
        s.append(sq[i])
        maxx = max(maxx, len(s))
    

print(maxx) # wrong ans
    