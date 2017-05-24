#valid only for even

sent = raw_input()
sent_list = list(sent)
n = len(sent)

k=1
pos=0

def valAt1(pos):
    return sent_list[n-pos]
def valAt2(pos):
    return sent_list[pos]

print " "*(n/4) + sent_list[0]

for i in xrange(1,n/4+1):
    space1 = " "*(n/4-i)
    space2 = " "*k
    k+=2 
    pos+=1
    print space1 + valAt1(pos) + space2 + valAt2(pos)

k-=4
for i in xrange(n/4-1,0,-1):
    space1 = " "*(n/4-i)
    space2 = " "*k
    k-=2
    pos+=1
    print space1 + valAt1(pos) + space2 + valAt2(pos)

print " "*(n/4) + sent_list[n/2]
