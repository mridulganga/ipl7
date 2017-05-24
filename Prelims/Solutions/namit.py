str_main = ""

def revstr(s):
    return s[::-1]
def getword(s,n):
    st = s.split(" ")
    st = filter(None, st) # fastest
    return st[n]
def wordcount(s):
    st = s.split(" ")
    st = filter(None, st) # fastest
    return len(st)
def shrink(w):
    st = list(w)
    i =0
    st2=[]
    for x in st:
        if i%2==0:
            st2.append(x)
        i+=1
    return "".join(st2)

def doStuff(s1,s2):
    str1 = s1
    str2 = s2.split(" ")
    global str_main
    for x in str2:
        if x=='count':
            str_main += str(wordcount(str1)) + " "
        if x[:3]=='len':
            str_main += str(len(getword(str1,int(x[4:])))) + " "
        if x[:3]=='rev':
            str_main += revstr(getword(str1,int(x[4:]))) + " "
        if x[:3]=='shr':
            str_main += shrink(getword(str1,int(x[4:]))) + " "


n = int(raw_input())    #test cases
for x in xrange(n):
    doStuff(raw_input(),raw_input())
    str_main +="\n"
print str_main.strip()
