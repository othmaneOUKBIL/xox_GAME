def rep(r,x, y ):
    
    
    t=[]
    for i in range(y-1):
       t.append(r[i])
    t.append(x)
    for i in range(y,len(r)):
        t.append(r[i])
    return t
def win(e):
    if e[0]==e[4]==e[8]=="x" or e[2]==e[4]==e[6]=="x":
        return 1
    if e[0]==e[4]==e[8]=="o" or e[2]==e[4]==e[6]=="o":
        return 0
    if e[3]==e[4]==e[5]=="x" or e[6]==e[7]==e[8]=="x"or e[0]==e[2]==e[1]=="x":
        return 1
    if e[4]==e[5]==e[3]=="o" or e[7]==e[6]==e[8]=="o"or e[0]==e[1]==e[2]=="o":
        return 0
    if e[0]==e[3]==e[6]=="x" or e[1]==e[4]==e[7]=="x"or e[8]==e[5]==e[2]=="x":
        return 1
    if e[0]==e[3]==e[6]=="o" or e[1]==e[4]==e[7]=="o"or e[8]==e[5]==e[2]=="o":
        return 0
    
    
    
    
    

m=[1,3,5,7,9]
    
v=["1","2","3","4","5","6","7","8","9"]

print(v[0]," | ",v[1]," | ",v[2])
print("_________________")
print(v[3]," | ",v[4]," | ",v[5])
print("_________________")
print(v[6]," | ",v[7]," | ",v[8])
    
for i in range(1,10):
        if win(v)==1:
            print("joueur 1 gagne")
            break
        if win(v)==0:
            print("joueur 2 gagne")
            break
        if i in m:
            y=int(input("tour du joueur 1 : "))
            v=rep(v,"x",y)
        else : 
                y=int(input("tour du joueur 2 : "))
                v=rep(v,"o",y)
            
        print(v[0]," | ",v[1]," | ",v[2])
        print("_________________")
        print(v[3]," | ",v[4]," | ",v[5])
        print("_________________")
        print(v[6]," | ",v[7]," | ",v[8])
        if i ==9:
            print('egualité')
