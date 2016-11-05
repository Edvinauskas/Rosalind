f = open('INI5_IN.txt', 'r')
f_out = open('INI5_OUT.txt', 'w')
for index, i in enumerate(f, start=1):
    if index % 2 == 0:
        f_out.write(i)