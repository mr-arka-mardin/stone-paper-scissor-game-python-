import random
print("1-stone,2=paper,3=scissor")
z=0#computer point
k=0#your point
i=0
while (i<8):
    i=i+1
    x = int(input("enter your character"))
    y = random.randint(1, 3)


    if x==1 and y==2:
        z=z+1
        print("you lost as computer chose paper.chances left:",8-i)


    elif x==2 and y==1:
        print("you won as computer chose stone.chances left:",8-i)
        k=k+1

    elif x==1 and y==3:
        print("you won as computer chose scissor.chances left:",8-i)
        k=k+1

    elif x==2 and y==3:
        print("you lost as computer chose scissor.chances left:",8-i)
        z=z+1

    elif x==3 and y==2:
        print("you won as computer chose paper.chances left:",8-i)
        k=k+1

    elif x==3 and y==1:
        print("you lost as computer chose stone.chances left:",8-i)
        z=z+1

    elif x==y:
        print("game-draw.chances left:",8-i)



else:
    print("game over!")
print("computer point is :",z,"and your point is:",k)
if (k>z):
    print("you won.as computer point is less than yours by",k-z,"points")
elif (z>k):
    print("you lost. computers point is more than yours point by",z-k,"points")
else:
    print("match draw as you both scored",k,"points")






