import MapRandomizer as mr
print("OK")

def getBox(x,y, n):
    print("BOX : ")
    print("P1 : ")
    print(getP4(x,y,n))
    print("P2 : ")
    print(getP2(x,y,n))

def getP41(x,y,n,s):
    s="<model name='unit_box_"+str(n)+"'>\n        <pose>"+str(x)+" "+str(y)+" "+str(s/2)+" 0 -0 0</pose>\n    <link name='link'>\n          <pose>"+str(x)+" "+str(y)+" "+str(s/2)+" 0 -0 0</pose>\n          <velocity>0 0 0 0 -0 0</velocity>\n          <acceleration>0 -0 0 0 -0 0</acceleration>\n          <wrench>0 -0 0 0 -0 0</wrench>\n        </link>\n      </model>"
    return s
def getP21(x,y,n,s):
    s="<model name='unit_box_"+str(n)+"'>\n      <pose>"+str(x)+" "+str(y)+" "+str(s/2)+" 0 -0 0</pose>\n      <link name='link'>\n        <inertial>\n          <mass>10</mass>\n          <inertia>\n            <ixx>1</ixx>\n            <ixy>0</ixy>\n            <ixz>0</ixz>\n            <iyy>1</iyy>\n            <iyz>0</iyz>\n            <izz>1</izz>\n          </inertia>\n        </inertial>\n        <collision name='collision'>\n          <geometry>\n            <box>\n              <size>"+str(s)+" "+str(s)+" "+str(s)+"</size>\n            </box>\n          </geometry>\n          <max_contacts>10</max_contacts>\n          <surface>\n            <bounce/>\n            <friction>\n              <ode/>\n            </friction>\n            <contact>\n              <ode/>\n            </contact>\n          </surface>\n        </collision>\n        <visual name='visual'>\n          <geometry>\n            <box>\n              <size>1 1 1</size>\n            </box>\n          </geometry>\n          <material>\n            <script>\n              <uri>file://media/materials/scripts/gazebo.material</uri>\n              <name>Gazebo/Grey</name>\n            </script>\n          </material>\n        </visual>\n        <velocity_decay>\n          <linear>0</linear>\n          <angular>0</angular>\n        </velocity_decay>\n        <self_collide>0</self_collide>\n        <kinematic>0</kinematic>\n        <gravity>1</gravity>\n      </link>\n      <static>0</static>\n    </model>"
    return s
def getP4(x,y,n,w,l,h):
    x=x+(w/2.0)
    y=y+(l/2.0)
    s="<model name='unit_box_"+str(n)+"'>\n        <pose>"+str(x)+" "+str(y)+" "+str(h)+" 0 -0 0</pose>\n    <link name='link'>\n          <pose>"+str(x)+" "+str(y)+" "+str(h/2)+" 0 -0 0</pose>\n          <velocity>0 0 0 0 -0 0</velocity>\n          <acceleration>0 -0 0 0 -0 0</acceleration>\n          <wrench>0 -0 0 0 -0 0</wrench>\n        </link>\n      </model>"
    return s
def getP2(x,y,n,w,l,h):
    x=x+(w/2.0)
    y=y+(l/2.0)
    #w=w-.1
    #l=l-.1
    #y=y+2
    s="<model name='unit_box_"+str(n)+"'>\n      <pose>"+str(x)+" "+str(y)+" "+str(h)+" 0 -0 0</pose>\n      <link name='link'>\n        <inertial>\n          <mass>100</mass>\n          <inertia>\n            <ixx>1</ixx>\n            <ixy>0</ixy>\n            <ixz>0</ixz>\n            <iyy>1</iyy>\n            <iyz>0</iyz>\n            <izz>1</izz>\n          </inertia>\n        </inertial>\n        <collision name='collision'>\n          <geometry>\n            <box>\n              <size>"+str(w)+" "+str(l)+" "+str(h)+"</size>\n            </box>\n          </geometry>\n          <max_contacts>10</max_contacts>\n          <surface>\n            <bounce/>\n            <friction>\n              <ode/>\n            </friction>\n            <contact>\n              <ode/>\n            </contact>\n          </surface>\n        </collision>\n        <visual name='visual'>\n          <geometry>\n            <box>\n              <size>"+str(w)+" "+str(l)+" "+str(h)+"</size>\n            </box>\n          </geometry>\n          <material>\n            <script>\n              <uri>file://media/materials/scripts/gazebo.material</uri>\n              <name>Gazebo/Grey</name>\n            </script>\n          </material>\n        </visual>\n        <velocity_decay>\n          <linear>0</linear>\n          <angular>0</angular>\n        </velocity_decay>\n        <self_collide>0</self_collide>\n        <kinematic>0</kinematic>\n        <gravity>0</gravity>\n      </link>\n      <static>0</static>\n    </model>"
    return s
#getBox(1,1,2)
#getBox(1,1,3)
size=20
xoff=-(size-1)/2
yoff=-(size-1)/2
bsize=2
map=mr.create(size)
boxes=[]
for col in map:
    cs=""
    for val in col:
        cs=cs+("X" if val==1 else " ")+" "
    print(cs)
mr.createObjects()
obj=mr.objects
#print(str(len(map))+", "+str(size))
for x in range(len(map)):
    for y in range(len(map[x])):
        #print(str(x)+", "+str(y))
        if(map[x][y]==1):
            boxes.append([(x+xoff)*bsize,(y+yoff)*bsize])


#boxes=[[2.2,2.1],[4.1,4.2],[2.2,0.1],[0.1,-2.2],[-2.1,-3.3]]
p2=""
p4=""

compress=True

if(not compress):
    for i in range(len(boxes)):
        p2=p2+getP21(boxes[i][0],boxes[i][1],i+1,bsize)
    for i in range(len(boxes)):
        p4=p4+getP41(boxes[i][0],boxes[i][1],i+1,bsize)
else:
    i1=0
    for o in obj:
        print(str(i1)+" - "+o.getString())
        p2=p2+getP2((o.x+xoff)*bsize,(o.y+yoff)*bsize,i1,o.w*bsize,o.h*bsize,bsize)
        p4=p4+getP4((o.x+xoff)*bsize,(o.y+yoff)*bsize,i1,o.w*bsize,o.h*bsize,bsize)
        i1=i1+1

p1=open("/home/racecar/PycharmProjects/Gazebo-Map-Gen/gen/p1.world","r")
p3=open("/home/racecar/PycharmProjects/Gazebo-Map-Gen/gen/p2.world","r")
p5=open("/home/racecar/PycharmProjects/Gazebo-Map-Gen/gen/p3.world","r")

s=p1.read()+p2+p3.read()+p4+p5.read()
#print(s)

nf=open("/home/racecar/racecar-ws/src/racecar-simulator/racecar_gazebo/worlds/racecar_gen.world","w")
nf.write(s)
nf.close()
#print(s)
#print(s.read())