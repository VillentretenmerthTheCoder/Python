from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()




while True:
  orientation = sense.get_orientation()
  yaw = orientation["yaw"]
  pitch = orientation["pitch"]
  roll = orientation["roll"]
  if pitch >=0:
   r = 255
   g = 255
   b = 255
   sense.clear((r, g, b))
  if pitch >=80:
   r = 35
   g = 12
   b = 213
   sense.clear((r, g, b))
