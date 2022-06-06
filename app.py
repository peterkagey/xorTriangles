from twitter_connection import TwitterConnection
from seed_maker import SeedMaker
from triangle_grower import TriangleGrower
from triangle_drawer import TriangleDrawer

api = TwitterConnection().api

def handler(event, _):
  if "modulus" in event:
    modulus = event['modulus']
  else:
    modulus = 2
  if "seed" in event and "tweet_copy" in event:
    seed = event['seed']
    tweet_copy = event['tweet_copy']
  else:
    (seed, tweet_copy) = SeedMaker(modulus).get_todays_basis_vector()
  triangle = TriangleGrower(modulus).make_triangle(seed)
  TriangleDrawer(triangle).draw_triangular_image()
  file_with_path = "/tmp/xor_triangle.png"
  api.update_status_with_media(filename=file_with_path, status=tweet_copy)
  return "Posted Tweet with message: '" + tweet_copy + "'"
