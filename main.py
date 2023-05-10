from turtle import Screen
import time

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

window_screen = Screen()
window_screen.setup(600, 600)
window_screen.bgcolor("black")
window_screen.tracer(0)
window_screen.title("Welcome to the snake game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

window_screen.listen()
window_screen.onkey(snake.up, "Up")
window_screen.onkey(snake.down, "Down")
window_screen.onkey(snake.left, "Left")
window_screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    window_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_change()
        # scoreboard.clear_score()
    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor() < -285 or \
            snake.segments[0].ycor() > 285:
        game_is_on = False
        scoreboard.game_over()

    # detec collision with tail
    for seg in snake.segments[1:]:
        # if seg == snake.segments[0]:
        #     pass
        if snake.segments[0].distance(seg)<10:
            game_is_on = False
            scoreboard.game_over()



window_screen.exitonclick()
