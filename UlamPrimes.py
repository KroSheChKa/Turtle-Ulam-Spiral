from turtle import *
from time import time
from svg_turtle import SvgTurtle

def write(d,f,w,h):
    t = SvgTurtle(w,h)
    d(t)
    t.save_as(f)

def draw(t, number = 2):
    index = 0
    t._tracer(0)
    t.up()
    t.forward(step)
    t.dot(dot_size)
    t.backward(step)

    for s in range(2, s_to*2):
        s //= 2
        if s % 100 == 0: print(s, time() - start_time)
        while s > 0:
            straight = primes[index+1] - number + 1
            
            if straight > s:
                t.forward(step * s)
                number += s
                break
            else:
                t.forward(step * straight)
                t.dot(dot_size)
                index += 1
                s -= straight
                number += straight
        t.left(90)

step = 4
dot_size = 5
s_to = 1500
primes = list(map(int, open('primes.txt')))
start_time = time()
write(draw, 'output.svg', step*s_to+dot_size*2, step*s_to+dot_size*2)
print(time() - start_time)
