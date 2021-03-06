class TriangleGrower:
  def __init__(self, modulus = 2):
    self.modulus = modulus

  def next_row(self, row):
    new_row = []
    def xor(i):
      return (row[i] + row[i+1]) % self.modulus
    return list(map(xor, range(len(row)-1)))

  def make_triangle(self, bottom_row):
    triangle = [bottom_row]
    while len(triangle[0]) > 1:
      triangle.insert(0, self.next_row(triangle[0]))
    return triangle
