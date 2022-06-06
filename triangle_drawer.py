from PIL import Image, ImageDraw
import math
import random
from seed_maker import SeedMaker
from triangle_grower import TriangleGrower
class TriangleDrawer:
  def __init__(self, tabl):
    self.rows = len(tabl)                # rows of triangle
    self.s = math.ceil(4096/3/self.rows) # Distance between hexagon centers
    self.r = self.s/2/0.866              # "radius" of hexagon
    self.tabl = tabl
    self.name = "xor_triangle"

  def draw_hexagon(self, triangle_coordinate, color):
    (x,y) = triangle_coordinate
    coordinates = [(x + self.r*math.cos(math.radians(theta)), y + self.r*math.sin(math.radians(theta))) for theta in range(30,390,60)]
    self.dctx.polygon(coordinates, fill=color)

  def draw_triangular_image(self):
    height = math.ceil(2*self.r + 0.866 * self.s * (self.rows-1))
    width = 2*height
    top_point = (width/2, self.r)
    img = Image.new("RGBA", (width, height), (255,255,255,0))  # create new Image
    self.dctx = ImageDraw.Draw(img)  # create drawing context
    self.fill_hexagons(top_point, self.get_colors())
    del self.dctx  # destroy drawing context
    file_name = "/tmp/" + str(self.name) + ".png"
    flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
    flipped.save(file_name)

  def get_colors(self):
    color1 = (random.randint(175,210),random.randint(175,210),random.randint(175,210))
    color2 = (random.randint(35,70),random.randint(35,70),random.randint(35,70))
    return (color1, color2)

  def fill_hexagons(self, top_point, colors):
    (x_t, y_t) = top_point
    for a in range(self.rows):
      for b in range(self.rows-a):
        if self.tabl[a+b][b] == 0:
          color = colors[0]
        else:
          color = colors[1]
        x = x_t - self.s*(a-b)/2
        y = y_t + 0.866*self.s*(a+b)
        self.draw_hexagon((x, y), color)
