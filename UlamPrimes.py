from turtle import *
from time import time
from svg_turtle import SvgTurtle

def group(arr):
    substr_lengths = []
    count = 1
    current_num = arr[0]
    for num in arr[1:]:
        if num == current_num:
            count += 1
        else:
            substr_lengths.append(count)
            count = 1
            current_num = num
    substr_lengths.append(count)
    return substr_lengths

def is_prime(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

def write(d,f,w,h):
    t = SvgTurtle(w,h)
    d(t)
    t.save_as(f)

def draw(t, number = 2):
    t._tracer(0)
    t.up()
    for s in range(2, s_to*2):
        s //= 2
        if s % 100 == 0: print(s, time() - start_time)
        primes = [is_prime(i) for i in range(number, number + s)]
        flag = primes[0]
        for i in group(primes):
            t.forward(step*i)
            number += i
            if flag:
                t.dot(dot_size)
            flag = not flag
        t.left(90)

step = 4
dot_size = 5
s_to = 600
start_time = time()
write(draw, 'output.svg', step*s_to+dot_size*2, step*s_to+dot_size*2)
print(time() - start_time)