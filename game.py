from random import randint
from models.calcular import Calculator

score = 0

#play
def play():
    global score

    print('Welcome to the Calculator Game\n')

    keep_playing = True

    while keep_playing: # keep_playing
        while True: #validar opcao dificuldade
            dif_level = input('\nPlease set up the the difficulty level for this round:\n1) easy\n2) intermediate\n3) hard\n4) expert')

            if dif_level.lower() not in ['1', '2', '3', '4', 'easy', 'intermediate', 'hard', 'expert']:
                print('\nInvalid choice, choose one of the following levels:\n')
            else:
                break

        calc = Calculator(dif_level)

#Checking answers
        print(calc.show_operation())

        while True: #validar resposta para que seja valor inteiro
            try:
                answer = int(input())
            except ValueError:
                print('Invalid value')
            else:
                break

        if answer == calc.result:
            score += 1
            print(f'Right on! You scored 1 point\nTotal score:{score}')
        else:
            print(f'\nWrong answer!!\nThe correct answer is {calc.result}\nTotal Score:{score}')

        while True: #validar opcao keep playing
            opcao = input(f'\nWould you like to keep playing?\n1) yes\n2) no')

            if opcao.lower() in ['1', 'yes', 'y']:
                break
            if opcao.lower() in ['2', 'no', 'n']:
                keep_playing = False
                print(f'\nOk... your final score was {score} point(s).\n\n See ya later')
                break
            else:
                print('Invalid answer')

if __name__ == '__main__':
    play()
