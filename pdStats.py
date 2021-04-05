import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import statistics
import scipy.stats 

x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

# # measures of central tendency
# mean 
# weighted mean 
# geometric mean 
# harmonic mean 
# median 
# mode 

# PANDAS:
pdavg = z.mean()
pd_nanavg = z_with_nan.mean()
print('Mean with pandas: \n', pdavg, pd_nanavg)

# NP WEIGHTED AVG
y, z, w = np.array(x), pd.Series(x), np.array(w)
# wmean = np.average(y, weights = w)
# print('Weighted mean of y with numpy: \n', wmean)

# wmean2 = np.average(z, weights = w)
# print('Weighted mean of Z with numpy: \n', wmean2)

# # HARMONIC MEAN w SCIPY
# harmonic_y = scipy.stats.hmean(y)
# harmonic_z = scipy.stats.hmean(z)
# print('Harmonic Means y, z with Scipy: \n', harmonic_y, harmonic_z)

# # MEDIAN WITH PANDAS
# zmed = z.median()
# print('Median of Z with pandas: \n', zmed)

# MODE WITH PANDAS
u = [2, 3, 2, 8, 12]
v = [12, 15, 12, 15, 21, 15, 12]
u, v, w = pd.Series(u), pd.Series(v), pd.Series([2, 2, math.nan])
# umode = u.mode()
# vmode = v.mode()
# wmode = w.mode()
# print('Modes of u, v, w with pandas: ', umode, vmode, wmode)

# MEASURES OF VARIABILITY

# VARIANCE
# STANDARD DEVIATION
# SKEWNESS
# PERCENTILES
# RANGES

# VARIANCE
zVariance = z.var(ddof=1)                     # for population variance instead of sample variance, use ddof=0 - that means delta degrees of freedom
znanVariance = z_with_nan.var(ddof=1)
print('Variance of z \n', zVariance, znanVariance)

# STD DEV
z_std = z.std(ddof=1)
# print(z_std)

# SKEW

zskew = z.skew()
print('Skewness of z: \n', zskew)

# describe

result = z.describe()
print(result)

# result['mean']
# 11.622222222222222
# result['std']
# 15.12454774346805
# result['min']
# -5.0
# result['max']
# 41.0
# result['25%']
# 0.1
# result['50%']
# 8.0
# result['75%']
# 21.0


# MEASURES OF CORRELATION BETWEEN PAIRS OF DATA

x = list(range(-10, 11))
y = [0, 2, 2, 2, 2, 3, 3, 6, 7, 4, 7, 6, 6, 9, 4, 5, 5, 10, 11, 12, 14]
x_, y_ = np.array(x), np.array(y)
x__, y__ = pd.Series(x_), pd.Series(y_)

# SAMPLE COVARIANCE
# # PURE PYTHON:
# n = len(x)
# mean_x, mean_y = sum(x) / n, sum(y) / n
# cov_xy = (sum((x[k] - mean_x) * (y[k] - mean_y) for k in range(n)) / (n - 1))

# NUMPY:  - OPTIONAL PARAMETERS BIAS=FALSE (DEFAULT) AND DDOF=NONE (DEFAULT)
cov_matrix = np.cov(x_, y_)
varX = x_.var(ddof=1)
varY = y_.var(ddof=1)
print(cov_matrix, varX, varY)   # non-diagonal values represent actual covariance between x,y

# PANDAS COVARIANCE

cov_xy = x__.cov(y__)
cov_yx = y__.cov(x__)

# CORRELATION COEFFICIENT
# PURE PYTHON
# var_x = sum((item - mean_x)**2 for item in x) / (n - 1)
# var_y = sum((item - mean_y)**2 for item in y) / (n - 1)
# std_x, std_y = var_x ** 0.5, var_y ** 0.5
# r = cov_xy / (std_x * std_y)

# SCIPY
# r, p = scipy.stats.pearsonr(x_, y_)
# result = scipy.stats.linregress(x_, y_)
# r = result.rvalue

# NUMPY
# corr_matrix = np.corrcoef(x_, y_)

# PANDAS
r = x__.corr(y__)
print('Correlation coefficient \n', r)  # You should call .corr() on one Series object and pass the other object as the first argument.


# OTHER SHIT

    # axis=None says to calculate the statistics across all data in the array. The examples above work like this. This behavior is often the default in NumPy.
    # axis=0 says to calculate the statistics across all rows, that is, for each column of the array. This behavior is often the default for SciPy statistical functions.
    # axis=1 says to calculate the statistics across all columns, that is, for each row of the array.

row_names = ['first', 'second', 'third', 'fourth', 'fifth']
col_names = ['A', 'B', 'C']
df = pd.DataFrame(a, index=row_names, columns=col_names)

df.mean()
df.var()
df.mean(axis=1)
df.var(axis=1)
df['A']
df['A'].mean()
df['A'].var()
df.values
df.to_numpy()
df.describe()
df.describe().at['mean', 'A']
df.describe().at['50%', 'B']

# VISUALIZING DATA 

np.random.seed(seed=0)
x = np.random.randn(1000)
y = np.random.randn(100)
z = np.random.randn(10)

fig, ax = plt.subplots()
ax.boxplot((x, y, z), vert=False, showmeans=True, meanline=True,
           labels=('x', 'y', 'z'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()

# HISTOGRAM

hist, bin_edges = np.histogram(x, bins=10)
bin_edges

fig, ax = plt.subplots()
ax.hist(x, bin_edges, cumulative=False)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')
plt.show()

fig, ax = plt.subplots()
ax.hist(x, bin_edges, cumulative=True)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')
plt.show()

# PIECHARTS

x, y, z = 128, 256, 1024

fig, ax = plt.subplots()
ax.pie((x, y, z), labels=('x', 'y', 'z'), autopct='%1.1f%%')
plt.show()

# BAR CHARTS

x = np.arange(21)
y = np.random.randint(21, size=21)
err = np.random.randn(21)

fig, ax = plt.subplots())
ax.bar(x, y, yerr=err)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# XY PLOTS

x = np.arange(21)
y = 5 + 2 * x + 2 * np.random.randn(21)
slope, intercept, r, *__ = scipy.stats.linregress(x, y)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Data points')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.show()

# HEATMAPS 
# COVARIANCE MATRIX:
matrix = np.cov(x, y).round(decimals=2)
fig, ax = plt.subplots()
ax.imshow(matrix)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, matrix[i, j], ha='center', va='center', color='w')
plt.show()

# CORRELATION COEFFICIENT MATRIX:
matrix = np.corrcoef(x, y).round(decimals=2)
fig, ax = plt.subplots()
ax.imshow(matrix)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, matrix[i, j], ha='center', va='center', color='w')
plt.show()
















# wmean = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w) 
