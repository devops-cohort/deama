import pytest
from application.snake import Snake


def test_thing():
    snake = Snake()
    snake.start()
    assert snake.snakeSpeed == 0
