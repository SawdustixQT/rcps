import ctypes
import math
import time
    

path = "C:/Projects/rcps/pr-13/sqrt.dll"
sqrt_dll = ctypes.CDLL(path)

def rsqrt(a):
    return sqrt_dll.Q_rsqrt(a)

sqrt_dll.Q_rsqrt.argtypes = [ctypes.c_float]
sqrt_dll.Q_rsqrt.restype = ctypes.c_float

def rsqrt_python(a):
    return 1 / math.sqrt(a)

def check_time(func):
    start = time.time()
    for _ in range(100000):
        func(4)
    end = time.time()
    return end - start

rsqrt_time = check_time(rsqrt)
rsqrt_python_time = check_time(rsqrt_python)
print(f'not py {rsqrt_time}')
print(f'py {rsqrt_python_time}')
