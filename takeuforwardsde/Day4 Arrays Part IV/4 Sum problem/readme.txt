this solution beats 97% users on LeetCode

4-nested loop solution: O(n**4)
use memo for last loop: O(n**3)

additional optimizations:
sort array
in each loop, only accept the first of the repeated values and skip the rest
check if solution is out of bound, and make necessary changes for that