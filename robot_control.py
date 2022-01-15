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
  if current == "up":
    params['l'] = 60
    params['r'] = 60
  elif current == "down":
    params['l'] = -60
    params['r'] = -60
  elif current == "left":
    params['l'] = -60
    params['r'] = 60
  elif current == "right":
    params['l'] = 60
    params['r'] = -60
  elif current == "" or current== 'middle':
    params['l'] = 0
    params['r'] = 0
  else:
    print(current)
    sys.exit(1)
  f = urllib.urlopen('http://robot:5000/motor?%s' % urllib.urlencode(params))
  print(f.read())













