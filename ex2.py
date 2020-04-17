print('GUESS THE NUMBER. you have 5 chances')
i = 0
while (i<5):
    i = i + 1
    f= int(input())
    if  f>18 :
      print('try again.your guessed number is larger than the actual one/n '' no. of chances left is', 5 - i)

    elif f<18:
        print('try again.your guess is smaller than the actual number' 'no. of chances left is',5-i)
    elif f == 18:
        print("you won")
        break

else:
    print("chances over")
