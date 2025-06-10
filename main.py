def decide_direction(sign_color):
    if sign_color == 'red':
        return 'Pass on the right'
    elif sign_color == 'green':
        return 'Pass on the left'
    else:
        return 'Unknown sign color'

color = input('Enter the sign color green or red:')
decision = decide_direction(color)
print(decision)

