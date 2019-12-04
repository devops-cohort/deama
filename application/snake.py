import time
import random
from threading import Timer
from time import sleep 


class Snake():
    gridLayout = []
    snake = [] #snake starting length, last entry is placeholder
    arenaX = 40
    arenaY = 20

    #lower = faster
    refresh = 0.05
    snakeSpeed = 0
    fruitSpawnTime = 0

    gridSymbol = "#"
    fruitSymbol = "@"

    snakeHeadSymbol = "+"
    snakeTailSymbol = "="

    direction = [0] #0 = up, 1 = down, 2 = left, 3 = right
    score = [0]
    runGame = [0] #0 = run, 1 = stop

    thread1 = None
    thread2 = None







#Threads----------------------------------------------------------------
    def snakeMovement(self): #thread
        try:
            storeOld = [0,0]
            storeOld2 = [0,0]
            while self.runGame[0] == 0:
                storeOld[0] = self.snake[0][0]
                storeOld[1] = self.snake[0][1]
                if self.direction[0] == 0:
                    self.snake[0][0] = self.snake[0][0] - 1
                elif self.direction[0] == 1:
                    self.snake[0][0] = self.snake[0][0] + 1
                elif self.direction[0] == 2:
                    self.snake[0][1] = self.snake[0][1] - 1
                elif self.direction[0] == 3:
                    self.snake[0][1] = self.snake[0][1] + 1

                if self.gridLayout[ self.snake[0][0] ][ self.snake[0][1] ] == self.fruitSymbol: #make snake longer when fruit eaten, and speed snake up
                    self.snake.append([0,0])
                    self.score[0] = self.score[0] + 1
                    self.snakeSpeed = self.snakeSpeed / 1.04
                    
                if self.gridLayout[ self.snake[0][0] ][ self.snake[0][1] ] == self.snakeTailSymbol: #end game when snake head meets snake tail
                    self.runGame[0] = 1

                if self.snake[0][0] < 0 or self.snake[0][1] < 0: #prevent snake from going negative
                    self.runGame[0] = 1

                for i in range( 1, len(self.snake) ):
                    storeOld2[0] = self.snake[i][0]
                    storeOld2[1] = self.snake[i][1]
                    self.snake[i][0] = storeOld[0]
                    self.snake[i][1] = storeOld[1]
                    storeOld[0] = storeOld2[0]
                    storeOld[1] = storeOld2[1]

                self.snakeDraw()
                        
                self.gridLayout[ self.snake[len(self.snake)-1][0] ][ self.snake[len(self.snake)-1][1] ] = self.gridSymbol
                
                time.sleep(self.snakeSpeed)
        except:
            self.runGame[0] = 1
        return


    def fruit(self):
        while self.runGame[0] == 0:
            x = random.randint(0, len(self.gridLayout)-1)
            y = random.randint(0, len(self.gridLayout[0])-1)

            try:
                self.gridLayout[x][y] = self.fruitSymbol
            except:
                print("BAD RANDOM:", x,y, flush=True)
                print("BAD RANDOM2:", len(self.gridLayout)-1,len(self.gridLayout[0])-1, flush=True)
                pass

            time.sleep(self.fruitSpawnTime)
        return

#Threads END------------------------------------------------------------





            
#Functions--------------------------------------------------------------
    def getScore(self):
        return self.score[0]

    def getGrid(self):
        return self.gridLayout

    def change(self, key): 
        if self.direction[0] == 0 and key == 1:
            pass
        elif self.direction[0] == 1 and key == 0:
            pass
        elif self.direction[0] == 2 and key == 3:
            pass
        elif self.direction[0] == 3 and key == 2:
            pass
        else:
            self.direction[0] = key

    def snakeDraw(self):
        for i in range( len(self.snake)-1 ): #-1 maybe error?
            if i == 0:
                self.gridLayout[self.snake[i][0]][self.snake[i][1]] = self.snakeHeadSymbol #head
            else:
                self.gridLayout[self.snake[i][0]][self.snake[i][1]] = self.snakeTailSymbol #tail

    def snakeStart(self):
        self.snake = [[11,8],[11,9],[11,10],[11,11]]
        self.gridLayout = []
        self.direction[0] = 0
        self.score[0] = 0
        self.snakeSpeed = 0.1
        self.fruitSpawnTime = 3


        for i in range(0, self.arenaY): #y
            self.gridLayout.append([])
            for p in range(0, self.arenaX): #X
                self.gridLayout[i].append(self.gridSymbol)

        if self.thread1 == None and self.thread2 == None:
            self.thread1 = Timer( self.refresh*5, self.snakeMovement )#moves snake around arena
            self.thread1.start()

            self.thread2 = Timer( self.refresh*10, self.fruit )
            self.thread2.start()

        return self.gridLayout

#Functions END-----------------------------------------------------------
