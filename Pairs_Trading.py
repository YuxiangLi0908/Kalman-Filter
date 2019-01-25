import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import fix_yahoo_finance as fyf
import numpy as np
from pykalman import KalmanFilter

start = dt.datetime(2010,1,1)
end = dt.datetime(2014,8,1)

tik = ['EWA', 'EWC']
data = fyf.download(tik, start, end)['Adj Close']
obs_mat = np.vstack([data.EWA, np.ones(data.EWA.shape)]).T[:, np.newaxis]
delta = 1e-5
trans_cov = delta * np.eye(2)
kf = KalmanFilter(n_dim_obs=1, n_dim_state=2,
                  initial_state_mean=np.zeros(2),
                  initial_state_covariance=np.ones((2, 2)),
                  transition_matrices=np.eye(2),
                  observation_matrices=obs_mat,
                  observation_covariance=1.0,
                  transition_covariance=trans_cov)
state_means, state_covs = kf.filter(data.EWC.values)
pd.DataFrame(state_means)[0].plot(label='Hedge Ratio')
pd.DataFrame(state_means)[1].plot(label='Intercept')
plt.title('Hedge Ratio & Intercept through Time', fontweight='bold')
plt.legend()
plt.show()