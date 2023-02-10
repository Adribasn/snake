import pyxel

class Snake():
    def __init__(self):
        self.x = 0
        self.y = 20
        self.score = 0
        self.direction = 'right'
        pyxel.init(45, 53, title="Snake", fps=20)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.direction == 'right':
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= 1
                self.direction = 'up'
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.y += 1
                self.direction = 'down'
            else:
                self.x += 1
        elif self.direction == 'left':
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= 1
                self.direction = 'up'
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.y += 1
                self.direction = 'down'
            else:
                self.x -= 1
        elif self.direction == 'up':
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 1
                self.direction = 'left'
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 1
                self.direction = 'right'
            else:
                self.y -= 1
        elif self.direction == 'down':
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 1
                self.direction = 'left'
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 1
                self.direction = 'right'
            else:
                self.y += 1

        if not (0 <= self.x < 45 and 8 <= self.y < 53):
            self.x = 0
            self.y = 20
            self.direction = 'right'

    def draw(self):
        pyxel.cls(1)
        pyxel.rect(0,0,45,8,6)
        pyxel.rect(self.x, self.y, 1, 1, 6)
        pyxel.rect(23, 34, 1, 1 , 7)

Snake()