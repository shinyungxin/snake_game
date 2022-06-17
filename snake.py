# imports
import turtle
import time
import random

delay = 0.1

# scores
score = 0
high_score = 0

# set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("yellow")
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off the screen update

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# snake body
segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# functions
def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)


def go_up():
	if head.direction != "down":
		head.direction = "up"


def go_down():
	if head.direction != "up":
		head.direction = "down"


def go_left():
	if head.direction != "right":
		head.direction = "left"


def go_right():
	if head.direction != "left":
		head.direction = "right"


# keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# main game loop
while True:
	wn.update()

	# check if the head touches the border
	if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"

		# hide the segment
		for segment in segments:
			segment.goto(1000, 1000)

		# remove the segments
		segments.clear()

		# reset score
		score = 0

		# show new score on screen
		pen.clear()
		pen.write("Score : {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

	# check if the head touches the food
	if head.distance(food) < 20:
		# Move food to random position
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)

		# Add a segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()
		segments.append(new_segment)

		# increase the score
		score += 10

		# check high score
		if score >= high_score:
			high_score = score

		# show new score on screen
		pen.clear()
		pen.write("Score : {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

	# move the end segment first
	for index in range(len(segments) - 1, 0, -1):
		x = segments[index - 1].xcor()
		y = segments[index - 1].ycor()
		segments[index].goto(x, y)

	# move segment 0 to where the head is
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	move()

	# check if the head touches the body
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"

			# hide the segment
			for seg in segments:
				seg.goto(1000, 1000)

			# remove the segments
			segments.clear()

			# reset score
			score = 0

			# show new score on screen
			pen.clear()
			pen.write("Score : {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

	time.sleep(delay)

wn.mainloop()
