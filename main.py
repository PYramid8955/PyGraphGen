from random import randint
from graph import GenSvg

with open("test.svg", "w") as f:
    f.write(GenSvg([randint(i, 300) for i in range(300)])) #you can play with data however you want, like in the following example:
    
with open("test1.svg", "w") as f:
    f.write(GenSvg([7, 10, 32, 11, 2, 43, 2, 36, 4, 2, 3, 5, 7, 20]))
