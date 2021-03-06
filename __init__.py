import sys,os
import numpy as np
import time,datetime

def minmax(x):
    return np.min(x),np.max(x)

def minmaxnorm(x):
    _min,_max=minmax(x)
    return (x-_min)/(_max-_min)

def array_info(a,dump=True):
    values=np.min(a),np.max(a),a.shape
    if dump:
        print(*values)
    return values

def stopwatch(func):
    def _f(*args, **kwargs):
        start=time.time()
        print(f'# [START]\t{datetime.datetime.now()}')
        ret=func(*args, **kwargs)
        print(f'# [END]\t\t{datetime.datetime.now()}\n# ELAPSED\t{time.time()-start:.3E} sec')
        return ret

    return _f

def mkdirif(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
