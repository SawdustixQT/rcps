import time
import ctypes

def smooth_c():
    pass

def smooth_py(arr, alpha):
    if (len(arr) == 0):
        return
    s = [0] * len(arr)
    s[0] = arr[0]
    for i in range(1, len(arr)):
        s[i] = s[i - 1] + alpha * (arr[i] - s[i - 1])
    return s


def check_time(func):
    global arr
    start = time.time()
    for _ in range(100000):
        func(arr, 4)
    end = time.time()
    return end - start

print(f"smooth time {check_time(smooth_py)}")
print(f"smooth time {check_time(smooth_c)}")
