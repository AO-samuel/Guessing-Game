guess = None
val = 5
lives = 3
print('Guessing Game')
print('You have 3 Lives')  

i = 0
if guess != val:
    while i < 3:
        guess = int(input('Enter guess: '))
        if guess == val:
            print('You win')
            break
        lives -= 1
        print('Lives remaining: ', lives)
        i += 1
    else:
        print('You lose')
