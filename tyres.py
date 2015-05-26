import numpy as np
from operator import itemgetter
from scipy import interpolate
import math

pit_loss = 21.9
nlaps = 78

def integer_divide(n,k):
    r = [n/k]*k
    r[0:n%k] = [i+1 for i in r[0:n%k]]
    return r

class Tyre(object):
    def __init__(self,amount,curve):
        self.amount = amount
        curve.append((nlaps,20))
        self.piecewise = curve
        self.parse()
        self.calculate_thresholds()


    def parse(self):
        self.curve = np.r_[0.0, np.cumsum(interpolate.interp1d([x[0] for x in self.piecewise],[x[1] for x in self.piecewise])(range(1,nlaps+1))) + pit_loss]

    def calculate_thresholds(self):
        self.thresholds = [(0,0,0)]
        for laps in range(1,nlaps+1):
            self.thresholds.append(min([(laps,n,sum(self.curve[integer_divide(laps,n)])) for n in range(1,self.amount+1)],key=itemgetter(2)))


t = Tyre(3,[(1,0.2),(5,0.0),(10,0.1),(12,0.3),(20,3),(40,4.5)])
print t.curve
print t.thresholds




