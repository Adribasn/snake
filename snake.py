import pyxel
import random

class Snake():
    def __init__(self):
        self.body = [[1, 20]] 
        self.biasX = 0
        self.biasY = 0
        self.length = 1
        self.score = 0
        self.alive = True
        self.direction = 'right'
        self.food = [random.randint(1, 46), random.randint(9, 54)]
        pyxel.init(47, 55, title="Snake", fps=15)
        pyxel.run(self.update, self.draw)

    def update(self):       
        if self.alive:
            self.updateDirection()
            self.eat()
            self.updateSnake()
        else:
            self.reset()
    
    def updateDirection(self):
        if self.direction == 'right':
            if pyxel.btn(pyxel.KEY_UP):
                self.biasY = -1
                self.direction = 'up'
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.biasY = 1
                self.direction = 'down'
            else:
                self.biasX = 1
        elif self.direction == 'left':
            if pyxel.btn(pyxel.KEY_UP):
                self.biasY = -1
                self.direction = 'up'
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.biasY = 1
                self.direction = 'down'
            else:
                self.biasX = -1
        elif self.direction == 'up':
            if pyxel.btn(pyxel.KEY_LEFT):
                self.biasX = -1
                self.direction = 'left'
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.biasX = 1
                self.direction = 'right'
            else:
                self.biasY = -1
        elif self.direction == 'down':
            if pyxel.btn(pyxel.KEY_LEFT):
                self.biasX = -1
                self.direction = 'left'
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.biasX = 1
                self.direction = 'right'
            else:
                self.biasY = 1

    def updateSnake(self):
        oldHead = self.body[0]
        newHead = [oldHead[0] + self.biasX, oldHead[1] + self.biasY]

        if not (1 < newHead[0] < 45 and 9 < newHead[1] < 53):
            self.alive = False

        self.body.insert(0, newHead)
        self.body = self.body[:self.length]

        self.biasX = 0
        self.biasY = 0
    
    def eat(self):
        if self.body[0][0] == self.food[0] and self.body[0][1] == self.food[1]:
            self.length += 1
            self.food[0] = random.randint(0, 44)
            self.food[1] = random.randint(8, 52)
    
    def reset(self):
        self.body = [[1, 20]] 
        self.biasX = 0
        self.biasY = 0
        self.length = 1
        self.score = 0
        self.alive = True
        self.direction = 'right'
        self.food = [random.randint(0, 44), random.randint(8, 52)]

    def draw(self):
        pyxel.cls(14)
        pyxel.rectb(0, 0, 47, 55, 0)
        pyxel.rect(1, 8, 47, 1, 0)

        #Display each item of the snake body
        for segment in self.body:
            pyxel.rect(segment[0], segment[1], 1, 1, 8)
        
        pyxel.rect(self.food[0], self.food[1], 1, 1 , 2)

Snake()