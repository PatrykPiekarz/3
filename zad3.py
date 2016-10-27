#znajdz liczby pierwsze za pomoca sita erystotenesa

class sito:

    boles=[]
    n=0

    def __init__(self,n):
        i=2
        while i <= self.n:
            self.boles.append(1)
            return

    def sito(self):

        m=self.n**0.5
        i=2
        while i < m:
            if self.boles[i-2] == 1:
                j=i**2
                while j < self.n:
                    self.boles[j]=0
                    j+=i
            i+=1



        return