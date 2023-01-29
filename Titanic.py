#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic.csv", sep= ",")

survived = df.loc[df['Survived']==1, :]['Pclass'].value_counts()
died     = df.loc[df['Survived']==0, :]['Pclass'].value_counts()
df_plot  = pd.DataFrame([survived,died])
df_plot.index=['survived','died']

df_plot.plot(kind='bar',stacked=True, title='Sobrevivientes y no sobrevivientes por clase')

