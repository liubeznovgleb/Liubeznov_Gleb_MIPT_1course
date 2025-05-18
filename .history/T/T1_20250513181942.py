import scipy.stats as stats

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
if __name__ == "__main__":
    sample1 = [12.1, 13.5, 14.2, 15.3, 16.1]
    sample2 = [11.8, 12.9, 13.7, 14.8, 15.6]
    p_value = calculate_p_value(sample1, sample2)
    print(f"P-value: {p_value}")