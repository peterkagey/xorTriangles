from argparse import ArgumentError
import json
import math
from datetime import datetime

class SeedMaker:
  def __init__(self, modulus = 2):
    self.modulus = modulus

  def get_basis_vectors(self):
    if self.modulus == 2:
      return json.loads(open("rows2.json", "r").read())
    elif self.modulus == 3:
      return json.loads(open("rows3.json", "r").read())
    else:
      raise ArgumentError(message="Unsupported modulus: " + str(self.modulus))

  def corresponding_integer(self, basis_vector):
    i = 0
    for x in basis_vector:
      i = self.modulus*i + x
    return i

  def make_tweet_copy(self, basis_vector):
    return "Base: " + str(self.modulus) + "\nSize: " + str(len(basis_vector)) + "\nSeed: " + "".join(map(str,basis_vector))

  def get_todays_basis_vector(self):
    all_basis_vectors = self.get_basis_vectors()
    time_since_start = datetime.now() - datetime(2022,6,6)
    # New index every 12 hours.
    todays_index = math.floor(time_since_start.total_seconds()/(12*60*60))
    basis_vector = all_basis_vectors[todays_index]
    return (basis_vector, self.make_tweet_copy(basis_vector))

# coeff[i_, j_, n_] := Binomial[i, j] - If[j + i == n, 1, 0];
# coeff2[i_, j_, n_] := Binomial[i, n - j] - If[j == i, 1, 0];

# TriangleSeedBasis[n_, p_] := NullSpace[
#    Table[coeff[i, j, n - 1], {i, 0, n - 1}, {j, 0, n - 1}]
#     ~Join~
#     Table[coeff2[i, j, n - 1], {i, 0, n - 1}, {j, 0, n - 1}],
#    Modulus -> p
#    ];
# LinearCombination[basis_, coeffs_] :=
#  Total[MapThread[#1*#2 &, {basis, coeffs}]]
# (* Linear combinations with a leading coefficient of 1. *)

# ProjectiveCombinations[basis_, n_] := (
#   dimension = Length[basis];
#   f[i_] := (
#     prefix = ConstantArray[0, i - 1] ~Join~{1};
#     suffixes = Tuples[Range[0, n - 1], dimension - i];
#     coefficients = Map[Join[prefix, #] &, suffixes]
#     );
#   coefficientsList = Flatten[Table[f[i], {i, 1, dimension}], 1];
#   Map[LinearCombination[basis, #] &, coefficientsList]
#   )
# Flatten[Table[ProjectiveCombinations[TriangleSeedBasis[i, 3], 3], {i, 3, 130}], 1]
