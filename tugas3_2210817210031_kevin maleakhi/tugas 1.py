x = int(input(""))
y = int(input(""))

z = int(input("")) 
if x<y and y<z: print("{} {} {}".format(x,y,z))
elif y<z and z<x: print("{} {} {}".format(y,z,x))
elif z<x and x<y: print("{} {} {}".format(z,x,y))
elif x<z and z<y: print("{} {} {}".format(x,z,y))
elif y<x and x<z: print("{} {} {}".format(y,x,z))
elif z<y and y<x: print("{} {} {}".format(z,y,x))
