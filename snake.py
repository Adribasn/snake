import pyxel

class Snake():
    def __init__(self):
        self.body = [[0, 20]] 
        self.biasX = 0
        self.biasY = 0
        self.length = 1
        self.score = 0
        self.direction = 'right'
        self.food = [23, 34]
        pyxel.init(45, 53, title="Snake", fps=10)
        pyxel.run(self.update, self.draw)

    def update(self):        
        #Change direction and position of head on click
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

        #add segment to snake body when eating food
        if self.body[0][0] == self.food[0] and self.body[0][1] == self.food[1]:
            self.length += 1

        oldHead = self.body[0]
        newHead = [oldHead[0] + self.biasX, oldHead[1] + self.biasY]
        self.body.insert(0, newHead)
        self.body = self.body[:self.length]

        self.biasX = 0
        self.biasY = 0

        print(self.body)
    
    def draw(self):
        pyxel.cls(1)
        pyxel.rect(0,0,45,8,6)

        #Display each item of the snake body
        for segment in self.body:
            pyxel.rect(segment[0], segment[1], 1, 1, 6)
        
        pyxel.rect(self.food[0], self.food[1], 1, 1 , 7)

Snake()