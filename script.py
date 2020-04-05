# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# First, lets get started by importing the required libraries

# %%
import pandas as pd 
from matplotlib import pyplot as plt 

# %% [markdown]
# Assuming, we have the file on the same directory, lets import this file and see how the data looks like. We'll only print the first five entries.

# %%
file = pd.read_csv('Daily Summaries.csv')
print(file.head())

# %% [markdown]
# Now, lets take a look at the 2020 data.

# %%
data_2020 = file[file['Date']>='2020-01-01']
print(data_2020.head())

# %% [markdown]
# Now let's dive into two of the columns within the 2020 data. Move Minutes count and Distance.

# %%
distance = data_2020[['Distance (m)']]
distance['Date'] = pd.to_datetime(data_2020['Date'])
mov_min = data_2020[['Move Minutes count']]
mov_min['Date'] = pd.to_datetime(data_2020['Date'])
print(distance.head(),mov_min.head())

# %% [markdown]
# Lets plot the distance vs time graph

# %%
distance.plot(x='Date',y='Distance (m)')
plt.ylabel('Distance')
plt.show()

# %% [markdown]
# Lets get the average distance.

# %%
print("The mean distance is: "+ str(distance['Distance (m)'].mean())+" metres")

# %% [markdown]
# Similarly, lets have a look at Move minutes count.

# %%
mov_min.plot(x='Date',y='Move Minutes count')
plt.ylabel('Move Minutes')
plt.show()

# %% [markdown]
# Lets have a look at the average values

# %%
print("The mean Move Minutes value is: "+ str(mov_min['Move Minutes count'].mean())+" minutes")

