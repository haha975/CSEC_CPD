personnum=int(input("please enter number of person"))
heightoffen=int(input("please enter fence height"))
x=0
for i in range(personnum):
    i=int(input("inter each value"))
    if i>heightoffen:
       i=2
    else:
        i=1
    x=x+i
print(x)
    
