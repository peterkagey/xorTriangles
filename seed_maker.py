import json
import math
from datetime import datetime

class SeedMaker:
  def __init__(self):
    pass

  def get_basis_vectors(self):
    return json.loads(open("rows.json", "r").read())

  def corresponding_integer(self, basis_vector):
    i = 0
    for x in basis_vector:
      i = 2*i + x
    return i

  def make_tweet_copy(self, basis_vector):
    return "Size: " + str(len(basis_vector)) + "\nSeed: " + str(self.corresponding_integer(basis_vector))

  def get_todays_basis_vector(self):
    all_basis_vectors = json.loads(open("rows.json", "r").read())
    time_since_start = datetime.now() - datetime(2021,4,16)
    todays_index = math.floor(time_since_start.total_seconds()/(12*60*60))
    basis_vector = all_basis_vectors[todays_index]
    return (basis_vector, self.make_tweet_copy(basis_vector))
