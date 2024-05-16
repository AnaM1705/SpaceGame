import turtle
import random
import math
import winsound
# set up screen

wn = turtle.Screen()
wn.setup(width=700, height=700)
wn.bgpic("spacebg.gif")
wn.bgcolor("black")
wn.title("Space game by Ana")
wn.tracer(0)

wn.register_shape("star.gif")


class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def drawBorder(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)


class ScoreDisplay(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0
        self.write(f'Score = {self.score}',
                   align="left", font=("Courier", 24, "bold"), )

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}',
                   align="left", font=("Courier", 24, "bold"), )

    def change_score(self, points):
        self.score += points
        self.update_score()


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.speed = 0.5 

    def move(self):
        self.forward(self.speed)

        # BORDER CHECKING COLLISION
        if self.xcor() > 290 or self.xcor() < -290:
            self.right(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.right(60)

    def goleft(self):
        self.left(30)

    def goright(self):
        self.right(30)

    def speedup(self):
        self.speed += 0.3

    def slowdown(self):
        self.speed -= 0.3


class Prize(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("star.gif")
        self.color("gold")
        self.speed = 0.2
        # Go to x,y coordinates
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))  # random angle

    def move(self):
        self.forward(self.speed)
        # BORDER CHECKING COLLISION
        if self.xcor() > 290 or self.xcor() < -290:
            self.right(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.right(60)

    def spawn(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))
        self.speed += 0.01
       # self.move()


player = Player()
border = Border()
scoreDisplay = ScoreDisplay()


prizes = []

for count in range(5):
    prizes.append(Prize())
border.drawBorder()


def playSound():
    winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


def isColission(t1, t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a**2) + (b**2))
    if distance < 20:
        return True
    else:
        return False



# Keyboard bindings
turtle.listen()
turtle.onkeypress(player.goleft, "Left")
turtle.onkeypress(player.goright, "Right")
turtle.onkeypress(player.speedup, "Up")
turtle.onkeypress(player.slowdown, "Down")

while True:
    wn.update()
    player.move()
    for prize in prizes:
        prize.move()
        if isColission(player, prize):
            playSound()
            prize.spawn()
            scoreDisplay.change_score(10)
