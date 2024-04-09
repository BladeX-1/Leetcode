from sys import *
from collections import *
from math import *

from typing import List

def subsetSum(arr: List[int]) -> List[int]:
    full = []
    f(arr,0,len(arr),0,full)
    full.sort()
    return full    

def f(arr,i,n,partialsum,fullarr):
    if(i==n):
        fullarr.append(partialsum)
        return
    else:
        f(arr,i+1,n,partialsum,fullarr)
        f(arr,i+1,n,partialsum+arr[i],fullarr)