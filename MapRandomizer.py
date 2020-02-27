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
        elif (co!=None):
            map1[co.x][co.y] = 1
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
    checkObjects()

    combineObs()
    #checkObjects()

def checkObjects():
    global objects;
    map2=[]
    for x in range(msize):
        col = []
        for y in range(msize):
            col.append(0)
        map2.append(col)
    onum=48
    for o in objects:
        for x1 in range(o.w):
            for y1 in range(o.h):
                #map2[o.x + x1][o.y + y1]=1 if map2[o.x + x1][o.y + y1]==0 else map2[o.x + x1][o.y + y1]+1
                map2[o.x + x1][o.y + y1]=onum
        onum = onum + 1
        if onum == 58:
            onum = 65
        elif onum == 91:
            onum = 97

    for col in map2:
        cs = ""
        for val in col:
            #cs = cs + ("X" if val == 1 else (" " if val==0 else "O")) + " "
            cs = cs + (chr(val) if val != 0 else " ") + " "

        print(cs)


def combineObs():
    global objects
    combine=[]
    for o in objects:
        ind=objects.index(o)
        for i1 in range(len(objects)):
            if(i1==ind):continue
            o2=objects[i1]
            for d in range(4):
                if(o.x+getXinDir(d,o.w)==o2.x and o.y+getYinDir(d,o.h)==o2.y):
                    if(d%2==0):
                        if(o2.h==o.h):
                            combine.append([o,o2])
                    else:
                        if(o2.w==o.w):
                            combine.append([o,o2])
    #print("combine: ")
    '''for os in combine:
        for o in os:
            if(objects.__contains__(o)):
                objects.remove(o)
        print("c { "+os[0].getString()+", "+os[1].getString())'''

    added=[]
    obs1=[]
    for c in combine:
        if(added.__contains__(c[1]) or added.__contains__(c[0])):continue
        small=c[0] if (c[0].x<c[1].x or c[0].y<c[1].y) else c[1]
        lg=c[1] if small==c[0] else c[0]
        if(c[0].x!=c[1].x):
            small.w=small.w+lg.w
        else:
            small.h=small.h+lg.h
        obs1.append(small)
        added.append(c[0])
        added.append(c[1])
    for o in objects:
        if ((not obs1.__contains__(o)) and (not added.__contains__(o))):
            obs1.append(o)
    objects=obs1
    checkObjects()
    if(len(combine)>3):
        print("again")
        combineObs()




def fill(x,y,liq):
    globals()
    #print(x,y)
    liq[x][y]=1
    for d in range(4):
        x1=x+getXinDir(d)
        y1=y+getYinDir(d)
        if(x1<len(liq) and y1<len(liq) and x1>=0 and y1>=0 ):
            if(liq[x1][y1]==0 and map[x1][y1]==0):
                liq=fill(x1,y1,liq)
        else:
            return [[]]
    return liq

def fillRegions():
    globals()
    r=[3,msize-3]
    maxsize=msize*msize*(.25*.25)
    print("fillsize="+str(maxsize))
    for x in range(r[1]-r[0]):
        for y in range(r[1]-r[0]):
           # print(x, y, r[0],r[1])
            if(map[int(x+r[0])][int(y+r[0])]==0):
                tryFill(r[0]+x,r[0]+y,1,maxsize)

def tryFill(ox,oy,min,max):
    globals()
    liq=[]
    for x in range(msize):
        col=[]
        for y in range(msize):
            col.append(0)
        liq.append(col)
    liq=fill(ox,oy,liq)
    list=[]
    ix=0
    for x in liq:
        iy=0
        for y in x:
            if (y==1):
               list.append([ix,iy])
            iy=iy+1
        ix=ix+1
    l=len(list)
    if(l<max and l>=min):
        for p in list:
            map[int(p[0])][int(p[1])]=1
    print("fill size = "+str(len(list))+" for "+str(ox)+", "+str(oy))

def create(size):
    globals()
    global msize
    msize=size
    cx = msize / 2
    cy = msize / 2
    for x in range(msize):
        col = []
        for y in range(msize):
            # fill=False
            # if(x==0 or x==39 or y==0 or y==39):fill=True
            fill = True
            # if(x%4==0):fill=True
            col.append((1 if fill else 0))
        map.append(col)

    cr = 2
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
    fillRegions()
    if(map[int(cx)][int(cy)]!=0):
        create(size)#recalls
    #createObjects()
    return map


def getXinDir(d,r=1):
    if(d%2==0):return 0
    return r if d==1 else -r
def getYinDir(d,r=1):
    if(d%2==1):return 0
    return r if d==2 else -r

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

