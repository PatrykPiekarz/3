#napisz skrypt ktory wylicza najmniejszy wspolny dzielnik i najmniejsza wspolna wielokrotnosc
a=raw_input("podaj liczbe a\n")
a=int(a)
b=raw_input("podaj liczbe b\n")
b=int(a)
n=a
m=b

while n!=m:
    if n > m:
        n-=m
    else:
        m-=n

print 'Najmniejszy wspolny dzielnik to'
print n
print 'A najwieksza wspolna wielokrotnosc to'
print (a*b)/n