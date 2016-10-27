A=set([1,2,3])
print A
A.discard(3)
A.add(8)
print A
B= frozenset([3,5,6])
slownik = {B:9}
print slownik
C=set([5,4,9])
C.add(B)
print C
D=set()
print D
print len(A),len(B),len(C),len(D)
print 5 in A, 5 in B,5 in C,5 in D
print 8 not in A, 8 not in B, 8 not in C, 8 not in D
print set([1,2]) <=A
print set([3,4]) <=B
print set([5]) <=B
print set([1,3,5]) <=A
print A.issubset(B)
print A>=set([1,2])
print B>=set([3,4])
print A.issubset(B)
print '\n'
E=A|B
print E
print '\n'
F=A&B
print F
print '\n'
G=A^B
print G
print '\n'