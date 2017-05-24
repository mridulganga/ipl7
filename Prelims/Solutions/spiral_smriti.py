def spiral(n):
    a = [['0' for i in range(n)] for j in range(n)]

    k = 1
    l = 65
    check=0

    c1=0
    c2=n-1
    r1=0
    r2=n-1

    while (k+l-65<=n*n):
        for i in xrange(c1,c2+1):
            if check==0:
                a[r1][i] = str(k)
                k+=1
                check = 1
            else:
                a[r1][i] = chr(l)
                l+=1
                check = 0
        for j in xrange(r1+1,r2+1):
            if check==0:
                a[j][c2] = str(k)
                k+=1
                check = 1
            else:
                a[j][r2] = chr(l)
                l+=1
                check = 0
        for i in xrange(c2-1,c1-1,-1):
            if check==0:
                a[r2][i] = str(k)
                k+=1
                check = 1
            else:
                a[r2][i] = chr(l)
                l+=1
                check = 0
        for j in xrange(r2-1,r1,-1):
            if check==0:
                a[j][c1] = str(k)
                k+=1
                check = 1
            else:
                a[j][r1] = chr(l)
                l+=1
                check = 0
        c1+=1
        c2-=1
        r1+=1
        r2-=1

    for x in a:
        for p in x:
            print p,
        print ""

num = int(raw_input())
list_side = (raw_input())
for x in list_side.split(): 
    spiral(int(x))
    print ""

