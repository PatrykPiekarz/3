#znajdz liczby pierwsze za pomoca sita erystotenesa

class sito:

    boles=[]
    n=0

    def __init__(self,n):
        self.n=n
        i=1
        while i != self.n+1:
            self.boles.append(i)
            i+=1
        return

    def sito(self):
        m=self.n**0.5
        boles=self.boles
        i=1
        while i < m:
            for j in boles:
                if (not (j % i) and not (i == j)) and i != 1:
                    boles.remove(j)
            j = boles.index(i) + 1
            i = boles[j]
        return

n = int(raw_input("podaj gorny zakres"))
x = sito(n)
x.sito()
for i in x.boles:
    print i
i=0

