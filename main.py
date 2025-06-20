import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

#Question 1
import pandas as pd


df = pd.read_csv('MD_agric_exam-4483.csv')
unique_crops = df['Crop_type'].nunique()
print(f"Number of unique crop types: {unique_crops}")

#Question 2
df = pd.read_csv('MD_agric_exam-4483.csv')
max_yield = df[df['Crop_type'] == 'wheat']['Annual_yield'].max()

print(f"Maximum annual yield for wheat: {round(max_yield, 2)}")

#Question 3
avg_pollution = df.groupby('Crop_type')['Pollution_level'].mean()
high_pollution_crops = avg_pollution[avg_pollution > 0.2].index

total_rainfall = df[df['Crop_type'].isin(high_pollution_crops)]['Rainfall'].sum()
print(f"Total rainfall for crop types with avg pollution > 0.2: {total_rainfall}")

#Question 4
df = pd.read_csv('MD_agric_exam-4483.csv')

def temperature_range(field_id):
    row = df[df['Field_ID'] == field_id]
    if row.empty:
        return None
    max_temp = row['Max_temperature_C'].values[0]
    min_temp = row['Min_temperature_C'].values[0]
    return max_temp - min_temp

ids = [1458, 1895, 5443]
results = {fid: temperature_range(fid) for fid in ids}

print(results)

#Question 5
# Identified the crop with the lowest Average minimum Temperature

#Question 6
df = pd.read_csv('MD_agric_exam-4483.csv')
# Filter for plots with pH less than 5.5 and sum their plot sizes
total_plot_size = df[df['pH'] < 5.5]['Plot_size'].sum()
print(f"Total plot size for plots with pH < 5.5: {total_plot_size}")

#Question 7
df = pd.read_csv('MD_agric_exam-4483.csv')
filtered_df = df[(df['Min_temperature_C'] < -5) & (df['Max_temperature_C'] > 30)]
num_rows = len(filtered_df)
print(f"Number of rows in the filtered dataset: {num_rows}")

#Question 8
df = pd.read_csv('MD_agric_exam-4483.csv')
median_plot_size = df['Plot_size'].median()
large_plots = df[df['Plot_size'] > median_plot_size]
rainfall_std = np.std(large_plots['Rainfall'], ddof=0)
print(f"Standard deviation of Rainfall (rounded): {round(rainfall_std, 2)}")

#Question 9

df = pd.read_csv('MD_agric_exam-4483.csv')
most_common_max_temp = df['Max_temperature_C'].mode()[0]
first_three_digits = str(most_common_max_temp).replace('.', '')[:3]
crop_counts = df['Crop_type'].value_counts(ascending=True)
least_common_crop = crop_counts.index[0]
last_three_letters = least_common_crop[-3:]
result = first_three_digits + last_three_letters
print(f"Resulting string: {result}")

#There is an error in this code , cant find the issue.

#Question 10
df = pd.read_csv('MD_agric_exam-4483.csv')
def elevation_category(elev):
    if elev < 300:
        return 'Low'
    elif elev <= 600:
        return 'Medium'
    else:
        return 'High'

df['Elevation_Category'] = df['Elevation'].apply(elevation_category)
plt.figure(figsize=(8, 6))
sns.violinplot(x='Elevation_Category', y='Annual_yield', data=df, order=['Low', 'Medium', 'High'])
plt.title('Distribution of Annual Yield Across Elevation Categories')
plt.xlabel('Elevation Category')
plt.ylabel('Annual Yield')
plt.show()

#Question 11
df = pd.read_csv('MD_agric_exam-4483.csv')
unique_crops = df['Crop_type'].unique()

def recursive_sum(crops):
    if len(crops) == 0:
        return 0
    return len(crops[0]) + recursive_sum(crops[1:])

total = recursive_sum(list(unique_crops))
print(f"Sum of integer values for each unique crop type: {total}")

#Total is 6 + 6 + 5 + 7 + 5 +3


#Question 12
df = pd.read_csv('MD_agric_exam-4483.csv')
coffee_yield = df[df['Crop_type'] == 'coffee']['Annual_yield']
banana_yield = df[df['Crop_type'] == 'banana']['Annual_yield']
t_stat, p_value = ttest_ind(coffee_yield, banana_yield, equal_var=False)
print(f"P-value: {round(p_value, 3)}")

# https://github.com/Trishalin05/PythonExam.git


