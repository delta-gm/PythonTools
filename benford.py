# benfords law

# [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

import numpy as np 
import pandas as pd 
import seaborn as sns
import random
import matplotlib.pyplot as plt
import math

def leadingDigit(n): 
    while n >= 10:  
        n = n / 10
    return int(n) 

BENFORD = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

plt.figure(figsize=(15,10))
plt.plot(BENFORD)
plt.title('Benford law distribution of first digits')
# plt.show()

def chi_square_test(data_count,expected_counts):
    """Return boolean on chi-square test (8 degrees of freedom & P-val=0.05)."""
    chi_square_stat = 0  # chi square test statistic
    for data, expected in zip(data_count,expected_counts):

        chi_square = math.pow(data - expected, 2)

        chi_square_stat += chi_square / expected

    print("\nChi-squared Test Statistic = {:.3f}".format(chi_square_stat))
    print("Critical value at a P-value of 0.05 is 15.51.")    
    return chi_square_stat < 15.51

covid_daily = pd.read_csv('day_wise.csv')
print(covid_daily.head)

confirmed_fd = []
confirmed = covid_daily.Confirmed.values

for i in confirmed:
    confirmed_fd.append(leadingDigit(i))

confired_fd_counts = pd.Series(confirmed_fd).value_counts().values

confired_fd_percent = (confired_fd_counts/np.sum(confired_fd_counts))*100

plt.figure(figsize=(15,10))
plt.plot(confired_fd_percent)
plt.plot(BENFORD)
plt.legend(['Covid worldwide','BENFORD'])
plt.show()


print(chi_square_test(confired_fd_percent,BENFORD))

# Since the chi_square test came out to be positive, 
# it means that the above dataset conforms with Benfords law for first digits. 



india_daily['State/UnionTerritory'].unique()

