from turtle import Turtle

SCORE = 0

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score_change()


    def score_change(self):
        self.clear()
        self.write(f'Score : {self.score}', align="center", font=('Verdana', 15, 'normal'))
        print(self.score)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write('Game is over', align="center", font=('Verdana', 15, 'normal'))




