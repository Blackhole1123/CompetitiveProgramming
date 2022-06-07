# format: 212 ,-7 ,284 into D400FF

def clamp(x): 
  return max(0, min(x, 255))

def rgb(r, g, b):
  return '{:02x}{:02x}{:02x}'.format(clamp(r), clamp(g), clamp(b)).upper()

print(rgb(255, 255, 255))