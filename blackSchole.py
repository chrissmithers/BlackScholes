from scipy.stats import norm
from math import *

def blackScholes(isCall, stock, strike, time, rate, divYield,volatility):
	tempA = (log(float(stock)/strike)
	tempB = rate + ((volatility**2) /2)
	tempC = v * sqrt(time)
	d1 = (tempA + tempB)/ tempC
	d2 = d1 - (v*sqrt(time))

	if isCall:
		temp1 = stock*exp(-divYield*time)*norm.cdf(d1)
		temp2 = strike*exp(-rate*time)*norm.cdf(d2)
		return temp1 - temp2
	else:
		temp1 = strike*exp(-rate*time)*norm.cdf(-d2)
		temp2 = stock*exp(-divYield*time)*norm.cdf(d-1)
		return temp1 - temp2

import matplotlib.animation
import matplotlib.pyplot as plot
import numpy

plot.clf()
figure, ax = plt.subplots()

maturity = 0

stock = np.linspace(80,120,200)

p = []

for i in stock:
	p.append(blackScholes(True, i, 100, 0.005, 0.06, 0, 0.04))

line, = ax.plot(p)