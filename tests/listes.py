import random
class Draw():
    def __init__(self,xLen,yLen,p):
        self.xLen = xLen
        self.yLen = yLen
        self.draw = []
        self.new(p)


    def applyDraw(self, preset):
        self.draw[0] = preset
        self.i = 0

    def __refresh(self,x,y,i):
        S = 0
        for nearx in range(0,3):
            for neary in range(0,3):
                if not nearx == neary == 1:
                    try:
                        S += self.draw[i][x-1+nearx][y-1+neary]
                    except:
                        pass #si par exemple on est proche d'un bord, on évite le plantage lors de la lecture dans un index bidon
        if self.draw[i][x][y]:
            if S == 2:
                return 1
        elif S == 3:
            return 1
        elif S <2:
            return 0
        elif S >3:
            return 0
        else:
            return 0

    def new(self,p):
        self.draw.append([ [self.randbool(p) for y in range(self.yLen)] for x in range(self.xLen)])
        #self.draw1 = [ [0 for y in range(self.yLen)] for x in range(self.xLen)]
        for n in range(0,self.xLen):
            print(self.draw[0][n])
        print("")
        self.i = 0

    def increment(self, increment):
        for i in range(self.i, self.i+ increment):
            self.draw.append([ [self.__refresh(x,y,self.i-1) for y in range(self.yLen)] for x in range(self.xLen)])
            if __name__ == '__main__':
                for n in range(0,self.xLen):
                    print(self.draw[i][n])
                print("")
    def getCurrentDraw(self):
        return self.draw[len(self.draw)-1]

    def randbool(self,p):
        '''renseigner un p compris entre 0 et 1
        '''
        r = random.randint(0,int(1/p))
        if r == 0:
            return 1
        else :
            return 0

if __name__ == '__main__':
    a = int(input('xLen : '))
    b = a
    c = float(input('p : '))
    MyDraw = Draw(a,b,c)
    MyDraw.increment(10)
