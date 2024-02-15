import turtle
# we will create object for this turtle
tu= turtle.Turtle() #make sure to keep this T capital
tu.screen.bgcolor("black") #background color will change to black
tu.pensize(2) #size of pen
tu.color("green") #initially the color of the turtle will be green


tu.left(90)


tu.backward(100)
tu.speed(650000)
tu.shape('turtle')


def tree(i):
    if i<10:
        return
    
    else:
        tu.forward(i)
        tu.color("orange")
        tu.circle(2)

        tu.color("brown")


        tu.left(30)
        tree(3*i/4)
        tu.right(60)
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)
tree(100)
turtle.done()       