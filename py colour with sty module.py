import random
from sty import fg
def colour():
    red = random.randint(0,256)
    green = random.randint(0,256)
    pink = random.randint(0,256)
    return red,green,pink
def generate(red,green,pink):
    return fg(red,green,pink)
s,n,s = colour()
y = generate(s,n,s)
print(y,"colours",fg.rs)
    
