import time
from time import sleep
import pytest
from application.snake import Snake

#if tests fail, may have to increase sleepTime to give game instance more time to execute.
sleepTime = 3

def test_start():
    #create snake game instance, let it run until game over, then test if game over happened.
    snake = Snake()
    snake.snakeStart()
    time.sleep( sleepTime )

    assert snake.gameState == "finished"
    
def test_direction():
    #create snake game instance, change direction to left, wait till game over, test if game over happened after delay.
    snake = Snake()
    snake.snakeStart()
    snake.changeDirection(2)
    time.sleep( sleepTime )

    assert snake.gameState == "finished"

def test_score():
    #create snake game instance, create fruit at specific location, then test if snake grabbed fruit by seeing if score increased.
    snake = Snake()
    snake.snakeStart()
    snake.gridLayout[1][8] = snake.fruitSymbol
    time.sleep( sleepTime )

    assert snake.score[0] > 0
