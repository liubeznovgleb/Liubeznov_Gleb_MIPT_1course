import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def calculate_p_value(sample1, sample2):
    """
    Calculate the p-value for two samples with normal distribution and unknown variances.
    Uses Welch's t-test.

    Parameters:
    sample1 (list or array-like): First sample data
    sample2 (list or array-like): Second sample data

    Returns:
    float: p-value
    """
    t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)
    return p_value

# Example usage
sample1 = np.read_csv('16511391_6#table-01.csv')
sample2 = np.read_csv('16511391_4#table-02.csv')

df_1 = sample1['age']
df_2 = sample2['age']

plt.plot(sample1, label='Sample 1', marker='o')
plt.plot(sample2, label='Sample 2', marker='o')
plt.show()

p_value = calculate_p_value(sample1, sample2)
print(f"P-value: {p_value}")