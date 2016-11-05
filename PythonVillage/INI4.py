odd_sum = 0
for i in range(4385,8988 + 1,):
    if (i % 2) == 1:
        odd_sum += i
print(odd_sum)