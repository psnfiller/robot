import sense_hat
import time
import random
import sys
import urllib

sense=sense_hat.SenseHat()
current=""
while True:
  old = current
  for event in sense.stick.get_events():
    if event.action == 'held':
      pass
    elif event.action == "released":
      current = ""
    elif event.action == "pressed":
      current = event.direction
    else:
      print(event)
      sys.exit(1)
  if old == current:
    continue
  print current
  params = {}
  left=90
  right=100
  if current == "up":
    params['l'] = left
    params['r'] = right
  elif current == "down":
    params['l'] = -left
    params['r'] = -right
  elif current == "left":
    params['l'] = left
    params['r'] = -right
  elif current == "right":
    params['l'] = -left
    params['r'] = right
  elif current == "" or current== 'middle':
    params['l'] = 0
    params['r'] = 0
  else:
    print(current)
    sys.exit(1)
  print(params)
  f = urllib.urlopen('http://robot:5000/motor?%s' % urllib.urlencode(params))













