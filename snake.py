import sense_hat
import time
import random
import collections
import copy

def op(a, b):
    x = [a,b]
    x.sort()
    return x== ["down", "up"] or x == ["left", "right"]
        
class Point(object):
    def __init__(self, x, y):
      self.x=x
      self.y =y
    def __eq__(self, other):
      return self.x == other.x and self.y == other.y
    def intersects(self, points):
        for p in points:
            if p == self:
                return True
        return False
    def __repr__(self):
        return "Point(%d,%d)" % (self.x, self.y)
      
def newFood(snake, n):
    while True:
      p = Point(random.randint(0, 7), random.randint(0, 7))
      if not p.intersects(snake.body) and p !=n:
      
      
      


       return p
     
     




sense=sense_hat.SenseHat()

sense.clear()
green = (0,250,0)

blue =(0,0,250)
none = (0,0,0)
red = (250,0,0)
#Point = collections.namedtuple("Point", ["x", "y"])
start = [Point(0,0), Point(0,1), Point(0,2)]
class Snake(object):
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction
    def next_head(self):
        h = copy.copy(self.head())
        if self.direction == "down":
         h.y=(h.y+1)%8
        elif self.direction == "up":
         h.y = (h.y-1)%8
        elif self.direction == "right":
         h.x = (h.x+1)%8
        elif self.direction == "left":
         h.x=(h.x-1)%8
        return h
         
    def move(self, h):
        old = self.body.pop(0)
        self.body.append(h)
        return old
    def head(self):
        return self.body[-1]
    def eat(self, new):
        self.body.append(new)
    def tail(self):
        return self.body[:-1]
        
    
snake = Snake(start, "down")
food = newFood(snake, Point(0,0))
sense.set_pixel(food.x, food.y, blue)
while True:
 for event in sense.stick.get_events():
    if event.action== "released":
         continue
    if event.direction not in ("up", "down", "left", "right"):
        continue
    if op(event.direction, snake.direction):
        print("igringo")
        continue
    snake.direction = event.direction
    print(snake.direction)
 

    break
 p = snake.next_head()
 if p == food:
     food = newFood(snake, p)
     sense.set_pixel(food.x, food.y, blue)
     snake.eat(p)
 else:
     old = snake.move(p)
     sense.set_pixel(old.x, old.y, none)
 if p.intersects(snake.tail()):
     break

 for b in snake.body:
        sense.set_pixel(b.x, b.y, green)
        
 time.sleep(1.0/(len(snake.body)*0.4))

for x in range(0,8):
  for y in range(0,8):
                p = Point(x,y)
                if p == food or p.intersects(snake.body):
                    continue
                sense.set_pixel(x, y, red)





print("game over %d" % len(snake.body))
        


 
 




 