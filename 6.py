s1=9
for i in range(1, s1+1):
    print(*range(i, i*s1+1, i), sep='\t')