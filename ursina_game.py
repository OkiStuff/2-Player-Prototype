from ursina import *
from runtime import *


app = Ursina()

player = Entity(model='cube', color=color.blue, scale_y=2, scale_x=3)
playerTwo = Entity(model='sphere', color=color.yellow, x=player.x - 5, scale_y=4, scale_x=1)

#settings = input("Welcome To my first game using the super easy to use Ursina Engine. Enjoy!\nDo you want VSync on? True/False: ")
#isVsync(settings, window)



def update():

    
    window.title = f'Two Player Prototype! - Player 1 Cords {player.x} Player 2 Cords {playerTwo.x}'

    playerTwo.x += held_keys['k'] *.1 # K, left
    playerTwo.x -= held_keys['h'] *.1 # H, right
    playerTwo.y += held_keys['u'] *.2    # U, up
    playerTwo.y -= held_keys['j'] *.2  # J, down


    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1
    player.y += held_keys['w'] * .2
    player.y -= held_keys['s'] * .2

    if held_keys['space']:
        playerTwo.visible = False
        print("Hey, Don't hide me!")

    else:
        playerTwo.visible = True

    #print(f'Player: {player.x} ')






app.run()