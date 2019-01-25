Kalman-Filter
=

# Introduction
This is about figuring out how Kalman Filter works. Here are some online materials

https://scipy-cookbook.readthedocs.io/items/KalmanFiltering.html     
https://pykalman.github.io/     
https://www.quantopian.com/lectures/kalman-filters#notebook_tab     
http://www.thealgoengineer.com/2014/online_linear_regression_kalman_filter/     

# Math Behind Kalman-Filter

## Notations

Z - true value    
z - observation values    
R - covariance of z    
x - estimate of Z (usually assigned to 0)    
P - covariance of x (usually assigned to 1)    
Q - transition covariance (usually assigned to 1e-5)    
Kg - Kalman Gain (a weight between observation and estimation)    

## Idea
Assume true value is constant     
At time t-1, we guess x(t) = x(t-1), then P(t) = P(t-1) + Q     
At time t, we get z(t). Then we use x(t) and z(t) to get a better x(t) and P(t) (I use x'(t) and P'(t)). Then back to previous step.

<a href="https://www.codecogs.com/eqnedit.php?latex=x(t)&space;=&space;x(t-1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x(t)&space;=&space;x(t-1)" title="x(t) = x(t-1)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=P(t)&space;=&space;P(t-1)&space;&plus;&space;Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(t)&space;=&space;P(t-1)&space;&plus;&space;Q" title="P(t) = P(t-1) + Q" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=Kg&space;=&space;P(t)&space;/&space;(P(t)&space;&plus;&space;R)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Kg&space;=&space;P(t)&space;/&space;(P(t)&space;&plus;&space;R)" title="Kg = P(t) / (P(t) + R)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=x'(t)&space;=&space;x(t)&space;&plus;&space;Kg&space;*&space;(z(t)&space;-&space;x(t))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x'(t)&space;=&space;x(t)&space;&plus;&space;Kg&space;*&space;(z(t)&space;-&space;x(t))" title="x'(t) = x(t) + Kg * (z(t) - x(t))" /></a> # This equals to weighted average between Z(t) and x(t-1)

<a href="https://www.codecogs.com/eqnedit.php?latex=P'(t)&space;=&space;(1&space;-&space;Kg)&space;*&space;P(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P'(t)&space;=&space;(1&space;-&space;Kg)&space;*&space;P(t)" title="P'(t) = (1 - Kg) * P(t)" /></a>   

how to get the new P'(t) in previous step     
rewrite

<a href="https://www.codecogs.com/eqnedit.php?latex=x'(t)&space;=&space;(1&space;-&space;Kg)&space;*&space;x(t)&space;&plus;&space;Kg&space;*&space;(z(t))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x'(t)&space;=&space;(1&space;-&space;Kg)&space;*&space;x(t)&space;&plus;&space;Kg&space;*&space;(z(t))" title="x'(t) = (1 - Kg) * x(t) + Kg * (z(t))" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=P'(t)&space;=&space;(1&space;-&space;Kg)^2&space;*&space;sigma(x(t))&space;&plus;&space;Kg^2&space;*&space;sigma(z(t))&space;=&space;(1&space;-&space;Kg)^2&space;*&space;P(t)&space;&plus;&space;Kg^2&space;*&space;R&space;=&space;(1&space;-&space;Kg)^2&space;*&space;P(t)&space;&plus;&space;Kg^2&space;*&space;(P(t)&space;/&space;Kg&space;-&space;P(t))&space;=&space;(1&space;-&space;Kg)&space;*&space;P(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P'(t)&space;=&space;(1&space;-&space;Kg)^2&space;*&space;sigma(x(t))&space;&plus;&space;Kg^2&space;*&space;sigma(z(t))&space;=&space;(1&space;-&space;Kg)^2&space;*&space;P(t)&space;&plus;&space;Kg^2&space;*&space;R&space;=&space;(1&space;-&space;Kg)^2&space;*&space;P(t)&space;&plus;&space;Kg^2&space;*&space;(P(t)&space;/&space;Kg&space;-&space;P(t))&space;=&space;(1&space;-&space;Kg)&space;*&space;P(t)" title="P'(t) = (1 - Kg)^2 * sigma(x(t)) + Kg^2 * sigma(z(t)) = (1 - Kg)^2 * P(t) + Kg^2 * R = (1 - Kg)^2 * P(t) + Kg^2 * (P(t) / Kg - P(t)) = (1 - Kg) * P(t)" /></a>
 
 Here, we use
 
 <a href="https://www.codecogs.com/eqnedit.php?latex=Kg&space;=&space;P(t)&space;/&space;(P(t)&space;&plus;&space;R)&space;to&space;get&space;R&space;=&space;P(t)&space;/&space;Kg&space;-&space;P(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Kg&space;=&space;P(t)&space;/&space;(P(t)&space;&plus;&space;R)&space;to&space;get&space;R&space;=&space;P(t)&space;/&space;Kg&space;-&space;P(t)" title="Kg = P(t) / (P(t) + R) to get R = P(t) / Kg - P(t)" /></a>
       
Finally, replace x(t) and P(t) with x'(t) and P'(t). Then we can begin next iteration.

# Simple example

To further illustrate Kalman-Filter. We generate some sample data and observations with noises, and try to apply Kalman-Filter to our observations. Let's see what happens.

In Simple_Excample, we assume true value is -0.37727, we generate 50 observations with normally distributed noise with mean 0 and variance 0.01. We also assume process variance is 1e-5. Our initial estimation and its covariance is 0 and 1. By iteratively apply Kalman-Filter, we can then get our estimation for the true value through time.

Here is the result

![](https://github.com/YuxiangLi0908/Kalman-Filter/blob/master/estimate_vs_iterations.png)

Although we get huge bias at the initial guess, but our estimation converges to true value very fast.

![](https://github.com/YuxiangLi0908/Kalman-Filter/blob/master/error_vs_iterations.png)

We can see that the error is gradually reducing through iterations. And it reduces very fast at the beginning.

Python also has a library `pykalman`. This module implements two algorithms for tracking: the Kalman Filter and Kalman Smoother. In addition, model parameters which are traditionally specified by hand can also be learned by the implemented EM algorithm without any labeled training data. All three algorithms are contained in the KalmanFilter class in this module.

https://pykalman.github.io/#kalman-filter-user-s-guide

Here is the result by using `pykalman`

![](https://github.com/YuxiangLi0908/Kalman-Filter/blob/master/pykalman.png)

# Pairs Trading

Pairs trading is a market-neutral trading strategy that matches a long position with a short position in a pair of highly correlated instruments such as two stocks, exchange-traded funds (ETFs), currencies, commodities or options. The long and short positions (also called hedge ratio) of the pairs can be calculated simply by linear regression between the two assets. However, the relation between two assets isn't always a constant in real world. In this situation, Kalman-Filter is a good method to calculate the hedge ratio.

Here is the result of applying Kalman-Filter to EWC and EWA with time horizon 2010-01-01 to 2014-08-01

![](https://github.com/YuxiangLi0908/Kalman-Filter/blob/master/Pair_Trading.png)
