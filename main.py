dstroke = Actor('dstroke')
dstroke.pos = 100, 56

WIDTH = 500
HEIGHT = dstroke.height + 20

def draw():
    screen.clear()
    dstroke.draw()
