import random


def game_Calculator_3000(n_rounds):
    """take INT as argument for game rounds"""
    game_rounds = 0
    while game_rounds != n_rounds:
        value_1 = random.randint(1 ,10)
        value_2 = random.randint(1 ,10)
        result = value_1 + value_2
        try:
            user_answer = int(input(f'Hello User Please do the follow task:\ncalculate {value_1} + {value_2} = \n'))
        except ValueError as invalid_input:
            print(invalid_input)
            continue
        if user_answer == result:
            print('Very Good')
            game_rounds += 1
        else :
            print("Not realy")
    print(f'Congrats you made it very nice !')

def start_game_Calculator_3000():
    """\033[33;1mstarts game by calling 'game_Calculator_3000' with an INT\033[0m"""
    while True:
        try:
            user_input = int(input('Hello User :) \nPlease type a number for rounds u wanna play :\n'))
        except ValueError as e:
            print(f'\033[31m{e}\033[0m')
            continue
        game_Calculator_3000(user_input)
        break
    print("Thank's for playing")
        
if __name__ == '__main__':
    start_game_Calculator_3000()