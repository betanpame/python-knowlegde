# Statistical Analysis Fundamentals - Practice 5

**Difficulty:** ⭐ (Very Easy)

## Description

Learn basic statistical analysis techniques including descriptive statistics, correlation analysis, and hypothesis testing using Python's statistical libraries.

## Objectives

- Calculate descriptive statistics
- Perform correlation analysis
- Understand probability distributions
- Conduct basic hypothesis tests
- Interpret statistical results

## Your Tasks

1. **descriptive_statistics()** - Calculate mean, median, mode, std dev
2. **correlation_analysis()** - Find relationships between variables
3. **probability_distributions()** - Work with normal, binomial distributions
4. **hypothesis_testing()** - Perform t-tests and chi-square tests
5. **statistical_summaries()** - Generate comprehensive statistical reports

## Example

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import pearsonr, spearmanr, chi2_contingency
import matplotlib.pyplot as plt

def descriptive_statistics():
    """Calculate and interpret descriptive statistics."""
    
    # Generate sample data
    np.random.seed(42)
    data = {
        'Height': np.random.normal(170, 10, 100),  # cm
        'Weight': np.random.normal(70, 15, 100),   # kg
        'Age': np.random.randint(18, 65, 100),     # years
        'Income': np.random.lognormal(10, 0.5, 100) # log-normal distribution
    }
    df = pd.DataFrame(data)
    
    print("Sample Data (first 10 rows):")
    print(df.head(10))
    
    # Basic descriptive statistics
    print("\\nDescriptive Statistics:")
    print(df.describe())
    
    # Individual statistics
    for column in df.columns:
        print(f"\\n{column} Statistics:")
        print(f"  Mean: {df[column].mean():.2f}")
        print(f"  Median: {df[column].median():.2f}")
        print(f"  Mode: {df[column].mode().iloc[0]:.2f}")
        print(f"  Standard Deviation: {df[column].std():.2f}")
        print(f"  Variance: {df[column].var():.2f}")
        print(f"  Skewness: {stats.skew(df[column]):.2f}")
        print(f"  Kurtosis: {stats.kurtosis(df[column]):.2f}")
        print(f"  Range: {df[column].max() - df[column].min():.2f}")
        
        # Quartiles
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        print(f"  Q1 (25th percentile): {q1:.2f}")
        print(f"  Q3 (75th percentile): {q3:.2f}")
        print(f"  IQR: {iqr:.2f}")
    
    return df

def correlation_analysis():
    """Analyze correlations between variables."""
    
    # Generate correlated data
    np.random.seed(42)
    n = 100
    
    # Create variables with known relationships
    x1 = np.random.normal(0, 1, n)
    x2 = 0.8 * x1 + 0.6 * np.random.normal(0, 1, n)  # Strong positive correlation
    x3 = -0.5 * x1 + 0.87 * np.random.normal(0, 1, n)  # Moderate negative correlation
    x4 = np.random.normal(0, 1, n)  # No correlation with x1
    
    df = pd.DataFrame({
        'Variable_1': x1,
        'Variable_2': x2,
        'Variable_3': x3,
        'Variable_4': x4
    })
    
    print("Correlation Matrix:")
    correlation_matrix = df.corr()
    print(correlation_matrix)
    
    # Detailed correlation analysis
    print("\\nDetailed Correlation Analysis:")
    
    # Pearson correlation
    for i, col1 in enumerate(df.columns):
        for j, col2 in enumerate(df.columns):
            if i < j:  # Avoid duplicate pairs
                pearson_corr, pearson_p = pearsonr(df[col1], df[col2])
                spearman_corr, spearman_p = spearmanr(df[col1], df[col2])
                
                print(f"\\n{col1} vs {col2}:")
                print(f"  Pearson correlation: {pearson_corr:.4f} (p-value: {pearson_p:.4f})")
                print(f"  Spearman correlation: {spearman_corr:.4f} (p-value: {spearman_p:.4f})")
                
                # Interpret correlation strength
                abs_corr = abs(pearson_corr)
                if abs_corr >= 0.7:
                    strength = "Strong"
                elif abs_corr >= 0.5:
                    strength = "Moderate"
                elif abs_corr >= 0.3:
                    strength = "Weak"
                else:
                    strength = "Very weak"
                
                direction = "positive" if pearson_corr > 0 else "negative"
                print(f"  Interpretation: {strength} {direction} correlation")
    
    # Visualize correlation matrix
    plt.figure(figsize=(8, 6))
    plt.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar(label='Correlation Coefficient')
    plt.title('Correlation Matrix Heatmap')
    plt.xticks(range(len(df.columns)), df.columns, rotation=45)
    plt.yticks(range(len(df.columns)), df.columns)
    
    # Add correlation values to heatmap
    for i in range(len(df.columns)):
        for j in range(len(df.columns)):
            plt.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}', 
                    ha='center', va='center', color='black')
    
    plt.tight_layout()
    plt.show()
    
    return df, correlation_matrix

def probability_distributions():
    """Work with common probability distributions."""
    
    # Normal distribution
    print("Normal Distribution Analysis:")
    
    # Parameters
    mu, sigma = 100, 15
    
    # Generate data
    normal_data = np.random.normal(mu, sigma, 1000)
    
    print(f"Population parameters: μ = {mu}, σ = {sigma}")
    print(f"Sample statistics: mean = {np.mean(normal_data):.2f}, std = {np.std(normal_data):.2f}")
    
    # Calculate probabilities
    # P(X < 85)
    prob_less_85 = stats.norm.cdf(85, mu, sigma)
    print(f"P(X < 85) = {prob_less_85:.4f}")
    
    # P(X > 115)
    prob_greater_115 = 1 - stats.norm.cdf(115, mu, sigma)
    print(f"P(X > 115) = {prob_greater_115:.4f}")
    
    # P(85 < X < 115)
    prob_between = stats.norm.cdf(115, mu, sigma) - stats.norm.cdf(85, mu, sigma)
    print(f"P(85 < X < 115) = {prob_between:.4f}")
    
    # Critical values
    alpha = 0.05
    critical_value = stats.norm.ppf(1 - alpha/2, mu, sigma)
    print(f"95% confidence interval critical value: {critical_value:.2f}")
    
    # Binomial distribution
    print("\\nBinomial Distribution Analysis:")
    
    n_trials = 20
    p_success = 0.3
    
    # Calculate probabilities
    binomial_probs = [stats.binom.pmf(k, n_trials, p_success) for k in range(n_trials + 1)]
    
    print(f"Parameters: n = {n_trials}, p = {p_success}")
    print(f"Expected value: {n_trials * p_success:.2f}")
    print(f"Variance: {n_trials * p_success * (1 - p_success):.2f}")
    
    # P(X = 6)
    prob_exactly_6 = stats.binom.pmf(6, n_trials, p_success)
    print(f"P(X = 6) = {prob_exactly_6:.4f}")
    
    # P(X <= 5)
    prob_at_most_5 = stats.binom.cdf(5, n_trials, p_success)
    print(f"P(X <= 5) = {prob_at_most_5:.4f}")
    
    return normal_data, binomial_probs

def hypothesis_testing():
    """Perform basic hypothesis tests."""
    
    # One-sample t-test
    print("One-Sample T-Practice:")
    
    # Sample data - test if mean height is different from 170 cm
    np.random.seed(42)
    sample_heights = np.random.normal(172, 8, 30)
    
    hypothesized_mean = 170
    t_stat, p_value = stats.ttest_1samp(sample_heights, hypothesized_mean)
    
    print(f"Sample mean: {np.mean(sample_heights):.2f}")
    print(f"Hypothesized mean: {hypothesized_mean}")
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    alpha = 0.05
    if p_value < alpha:
        print(f"Reject null hypothesis (p < {alpha})")
        print("Sample mean is significantly different from hypothesized mean")
    else:
        print(f"Fail to reject null hypothesis (p >= {alpha})")
        print("No significant difference from hypothesized mean")
    
    # Two-sample t-test
    print("\\nTwo-Sample T-Practice:")
    
    # Compare heights between two groups
    group1 = np.random.normal(170, 8, 30)
    group2 = np.random.normal(175, 10, 35)
    
    t_stat2, p_value2 = stats.ttest_ind(group1, group2)
    
    print(f"Group 1 mean: {np.mean(group1):.2f}")
    print(f"Group 2 mean: {np.mean(group2):.2f}")
    print(f"T-statistic: {t_stat2:.4f}")
    print(f"P-value: {p_value2:.4f}")
    
    if p_value2 < alpha:
        print(f"Reject null hypothesis (p < {alpha})")
        print("Significant difference between group means")
    else:
        print(f"Fail to reject null hypothesis (p >= {alpha})")
        print("No significant difference between group means")
    
    # Chi-square test of independence
    print("\\nChi-Square Practice of Independence:")
    
    # Create contingency table
    observed = np.array([[20, 15, 10],
                        [25, 30, 20],
                        [15, 10, 25]])
    
    chi2_stat, chi2_p, dof, expected = chi2_contingency(observed)
    
    print("Observed frequencies:")
    print(observed)
    print("\\nExpected frequencies:")
    print(expected)
    print(f"\\nChi-square statistic: {chi2_stat:.4f}")
    print(f"P-value: {chi2_p:.4f}")
    print(f"Degrees of freedom: {dof}")
    
    if chi2_p < alpha:
        print(f"Reject null hypothesis (p < {alpha})")
        print("Variables are dependent")
    else:
        print(f"Fail to reject null hypothesis (p >= {alpha})")
        print("Variables are independent")
    
    return t_stat, p_value, t_stat2, p_value2, chi2_stat, chi2_p

def statistical_summaries():
    """Generate comprehensive statistical reports."""
    
    # Create sample dataset
    np.random.seed(42)
    n = 200
    
    data = {
        'Age': np.random.randint(18, 80, n),
        'Income': np.random.lognormal(10, 0.8, n),
        'Education_Years': np.random.normal(14, 3, n),
        'Job_Satisfaction': np.random.randint(1, 11, n),
        'Department': np.random.choice(['Sales', 'Engineering', 'Marketing', 'HR'], n)
    }
    
    df = pd.DataFrame(data)
    df['Education_Years'] = np.clip(df['Education_Years'], 8, 20)  # Realistic bounds
    
    print("Dataset Overview:")
    print(f"Shape: {df.shape}")
    print(f"\\nData types:\\n{df.dtypes}")
    print(f"\\nFirst 5 rows:\\n{df.head()}")
    
    # Numerical summary
    print("\\nNumerical Variables Summary:")
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    
    summary_stats = {}
    for col in numerical_cols:
        summary_stats[col] = {
            'count': df[col].count(),
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std': df[col].std(),
            'min': df[col].min(),
            'max': df[col].max(),
            'skewness': stats.skew(df[col]),
            'kurtosis': stats.kurtosis(df[col])
        }
    
    summary_df = pd.DataFrame(summary_stats).T
    print(summary_df.round(2))
    
    # Categorical summary
    print("\\nCategorical Variables Summary:")
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    for col in categorical_cols:
        print(f"\\n{col}:")
        value_counts = df[col].value_counts()
        percentages = df[col].value_counts(normalize=True) * 100
        
        summary_cat = pd.DataFrame({
            'Count': value_counts,
            'Percentage': percentages
        })
        print(summary_cat.round(2))
    
    # Correlation analysis for numerical variables
    print("\\nCorrelation Matrix for Numerical Variables:")
    corr_matrix = df[numerical_cols].corr()
    print(corr_matrix.round(3))
    
    # Group statistics
    print("\\nGroup Statistics by Department:")
    group_stats = df.groupby('Department')[numerical_cols].agg(['mean', 'std']).round(2)
    print(group_stats)
    
    return df, summary_stats, corr_matrix

# Practice all functions
if __name__ == "__main__":
    print("=== Statistical Analysis Fundamentals ===")
    
    print("\\n1. Descriptive Statistics:")
    desc_results = descriptive_statistics()
    
    print("\\n" + "="*60)
    print("2. Correlation Analysis:")
    corr_results = correlation_analysis()
    
    print("\\n" + "="*60)
    print("3. Probability Distributions:")
    prob_results = probability_distributions()
    
    print("\\n" + "="*60)
    print("4. Hypothesis Testing:")
    test_results = hypothesis_testing()
    
    print("\\n" + "="*60)
    print("5. Statistical Summaries:")
    summary_results = statistical_summaries()
    
    print("\\n=== Statistical Analysis Complete! ===")
```

## Hints

- Use `df.describe()` for quick descriptive statistics
- Use `scipy.stats` for advanced statistical functions
- Check p-values against significance level (typically 0.05)
- Consider both Pearson and Spearman correlations
- Always interpret statistical results in context

## Practice Cases

Your functions should:

- Calculate comprehensive descriptive statistics (mean, median, std, etc.)
- Compute correlation coefficients and interpret their strength
- Work with normal and binomial probability distributions
- Perform t-tests and chi-square tests with proper interpretation
- Generate detailed statistical summary reports

## Bonus Challenge

Create a function that performs automatic outlier detection and statistical profiling for any dataset!