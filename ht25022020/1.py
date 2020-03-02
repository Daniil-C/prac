from turtle import *
from random import *
import math


SIZE = 700


def rand_rad(l, r):
	rad = randrange(l,r)
	while abs(rad) < (r - l) / 25:
		rad = randrange(l,r)
	return rad


def pos_next(t, rad, l):
	astamp = t.stamp()
	t.up()
	t.speed(0)
	t.circle(rad, l)
	pos = t.pos()
	t.left(180)
	t.circle(-rad, l)
	t.left(180)
	t.speed(6)
	t.clearstamp(astamp)
	t.down()
	return pos


def in_sq(pos, bord):
	if abs(pos[0]) < bord / 2 and abs(pos[1]) < bord / 2:
		return True
	return False

def square(t, a):
	for i in range(4):
		t.fd(a)
		t.right(90)

border = SIZE * 0.9
t = Turtle()
t.up()
t.speed(0)
t.setpos(-border/2, border/2)
t.down()
square(t, border)
t.up()
t.setpos(0, 0)
t.down()
t.pensize(3)
t.screen.setup(SIZE, SIZE)
t.speed(6)
for i in range(100):
    rad = rand_rad(-60, 60)
    l = randrange(10, 200)
    while not in_sq(t.pos(), border - 4 * abs(rad)) and not in_sq(pos_next(t, rad, l), border):
    	rad = rand_rad(-60, 60)
    	l = randrange(20, 200)
    t.color(random(), random(), random())
    t.circle(rad, l)
exitonclick()
