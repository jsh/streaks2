# Decomposing Sequences

Below, I show five decompositions of the 3! = 6 permutations of the elements {1, 2, 4}.
I choose these particular integers because all subsets have different means from the set mean.
This guarantees that the trend decompositions are all possible and unique.

I choose integers because they're easier to write than three random reals. :-)


## Decompositions

The first three well-defined decompositions are into

- cycles (standard permutation cycles),
- trends (quasi-increasing sequences), and
- winning streaks (sequences in which the first element is the smallest)

to these, I add

- reverse trends (quasi-decreasing sequences), and
- reverse streaks (sequences in which the first element is the largest)

The algorithms for all are greedy and `O(N)`, though the algorithms for both trend-flavored decompositions are recursive.


| Permutation | Cycles   | Trends   | Streaks  | Reverse<br>Trends | Reverse<br>Streaks |
|-------------|----------|----------|----------|-------------------|--------------------|
|             |          |          |          |                   |                    |
| 1 2 4       | (1)(2)(4)| (1 2 4)  | (1 2 4)  | (1)(2)(4)         | (1)(2)(4)          |
| 1 4 2       | (1)(2 4) | (1 4)(2) | (1 4 2)  | (1)(4 2)          | (1)(4 2)           |
| 2 1 4       | (1 2)(4) | (2 1 4)  | (2)(1 4) | (2 1)(4)          | (2 1)(4)           |
| 2 4 1       | (1 2 4)  | (2 4)(1) | (2 4)(1) | (2)(4 1)          | (2)(4 1)           |
| 4 1 2       | (1 4 2)  | (4)(1 2) | (4)(1 2) | (4 1 2)           | (4 1 2)            |
| 4 2 1       | (1 4)(2) | (4)(2)(1)| (4)(2)(1)| (4 2 1)           | (4 2 1)            |

***

## Normalized

Here, I map the integers above, {1, 2, 4}, to their rank orders, {1, 2, 3}, and re-write each block (cycle equivalent)
using the standard convention for permutation cycles:

- circularly permute each block until the smallest element is first
- re-order blocks so their smallest elements are strictly increasing

Note that the decompositions are no longer "correct" -- this is just a re-labeling.

| Permutation | Cycles   | Trends   | Streaks  | Reverse<br>Trends | Reverse<br>Streaks |
|-------------|----------|----------|----------|-------------------|--------------------|
|             |          |          |          |                   |                    |
| 1 2 3       | (1)(2)(3)| (1 2 3)  | (1 2 3)  | (1)(2)(3)         | (1)(2)(3)          |
| 1 3 2       | (1)(2 3) | (1 3)(2) | (1 3 2)  | (1)(2 3)          | (1)(2 3)           |
| 2 1 3       | (1 2)(3) | (1 3 2)  | (1 3)(2) | (1 2)(3)          | (1 2)(3)           |
| 2 3 1       | (1 2 3)  | (1)(2 3) | (1)(2 3) | (1 3)(2)          | (1 3)(2)           |
| 3 1 2       | (1 3 2)  | (1 2)(3) | (1 2)(3) | (1 2 3)           | (1 2 3)            |
| 3 2 1       | (1 3)(2) | (1)(2)(3)| (1)(2)(3)| (1 3 2)           | (1 3 2)            |

***

## Observation

Permutations can be decomposed into adjacent cycles, trends, or streaks, uniquely.
Reverse trend and reverse streak decompositions are also straightforward.
Interestingly, for permutations on three elements, cycle, trend, and streak decompositions are all distinct, but have 1-1 mappings to one another. The reverse trend and streak decompositions are also different from the first three, but identical to one another.

Thus, we know five straightforward decompositions that produce four different decompositions.

*However*, there are 6! = 720 possible mappings of permutations to decompositions.
We could, thus, add 716 more columns to the tables above, each of which corresponds to a distinct way to decompose a sequence of three elements into blocks.

***

## Questions

- Why do reverse trends and reverse streaks produce the same decompositions?
- Is this identity for permutations on `N` elements true for all `N`?
- Is there some way to find the rule that produces each (any?) of the other 716 possible decompositions on 3 elements?
- Does the method generalize to ways to find novel decompositions of sequences of `N` elements?
- Is there a general way to choose a set of `N` integers that has the property "all subset means are distinct from the set mean"?
- Is there a way that isn't NP-complete?
- Is the re-labeling in the **Normalized** section useful?
