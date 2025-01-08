n = input().split()
n = [int(item) for item in n]
m = int(input())
d = n[-m:]
print(" ".join(map(str,d)))

#آخرین عدد