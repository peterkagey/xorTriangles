from twitter_connection import TwitterConnection
from seed_maker import SeedMaker
from triangle_grower import TriangleGrower
from triangle_drawer import TriangleDrawer

api = TwitterConnection().api

def handler(event, context):
  if "seed" in event and "tweet_copy" in event:
    seed = event['seed']
    tweet_copy = event['tweet_copy']
  else:
    (seed, tweet_copy) = SeedMaker().get_todays_basis_vector()
  triangle = TriangleGrower().make_triangle(seed)
  TriangleDrawer(triangle).draw_triangular_image()
  file_with_path = "/tmp/xor_triangle.png"
  api.update_with_media(filename=file_with_path, status=tweet_copy)
  return "Posted Tweet with message: '" + tweet_copy + "'"
