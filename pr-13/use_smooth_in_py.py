import time
import ctypes

def smooth(arr, alpha):
    if (len(arr) == 0):
        return
    s = [0] * len(arr)
    s[0] = arr[0]
    