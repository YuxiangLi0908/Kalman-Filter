# Kalman-Filter

This is about figuring out how Kalman Filter works

Here are some online materials

https://scipy-cookbook.readthedocs.io/items/KalmanFiltering.html     
https://pykalman.github.io/     
https://www.quantopian.com/lectures/kalman-filters#notebook_tab     
http://www.thealgoengineer.com/2014/online_linear_regression_kalman_filter/     

Z - true value    
z - observation values    
R - covariance of z    
x - estimate of Z (usually assigned to 0)    
P - covariance of x (usually assigned to 1)    
Q - transition covariance (usually assigned to 1e-5)    
Kg - Kalman Gain (a weight between observation and estimation)    

Idea: 
Assume true value is constant     
At time t-1, we guess x(t) = x(t-1), then P(t) = P(t-1) + Q     
At time t, we get z(t). Then we use x(t) and z(t) to get a better x(t) and P(t) (I use x'(t) and P'(t)). Then back to previous step.    

x(t) = x(t-1)    
P(t) = P(t-1) + Q    
Kg = P(t) / (P(t) + R)    
x'(t) = x(t) + Kg * (z(t) - x(t))     # This equals to weighted average between Z(t) and x(t-1)    
P'(t) = (1 - Kg) * P(t)    

how to get the new P'(t) in previous step     
rewrite x'(t) = (1 - Kg) * x(t) + Kg * (z(t))     
P'(t) = (1 - Kg)^2 * sigma(x(t)) + Kg^2 * sigma(z(t))    
      = (1 - Kg)^2 * P(t) + Kg^2 * R                      # rewrite Kg = P(t) / (P(t) + R) to get R = P(t) / Kg - P(t)     
      = (1 - Kg)^2 * P(t) + Kg^2 * (P(t) / Kg - P(t))     
      = (1 - Kg) * P(t)     
Finally, replace x(t) and P(t) with x'(t) and P'(t). Then we can begin next interation.     
