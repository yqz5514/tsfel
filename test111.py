

# %%
import tsfel
import pandas as pd

#%%
# load dataset
df = pd.read_csv('MSFT.csv')


# %%
df.dtypes
# %%
df.head()
#%%
df.dtypes
#%%
df['Date'] = df['Date'].astype(pd.StringDtype())
df.dtypes

#%%
df['Date'] = df['Date'].str.replace('-', '').astype(float)
df.head()

#%%
df.dtypes
# %%
df.columns
#%%
# Retrieves a pre-defined feature configuration file to extract all available features
cfg = tsfel.get_features_by_domain()

# Extract features
X = tsfel.time_series_features_extractor(cfg, df)
# %%
pd.set_option('display.max_columns', None)
# %%
X
# %%
X.columns
# %%
print(X. columns)
# %%
