from sys import stdin, stdout
k, r = map( int, stdin.readline().rstrip().split() )

x = 1
while 1:
    if((x == 10) or (((k*x)-r)%10 == 0) or ((k*x)%10 == 0)):
        break
    else:
        x += 1
print(x)