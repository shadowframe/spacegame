import pgzrun

WIDTH = 1024
HEIGHT = 860

ship = Actor('player/playership1_blue.png')
ship.x = 370
ship.y = 550

def update():
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

def draw():
    screen.fill((80,0,70))
    ship.draw()
    
pgzrun.go() # LAST LINE