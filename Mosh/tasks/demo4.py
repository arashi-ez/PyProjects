secret_num = '4'
i = 1
while i <= 3:
    guess = input("Guess: ")
    if guess == secret_num:
        print('Congrats')
        break
    i+=1
else:
    print('Sorry you failed!')