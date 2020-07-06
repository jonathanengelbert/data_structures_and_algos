# Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.

import turtle
from random import randint

def tree(branchLen,t):
    if branchLen > 5:
        # this decreases size of branch as length increases
        t.width(branchLen / 5)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    t.width(20)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75,t)
    myWin.exitonclick()

main()

