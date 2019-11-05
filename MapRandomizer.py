import random as r
#width=600
#height=600
map=[]
msize=20
cx = msize / 2
cy = msize / 2

objects=[]

def isIsolated(x,y):
    s = True
    for d in range(4):
        x1 = x + getXinDir(d)
        y1 = y + getYinDir(d)
        if (x1 >= 0 and y1 >= 0 and y1 < msize and x1 < msize):
            if (map[x1][y1] == 1):
                s = False
    return s

class Object():
    x=0
    y=0
    w=0
    h=0
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def incH(self):
        self.h=self.h+1
    def incW(self):
        self.w=self.w+1
    def getString(self):
        return "("+str(self.x)+", "+str(self.y)+") w: "+str(self.w)+" | h: "+str(self.h)

def createObjects():
    global objects
    rows=[]
    map1=[]
    for x in range(msize):
        col = []
        for y in range(msize):
            col.append(1 if map[x][y]==1 else 0)
        map1.append(col)

    for x in range(msize):
        co=None
        for y in range(msize):
            if(map1[x][y]==1):
                if(co!=None):
                    co.h=co.h+1
                    map1[x][y]=0
                else:
                    co=Object(x,y,1,1)
                    map1[x][y]=0
            else:
                if (co != None):
                    if (co.w == 1 and co.h == 1):# and not isIsolated(co.x, co.y)):
                        map1[co.x][co.y]=1
                        co = None
                    else:
                        rows.append(co)
                        co = None
        if (co != None and not(co.w==1 and co.h==1)):
            rows.append(co)
            #co = None

    for y in range(msize):
        co=None
        for x in range(msize):
            if(map1[x][y]==1):
                if(co!=None):
                    co.w=co.w+1
                else:
                    co=Object(x,y,1,1)
            else:
                if(co!=None):
                    #if(co.w==1 and co.h==1 and not isIsolated(co.x,co.y)):
                    #    co=None
                    #else:
                    rows.append(co)
                    co=None
        if(co!=None):
            rows.append(co)
            #co = None
    for row in rows:
        print(row.getString())
    objects=rows

def create(size):
    globals()
    global msize
    msize=size
    for x in range(msize):
        col = []
        for y in range(msize):
            # fill=False
            # if(x==0 or x==39 or y==0 or y==39):fill=True
            fill = True
            # if(x%4==0):fill=True
            col.append((1 if fill else 0))
        map.append(col)

    cr = int(msize / 10.0)
    for xi in range(2 * cr):
        for yi in range(2 * cr):
            map[int(cx - cr + xi)][int(cy - cr + yi)] = 0
    orient = r.randrange(0, 4)

    maxd = msize / 2
    for i in range(50):
        move(orient, r.randrange(1, maxd))
        orient = orient + r.randrange(-1, 2)
        if (orient < 0): orient = 3
        if (orient > 3): orient = 0

    removeSurrounding()
    #createObjects()
    return map

def getXinDir(d):
    if(d%2==0):return 0
    return 1 if d==1 else -1
def getYinDir(d):
    if(d%2==1):return 0
    return 1 if d==2 else -1

def move(dir,dist):
    global cx,cy,msize
    for d in range(dist):
        if(dir%2==0):cy=cy-1 if dir==0 else cy+1
        else:cx=cx-1 if dir==3 else cx+1
        if(cx<1 or cx>=msize-2):cx=1 if cx<1 else msize-2
        if(cy<1 or cy>=msize-2):cy=1 if cy<1 else msize-2
        #print(str(cx)+", "+str(cy))
        map[int(cx)][int(cy)]=0

def removeSurrounding():
    global cx,cy,map
    map1=[]
    for x in range(msize):
        col = []
        for y in range(msize):
            col.append(1 if map[x][y]==1 else 0)
        map1.append(col)
    x=0
    for col in map:
        y=0
        for row in col:
            #print(row,map[x][y])
            if(row==1):
                s=True
                for d in range(4):
                    x1=x+getXinDir(d)
                    y1=y+getYinDir(d)
                    if(x1>=0 and y1>=0 and y1<msize and x1<msize):
                        if(map[x1][y1]==0):
                            s=False
                if(s):
                    #print(x,y)
                    map1[x][y]=0
                    #print(map[x][y], map1[x][y])
            y=y+1
        x=x+1
    map=map1

