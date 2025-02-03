user=[int(i) for i in input().split()]
height=[int(i) for i in input().split()]
c=0
for i in height:
    if user[1]<i:
        c+=1
print(c*2+(user[0]-c)*1)
