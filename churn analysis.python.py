#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv(r"C:\Users\user\Downloads\Customer Churn.xls")


# In[6]:


df.info()


# In[108]:


df["TotalCharges"] = df["TotalCharges"].replace(" ","0")


# In[109]:


df["TotalCharges"] = df["TotalCharges"].astype("float")


# In[110]:


df.info()


# In[14]:


df.isnull().sum().sum()


# In[15]:


df.drop('Tota;Charges', axis=1, inplace=True)


# In[16]:


df.info()


# In[18]:


df.isnull().sum().sum()


# In[19]:


df.describe()


# In[22]:


df["customerID"].duplicated().sum()


# In[114]:


df.head(100)


# # convertion 0 and 1 into yes/no in column

# In[115]:


def conv(value):
    if value == 1:
        return "yes"
    else:
        return "no"
    
df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)


# In[65]:


ax = sns.countplot(x='Churn', data=df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Churn" , fontsize = 10)
plt.show()


# In[68]:


plt.figure(figsize = (3,4))
gb = df.groupby('Churn').agg({'Churn':'count'})
gb
plt.pie(gb['Churn'], labels = gb.index, autopct ="%1.2f%%")
plt.title("Percentage of Customers Churn" , fontsize = 10)
plt.show()


# #from the given pie chart we can conclude that 26.54% of customers have Churned out
# #now lets exolore reason behind it

# In[81]:


plt.figure(figsize = (4,4))
sns.countplot(x = 'gender' , data = df , hue = "Churn")
plt.title("Churn by Gender", fontsize= 10)
plt.show()


# In[143]:


plt.figure(figsize = (3,4))
ax = sns.countplot(x = 'SeniorCitizen' , data = df , hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Count of customers by SeniorCitizen", fontsize= 10)
plt.show()


# In[123]:


plt.figure(figsize = (9,4))
sns.histplot(x = "tenure" , data = df , bins = 72, hue = "Churn")
plt.show()


# # people who have used our services for a long time have stayed and people whoe have stayed one or two months have churned

# In[142]:


plt.figure(figsize = (4,4))
ax = sns.countplot(x = "Contract" , data = df , hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("count of customers by contract")
plt.show()


# # people who have month to month contract are likely to churned then from those who have one year or two year contract

# In[129]:


df.columns.values


# In[132]:


# Columns to create count plots for
columns_to_plot = [
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies'
]

# Create a figure with subplots
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))

# Flatten the axes array for easy iteration
axes = axes.flatten()

# Loop through the columns and the axes to create count plots
for i, column in enumerate(columns_to_plot):
    sns.countplot(x=column, data=df, ax=axes[i], hue = df["Churn"])
    axes[i].set_title(f'Count of {column}')
    axes[i].set_xlabel('')
    axes[i].set_ylabel('Count')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()


# # the majority of customers who do not churn tend to have services like phoneServices, internetServices(dsl), and onlinesecurity enabled for sevices like onlinebackup, techsupport , streamingtv churn rate are higher when these services are unused or are unavailable 

# In[147]:


plt.figure(figsize = (6,4))
ax = sns.countplot(x = "PaymentMethod" , data = df , hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("count of customers by PaymentMethod")
plt.xticks(rotation = 45)
plt.show()


# # customer is likely to churn when he is using electronic check as payment method

# In[ ]:




