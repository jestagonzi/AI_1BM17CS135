w=0
p=2#player
x=1#comp
r=0

a=[[0,0,0],[0,0,0],[0,0,0]]

def grid():
    print('\n\n\n')
    print("\t  1\t  2\t  3")
    print("\t"+"________"*3)
    for i in range(3):
        print(chr(65+i)+"\t|",end='')
        for j in range(3):
            if(a[i][j]==0):
                print("\t",end='')
            elif(a[i][j]==1):
                print('X\t',end='')
            elif(a[i][j]==2):
                print('O\t',end='')
            print("|",end='')
        print()
        print("\t"+"________"*3)
        
def check():
    global w
    for i in range(3):
        if a[i]==[1,1,1]:
            w=1
        elif a[i]==[2,2,2]:
            w=2
    for i in range(3):
        if(a[0][i]==a[1][i]==a[2][i]==1):
            w=1
        elif(a[0][i]==a[1][i]==a[2][i]==2):
            w=2
    if(a[0][0]==a[1][1]==a[2][2]==1 or a[2][0]==a[1][1]==a[0][2]==1):
        w=1
    elif(a[0][0]==a[1][1]==a[2][2]==2 or a[2][0]==a[1][1]==a[0][2]==2):
        w=2


def play():
    global p
    while 1:
        s=input("\nPlayer "+str(p)+":\nEnter postion: ")
        i=ord(s[0])-65
        j=int(s[1])-1
        
        if(i in range(3) and j in range(3)):
            if(a[i][j]==0):
                a[i][j]=p
                if(p==1):
                    p=2
                else:
                    p=1
                break
        

def blockWin(p,x):
    for i in range(3):
        if a[i][0]==a[i][1]==p:
            if a[i][2]==0:
                a[i][2]=x
                return 1
        if a[i][0]==a[i][2]==p:
            if a[i][1]==0:
                a[i][1]=x
                return 1
        if a[i][1]==a[i][2]==p:
            if a[i][0]==0:
                a[i][0]=x
                return 1

    for i in range(3):
        if a[0][i]==a[1][i]==p:
            if a[2][i]==0:
                a[2][i]=x
                return 1
        if a[0][i]==a[2][i]==p:
            if a[1][i]==0:
                a[1][i]=x
                return 1
        if a[1][i]==a[2][i]==p:
            if a[0][i]==0:
                a[0][i]=x
                return 1

    if a[0][0]==a[1][1]==p:
        if a[2][2]==0:
            a[2][2]=x
            return 1
    if a[0][0]==a[2][2]==p:
        if a[1][1]==0:
            a[1][1]=x
            return 1
    if a[1][1]==a[2][2]==p:
        if a[0][0]==0:
            a[0][0]=x
            return 1
    elif a[2][0]==a[1][1]==p:
        if a[0][2]==0:
            a[0][2]=x
            return 1
    if a[2][0]==a[0][2]==p:
        if a[1][1]==0:
            a[1][1]=x
            return 1
    if a[1][1]==a[0][2]==p:
        if a[2][0]==0:
            a[2][0]=x
            return 1

    return 0
    



def aiFirst(n):
    global r
    if n==1:
        a[0][0]=1
    elif n==2:
        if a[2][2]==0:
            a[2][2]=1
            r=1
        else:
            a[0][2]=1
            r=2
    if n>2:
        if blockWin(1,1):
            return
        if blockWin(2,1):
            return
    if n==3:
        if r==2:
            a[2][0]=1
            
            
def playAI():
    global p
    while 1:
        s=input("\nPlayer "+str(p)+":\nEnter postion: ")
        i=ord(s[0])-65
        j=int(s[1])-1
        
        if(i in range(3) and j in range(3)):
            if(a[i][j]==0):
                a[i][j]=p
                #if(p==1):
                    #p=2
                #else:
                    #p=1
                break
        
        


grid()
n=1
c=0
t=0
while w==0 and c<9:
    if t==0:
        aiFirst(n)
        grid()
        n+=1
    elif t==1:
        playAI()
        grid()
    c+=1
    check()
    t=(t+1)%2

    
if c<9:
    print("Player %s Wins"%w)
else:
    print("Draw")
