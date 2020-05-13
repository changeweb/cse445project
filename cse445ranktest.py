import pandas as pd
import scipy.stats
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

CRED = '\033[91m'
CGREEN = '\33[32m'
CEND = '\033[0m'
CBOLD = '\33[1m'
CITALIC = '\33[3m'


sns.set(color_codes=True)
# Set up the matplotlib figure
f, axes = plt.subplots(2, 2, figsize=(7, 7))

# Read csv data
# Only load "commodity", "category","weight_kg","flow" columns
df = pd.read_csv (r'./global-commodity-trade-statistics/commodity_trade_statistics_data.csv', usecols=["commodity", "category","weight_kg","flow"], sep=',')

# Select "Fertilizers" from "category" ccolumn
fertilizers = df[df['category'] == "31_fertilizers"]

# Select "Urea" from "Fertilizers"
fertilizer1 = fertilizers[fertilizers['commodity'] == "Urea, including aqueous solution in packs >10 kg"]

# Select only "Imported" Urea
fertilizer1Import = fertilizer1[fertilizer1['flow'] == "Import"]

# Select "weight_kg" column for Imported Urea.
# Drop any missing rows
fertilizer1ImportWeight = fertilizer1Import['weight_kg'].dropna(how='any').reset_index(drop=True)

print("-----------------------------------------")
print(CITALIC + "-> At The End, Seaborn Plot Distribution Graph" + CEND)
print(CITALIC + "-> Please install \"Jupyter\" for better view" + CEND)
print("-----------------------------------------")
print(CBOLD + "Fertilizer1: " + CEND + "Urea")
print(CBOLD + "Fertilizer2: " + CEND + "Ammonium sulphate")
print("-----------------------------------------")
print(CBOLD + "\n---------- Test Imported Fertilizer weight for range between 0.0 to 1000000000.0 kg --------" + CEND)
# Print Minimum weight
print("Fertilizer1 Min: %.3f kg" % (np.min(fertilizer1ImportWeight)))
# Print Maximum weight
print("Fertilizer1 Max: %.3f kg" % (np.max(fertilizer1ImportWeight)))

# print(fertilizer1ImportWeight)

# Select "Ammonium sulphate" from "Fertilizers"
fertilizer2 = fertilizers[fertilizers['commodity'] == "Ammonium sulphate, in packs >10 kg"]

# Select only "Imported" Ammonium sulphate
fertilizer2Import = fertilizer2[fertilizer2['flow'] == "Import"]

# Select "weight_kg" column for Imported Ammonium sulphate.
# Drop any missing rows
fertilizer2ImportWeight = fertilizer2Import['weight_kg'].dropna(how='any').reset_index(drop=True)

# Print Minimum weight
print("Fertilizer2 Min: %.3f kg" % (np.min(fertilizer2ImportWeight)))
# Print Maximum weight
print("Fertilizer2 Max: %.3f kg" % (np.max(fertilizer2ImportWeight)))
print("-----------------------------------------")

# Print Distribution plot for Imported Urea 
# and Imported Ammonium sulphate
sns.distplot(fertilizer1ImportWeight, hist=False, ax=axes[0, 0])
sns.distplot(fertilizer2ImportWeight, hist=False, ax=axes[0, 0])

# Run Mann Whitney U Rank test
stat, p = mannwhitneyu(fertilizer1ImportWeight, fertilizer2ImportWeight)
print("-----------------------------------------")
print(CBOLD + "MANN WHITNEY U TEST" + CEND)
print("=========================================")
print("Let, H0: Same distribution")
print("-----------------------------------------")
print(CBOLD + "Output:" + CEND)
print("-----------------------------------------")
print('| Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print(CGREEN + '| -> Same distribution (fail to reject H0)' + CEND)
else:
	print(CRED + '| -> Different distribution (reject H0)' + CEND)
print("=========================================")


# Select Imported Urea of weight less than 100000.0 kg.
# Drop any missing rows
fertilizer1ImportWeight2 = fertilizer1Import[fertilizer1Import['weight_kg'] < 100000.0]['weight_kg'].dropna(how='any').reset_index(drop=True)

print(CBOLD + "\n---------- Now test Imported Fertilizer weight for range between 0.0 to 100000.0 kg --------" + CEND)
print("=========================================")

# Print Minimum weight
print("fertilizer1 Min: %.3f kg" % (np.min(fertilizer1ImportWeight2)))
# Print Maximum weight
print("fertilizer1 Max: %.3f kg" % (np.max(fertilizer1ImportWeight2)))

# Select Imported Ammonium sulphate of weight less than 100000.0 kg.
# Drop any missing rows
fertilizer2ImportWeight2 = fertilizer2Import[fertilizer2Import['weight_kg'] < 100000.0]['weight_kg'].dropna(how='any').reset_index(drop=True)

# print(fertilizer2ImportWeight2)

# Print Minimum weight
print("Fertilizer2 Min: %.3f kg" % (np.min(fertilizer2ImportWeight2)))
# Print Maximum weight
print("Fertilizer2 Max: %.3f kg" % (np.max(fertilizer2ImportWeight2)))
print("-----------------------------------------")

# Print Distribution plot for Imported Urea
# and Imported Ammonium sulphate less than 100000 kg
sns.distplot(fertilizer1ImportWeight2, hist=False, ax=axes[0, 1])
sns.distplot(fertilizer2ImportWeight2, hist=False, ax=axes[0, 1])

# Run Mann Whitney U Rank test
stat, p = mannwhitneyu(fertilizer1ImportWeight2, fertilizer2ImportWeight2)
print("-----------------------------------------")
print(CBOLD + "MANN WHITNEY U TEST" + CEND)
print("=========================================")
print("Let, H0: Same distribution")
print("-----------------------------------------")
print(CBOLD + "Output:" + CEND)
print("-----------------------------------------")
print('| Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print(CGREEN + '| -> Same distribution (fail to reject H0)' + CEND)
else:
	print(CRED + '| -> Different distribution (reject H0)' + CEND)
print("-----------------------------------------")
plt.show()