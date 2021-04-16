# @xorTriangles

This is the GitHub repository for my Twitter bot [@xorTriangles](https://twitter.com/xorTriangles/).

This project is based on the [MathOverflow question "Number triangle"](https://mathoverflow.net/q/359138/104733) and inspired by Michael De Vlieger's [illustration](https://oeis.org/A334556/a334556.png) on OEIS sequence [A334556](https://oeis.org/A334556).

## Seeds
Seeds come from the following Mathematica program:
```Mathematica
value[i_, j_, n_] := Binomial[i, j] - If[j == n - i, 1, 0];
xorSeedsBasis[n_] := NullSpace[
  Table[value[i, j, n], {i, 0, n}, {j, 0, n}],
  Modulus -> 2
];
seeds = Flatten[Table[
  Map[
    Mod[Total[#], 2] &, 
    Subsets[xorSeedsBasis[n]][[2;;]]
  ], 
  {n, 0, 20}
 ], 1];
```
