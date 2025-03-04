import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import textwrap

# Brand Surveys
heard_of_brand = pd.DataFrame({
    'Brand': ['Airbnb', 'Crowne Plaza', 'Hilton', 'Holiday Inn', 'Ibis', 'Mercure', 'Premier Inn', 'Travelodge'],
    'Dec-16': [52, 63, 93, 95, 80, 47, 97, 95],
    'Dec-17': [66, 63, 94, 93, 79, 51, 96, 95],
    'Dec-18': [78, 63, 94, 93, 81, 54, 95, 92]
})


remember_seeing_ad = pd.DataFrame({
    'Brand': ['Airbnb', 'Crowne Plaza', 'Hilton', 'Holiday Inn', 'Ibis', 'Mercure', 'Premier Inn', 'Travelodge'],
    'Dec-16': [14, 4, 10, 13, 10, 4, 36, 27],
    'Dec-17': [18, 4, 11, 10, 8, 4, 32, 20],
    'Dec-18': [22, 5, 16, 15, 11, 5, 26, 23]
})

stayed_past_12_months = pd.DataFrame({
    'Brand': ['Airbnb', 'Crowne Plaza', 'Hilton', 'Holiday Inn', 'Ibis', 'Mercure', 'Premier Inn', 'Travelodge'],
    'Dec-16': [9, 7, 21, 20, 18, 9, 45, 36],
    'Dec-17': [12, 8, 19, 25, 14, 8, 43, 37],
    'Dec-18': [21, 10, 22, 25, 18, 10, 48, 38]
})


would_seriously_consider = pd.DataFrame({
    'Brand': ['Airbnb', 'Crowne Plaza', 'Hilton', 'Holiday Inn', 'Ibis', 'Mercure', 'Premier Inn', 'Travelodge'],
    'Dec-16': [11, 18, 34, 41, 29, 14, 63, 49],
    'Dec-17': [15, 15, 31, 39, 29, 17, 60, 47],
    'Dec-18': [21, 15, 32, 36, 28, 14, 61, 48]
})


most_preferred_choice = pd.DataFrame({
    'Brand': ['Airbnb', 'Crowne Plaza', 'Hilton', 'Holiday Inn', 'Ibis', 'Mercure', 'Premier Inn', 'Travelodge'],
    'Dec-16': [3, 1, 11, 4, 4, 2, 25, 9],
    'Dec-17': [4, 2, 8, 7, 3, 2, 26, 10],
    'Dec-18': [6, 2, 8, 3, 2, 1, 21, 11]
})


# Brand surveys

# Heatmap for brand awareness
plt.figure(figsize=(12, 10))
sns.heatmap(heard_of_brand.drop('Brand', axis=1).set_index(heard_of_brand['Brand']), annot=True, cmap="inferno", cbar_kws={'label': 'Percentage (%)'})
plt.title("Brand Awareness Heatmap (2016-2018)", fontsize=18)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Brand", fontsize=14)
plt.yticks(rotation=0)
plt.show()

years = ['Dec-16', 'Dec-17', 'Dec-18']
airbnb_ad_recall = remember_seeing_ad[remember_seeing_ad['Brand'] == 'Airbnb'][years].values.flatten()
airbnb_stay = stayed_past_12_months[stayed_past_12_months['Brand'] == 'Airbnb'][years].values.flatten()
airbnb_consider = would_seriously_consider[would_seriously_consider['Brand'] == 'Airbnb'][years].values.flatten()

# Ad Recall, Consideration, and Stayed Over Time
plt.figure(figsize=(10, 6))
plt.plot(years, airbnb_ad_recall, marker='o', linestyle='-', color='blue', label="Ad Recall")
plt.plot(years, airbnb_consider, marker='o', linestyle='-', color='green', label="Serious Consideration")
plt.plot(years, airbnb_stay, marker='o', linestyle='-', color='red', label="Stayed Past 12 Months")

plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.title("Airbnb Ad Recall, Consideration, and Stayed Over Time")
plt.grid(True)
plt.legend()
plt.show()

# Stayed in Past 12 Months
plt.figure(figsize=(12, 7))
bar_width = 0.2
x = range(len(stayed_past_12_months))
colors = ['#2C6A9A', '#9b59b6', '#f39c12']

plt.bar([i - bar_width for i in x], stayed_past_12_months['Dec-16'], width=bar_width, label='Dec-16', color=colors[0])
plt.bar(x, stayed_past_12_months['Dec-17'], width=bar_width, label='Dec-17', color=colors[1])
plt.bar([i + bar_width for i in x], stayed_past_12_months['Dec-18'], width=bar_width, label='Dec-18', color=colors[2])
plt.xlabel('Brand', fontsize=14, fontweight='bold', color='#333')
plt.ylabel('Percentage (%)', fontsize=14, fontweight='bold', color='#333')
plt.title('Percentage of People Who Stayed in Each Brand in the Past 12 Months (2016-2018)', fontsize=16, fontweight='bold', color='#333')
plt.xticks(x, stayed_past_12_months['Brand'], rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title="Year", title_fontsize=13, loc='upper left', fontsize=12)
plt.tight_layout()
plt.show()

# Most Preferred brands Pie charts
fig, axes = plt.subplots(1, 3, figsize=(18, 8))

years = ['Dec-16', 'Dec-17', 'Dec-18']
for i, year in enumerate(years):
    preferences = most_preferred_choice[year]
    axes[i].pie(preferences, labels=most_preferred_choice['Brand'], autopct='%1.1f%%', startangle=90, 
                colors=sns.color_palette("Set3", len(most_preferred_choice)))
    axes[i].set_title(f'Most Preferred Brands in {year}')

plt.tight_layout()
plt.show()

# TGI 1: Used_past_12_months
age = pd.DataFrame({
    'Age Group': ['15-24', '25-34', '35-44', '45-54', '55-64', '65+'],
    'Mercure': [8, 16, 11, 23, 14, 27],
    'Ibis': [16, 23, 14, 16, 13, 19],
    'Crowne Plaza': [11, 20, 17, 18, 14, 20],
    'Travelodge': [12, 17, 17, 20, 17, 18],
    'Hilton': [14, 20, 19, 18, 12, 17],
    'Holiday Inn': [9, 22, 19, 19, 13, 20],
    'Premier Inn': [11, 15, 16, 21, 15, 22],
    'Airbnb': [23, 32, 17, 12, 8, 8]
})

gender= pd.DataFrame({
    'Gender': ['Female', 'Male'],
    'Mercure': [50, 50],
    'Ibis': [51, 49],
    'Crowne Plaza': [54, 46],
    'Travelodge': [53, 47],
    'Hilton': [47, 53],
    'Holiday Inn': [48, 52],
    'Premier Inn': [52, 48],
    'Airbnb': [50, 50]
})

sns.set_style("darkgrid")
age_melted = age.melt(id_vars=['Age Group'], var_name='Brand', value_name='Percentage')
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", 
    "#9467bd", "#17becf", "#f5a623", "#4b0082"
]


# Usage by Age Group
plt.figure(figsize=(12, 6))
sns.barplot(x='Age Group', y='Percentage', hue='Brand', data=age_melted, palette=colors)
plt.title('Usage by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Percentage')
plt.legend(title='Brand', bbox_to_anchor=(1, 1), loc='upper left')
plt.tight_layout()
plt.show()

gender_melted = gender.melt(id_vars=['Gender'], var_name='Brand', value_name='Percentage')
brands = gender.columns[1:]
female_data = gender.loc[0, brands]
male_data = gender.loc[1, brands]
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Female Pie Chart
wedges, texts, autotexts = axes[0].pie(female_data, labels=brands, 
                                       autopct=lambda p: f'{p:.1f}%\n({int(p * sum(female_data) / 100)})', 
                                       colors=colors, startangle=90, 
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 0.5})
axes[0].set_title('Brand Usage Among Females', color='black', fontsize=16, weight='bold')

for i, label in enumerate(texts):
    label.set_color(colors[i])
for autotext in autotexts:
    autotext.set_color('white')

# Male Pie Chart
wedges, texts, autotexts = axes[1].pie(male_data, labels=brands, 
                                       autopct=lambda p: f'{p:.1f}%\n({int(p * sum(male_data) / 100)})', 
                                       colors=colors, startangle=90, 
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 0.5})
axes[1].set_title('Brand Usage Among Males', color='black', fontsize=16, weight='bold')

for ax in axes:
    for label in ax.texts:
        label.set_fontsize(10)
        label.set_fontweight('bold')
for i, label in enumerate(texts):
    label.set_color(colors[i])
for autotext in autotexts:
    autotext.set_color('white')

plt.show()



# TGI 2: Sentiments
consumer_behavior = pd.DataFrame({
    'Statement': [
        'I look for the lowest possible prices when shopping',
        'Own label products are equal quality to big brand products',
        'Convenience often plays a part in my purchase decisions',
        'I will pay more for products that make life easier',
        'I tend to go for premium rather than standard options',
        "It's worth paying extra for quality goods",
        'I buy new products before most of my friends',
        'It is important that a company acts ethically'
    ],
    'Mercure': [48, 52, 50, 52, 32, 77, 23, 74],
    'Ibis': [59, 56, 53, 47, 25, 68, 21, 75],
    'Crowne Plaza': [50, 58, 56, 59, 31, 74, 31, 68],
    'Travelodge': [60, 60, 56, 45, 20, 62, 16, 72],
    'Hilton': [51, 50, 58, 57, 37, 73, 31, 73],
    'Holiday Inn': [51, 52, 58, 49, 29, 71, 27, 70],
    'Premier Inn': [54, 59, 54, 44, 22, 64, 15, 72],
    'Airbnb': [61, 56, 66, 57, 26, 76, 20, 84]
})

# Consumer behavior data heatmap
consumer_melted = consumer_behavior.melt(id_vars=['Statement'], var_name='Brand', value_name='Percentage')

consumer_pivot = consumer_melted.pivot(index='Statement', columns='Brand', values='Percentage')
consumer_pivot.index = [textwrap.fill(label, width=20) for label in consumer_pivot.index]

plt.figure(figsize=(12, 8), facecolor='#f0f0f0')
sns.heatmap(consumer_pivot, annot=True, cmap='inferno', fmt='.1f')
plt.title('Consumer Behavior Across Brands')
plt.xlabel('Brand')
plt.ylabel('Statement')
plt.xticks(rotation=45)
plt.show()