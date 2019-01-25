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
       
Finally, replace x(t) and P(t) with x'(t) and P'(t). Then we can begin next interation.
