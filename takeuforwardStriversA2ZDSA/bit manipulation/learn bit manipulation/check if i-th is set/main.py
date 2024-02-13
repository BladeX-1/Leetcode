from typing import *


def bitManipulation(num: int, i: int) -> List[int]:
    # put the i-th bit at once position, and use filter
    return [(num >> (i - 1)) & 1, (1 << (i - 1)) | num, (num & ~(1 << (i - 1)))]
