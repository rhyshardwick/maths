import visual, math

ball = visual.sphere()
box = visual.box( pos=[0,-1,0], width=4, length=4, height=0.5 )
trace=visual.curve( radius=0.2, color=visual.color.green)

for i in range(1000):
    t = i*0.1
    y = math.sin(t)

    #update the ball's position
    ball.pos = [t, y, 0]

    trace.append( ball.pos )

    #ensure we have only 24 frames per second
    visual.rate(24)
