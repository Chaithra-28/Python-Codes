import turtle as t

playerA_score = 0
playerB_score = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#creating leftpaddle

leftpaddle = t.turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("green")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating rightpaddle

rightpaddle = t.turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("green")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball

ball = t.turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(5,5)
ballxdirection = 0.2
ballydirection = 0.2

#creating pen for scorecard update

pen = t.turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center", font=('Arial',24,'normal'))

#moving the leftpaddle

def leftpaddleUp():
	y = leftpaddle.ycor()
	y = y+90
	leftpaddle.sety(y)

def leftpaddleDown():
	y = leftpaddle.ycor()
	y = y-90
	leftpaddle.sety(y)

#moving the rightpaddle

def rightpaddleUp():
	y = rightpaddle.ycor()
	y = y+90
	rightpaddle.sety(y)

def rightpaddleDown():
	y = rightpaddle.ycor()
	y = y-90
	rightpaddle.sety(y)

#Assign keys to play

window.listen()
window.onkeypress(leftpaddle,'w')
window.onkeypress(leftpaddle,'s')
window.onkeypress(rightpaddle,'up')
window.onkeypress(rightpaddle,'down')

while True:
	windows.update()

	#moving the ball

	ball.setx(ball.xcor()+ballxdirection)
	ball.sety(ball.ycor()+ballydirection)

	#settingUp border

	if ball.ycor()>290:
		ball.sety(290)
		ballydirection = ballydirection*-1
	if ball.ycor()>-290:
		ball.sety(-290)
		ballydirection = ballydirection*-1

	if ball.xcor()>390:
		ball.goto(0,0)
		ballxdirection = ballxdirection
		playerA_score = playerA_score+1
		pen.clear()
		pen.write("player A:{} player B:{}".format(playerA_score, playerB_score), align='center', font=('Arial',24,'normal'))

	if (ball.xcor())<-390:
		ball.goto(0,0)
		ballxdirection = ballxdirection*-1
		playerB_score = playerB_score+1
		pen.clear()
		pen.write("player A:{} player B:{}".format(playerA_score, playerB_score), align='center', font=('Arial',24,'normal'))

	#Handling collisions

	if (ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
		ball.setx(340)
		ballxdirection = ballxdirection*-1

	if (ball.xcor()>-340)and(ball.xcor()<-350)and(ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
		ball.setx(-340)
		ballxdirection = ballxdirection*-1

