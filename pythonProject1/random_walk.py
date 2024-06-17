import turtle as t
import random

tim = t.Turtle()

colors = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue',
          'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
tim.width(15)
tim.speed('fastest')
directions = [0, 90, 180, 270]
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

