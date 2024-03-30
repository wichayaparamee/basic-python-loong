import turtle
from random import random
from random import random,choice

tao=turtle.Pen()
tao.shape('turtle')

count = 0
size = 0
for i in range(15):
    
    
    x = choice(['green','blue','red','orange','brown','yellow','black','pink'])
    tao.color(x)
    for i in range(4):
        tao.forward(70+size)
        tao.left(90)
    tao.right(18)
    size += 2
    
