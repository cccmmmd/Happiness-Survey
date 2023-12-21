#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[3]:


# df = pd.read_csv('Happiness_Survey_students_Goldsmiths.csv', usecols= range(1,15))
df = pd.read_csv('Happiness_Survey_students_Goldsmiths.csv')
df = df.dropna().drop('時間戳記', axis=1)

df.head().append(df.tail())


# In[20]:


ax1 = df[df['My gender is…'] == 'Female']['I agree that people in my life care about me.'].value_counts()
ax2 = df[df['My gender is…'] == 'Male']['I agree that people in my life care about me.'].value_counts()
ax3 = df[df['My gender is…'] == 'Prefer not to say']['I agree that people in my life care about me.'].value_counts()
dfa = pd.concat([ax1,ax2,ax3],axis=1).fillna(0)
dfa.columns = ['Female', 'Male', 'Prefer not to say']

fig, axs = plt.subplots(1,3, figsize=(20, 10))
axs[0].pie(
        ax1,
        labels=['Strongly agree', 'Agree', 'Neither agree or disagree', 'Disagree'],
        autopct='%1.1f%%',
        startangle=270,
        radius=1,
        counterclock=False)
axs[0].set_title('Female')
axs[1].pie(
        ax2,
        labels=['Strongly agree', 'Agree', 'Neither agree or disagree'],
        autopct='%1.1f%%',
        startangle=270,
        radius=1,
        counterclock=False)
axs[1].set_title('Male')
axs[2].pie(
        ax3,
        labels=['Strongly agree'],
        autopct='%1.1f%%',
        startangle=270,
        radius=1,
        counterclock=False)
axs[2].set_title('Prefer not to say')
fig.suptitle("I agree that people in my life care about me.",y=0.8);

plt.show()


# In[5]:


ax1 = df[df['My gender is…'] == 'Female']['I agree that people in my life care about me.'].value_counts()
ax2 = df[df['My gender is…'] == 'Male']['I agree that people in my life care about me.'].value_counts()
ax3 = df[df['My gender is…'] == 'Prefer not to say']['I agree that people in my life care about me.'].value_counts()
dfa = pd.concat([ax1,ax2,ax3],axis=1).fillna(0)
dfa.columns = ['Female', 'Male', 'Prefer not to say']
dfa = dfa.transpose()
print(dfa)

fig, ax = plt.subplots(figsize=(10,7))
ax = dfa.plot.bar(rot=20,  ax=ax)
ax.set_xlabel('I agree that people in my life care about me.')
ax.set_ylabel('number of people')
ax.legend(fontsize = 12)

plt.show()


# In[6]:


ax1 = df[df['The department where I am studying is '] == 'A/Computing']['How would I rate my study-life balance?'].value_counts(normalize=True).round(3)
ax2 = df[df['The department where I am studying is '] == 'A/Media, Communications and Cultural Studies']['How would I rate my study-life balance?'].value_counts(normalize=True).round(3)
ax3 = df[df['The department where I am studying is '] == 'A/Institute of Creative and Cultural Entrepreneurship']['How would I rate my study-life balance?'].value_counts(normalize=True).round(3)
ax4 = df[df['The department where I am studying is '] == 'A/Art']['How would I rate my study-life balance?'].value_counts(normalize=True).round(3)
ax5 = df[df['The department where I am studying is '] == 'A/Stacs']['How would I rate my study-life balance?'].value_counts(normalize=True).round(3)
dfa = pd.concat([ax1,ax2,ax3,ax4,ax5],axis=1).fillna(0)
dfa.columns = ['A/Computing', 'A/Media', 'A/Institute of CCE', 'A/Art', 'A/Stacs']

dfa = dfa.transpose()

fig, ax = plt.subplots(figsize=(10,7))
dfa.plot.barh(stacked=True, rot=0, ax=ax)
ax.invert_yaxis()
fig.suptitle("How would I rate my study-life balance?",y=0.95);
ax.set_xlabel('Percentage of people')
ax.set_ylabel('Student departments')
ax.legend(bbox_to_anchor=(1,1), fontsize = 12)
plt.show()


# In[7]:


ax1 = df[df['My gender is…'] == 'Female']['I have enough money to buy things I want.'].value_counts(normalize=True)
ax2 = df[df['My gender is…'] == 'Male']['I have enough money to buy things I want.'].value_counts(normalize=True)
ax3 = df[df['My gender is…'] == 'Prefer not to say']['I have enough money to buy things I want.'].value_counts(normalize=True)
dfa = pd.concat([ax1,ax2,ax3],axis=1).fillna(0)
dfa.columns = ['Female', 'Male', 'Prefer not to say']
dfa = dfa.transpose()

fig, ax = plt.subplots(figsize=(10,7))
dfa.plot.barh(stacked=True, rot=0, ax=ax)
ax.invert_yaxis()
fig.suptitle("I have enough money to buy things I want.",y=0.95);
ax.set_xlabel('Percentage of people')
ax.set_ylabel('Genders')
ax.legend(bbox_to_anchor=(1,1), fontsize = 12)
plt.show()


# In[8]:


ax1 = df[df['My gender is…'] == 'Female']['How often do I share my feelings with friends or relatives?'].value_counts(normalize=True)
ax2 = df[df['My gender is…'] == 'Male']['How often do I share my feelings with friends or relatives?'].value_counts(normalize=True)
ax3 = df[df['My gender is…'] == 'Prefer not to say']['How often do I share my feelings with friends or relatives?'].value_counts(normalize=True)
dfa = pd.concat([ax1,ax2,ax3],axis=1).fillna(0)
dfa.columns = ['Female', 'Male', 'Prefer not to say']
dfa = dfa.transpose()

fig, ax = plt.subplots(figsize=(10,7))
dfa.plot.barh(stacked=True, rot=0, ax=ax)
ax.invert_yaxis()
fig.suptitle("How often do I share my feelings with friends or relatives?",y=0.95);
ax.set_xlabel('Percentage of people')
ax.set_ylabel('Genders')
ax.legend(bbox_to_anchor=(1,1), fontsize = 12)
plt.show()


# In[9]:


dfs = df['My friends make me feel happy.'].value_counts()
print(dfs)
ax = dfs.plot.barh()
ax.invert_yaxis()
ax.set_xlabel('people number')
ax.set_ylabel('answer')
ax.set_xlim(0,20)
ax.set_title('My friends make me feel happy.')


# In[10]:


dfs = df['In general, how much stress do I have with my personal finances?'].value_counts(normalize=True).round(3)
print(dfs)
ax = dfs.plot.pie(
        autopct='%1.1f%%',
        startangle=270,
        counterclock=False,
        label='',
        title='In general, how much stress do I have with my personal finances?',
        subplots=True)


# In[11]:


dfs = df['I am satisfied with my ability to perform activities of daily living.'].value_counts(normalize=True).round(3)
print(dfs)
ax = dfs.plot.pie(
        autopct='%1.1f%%',
        startangle=270,
        counterclock=False,
        label='',
        title='I am satisfied with my ability to perform activities of daily living.',
        subplots=True)


# In[12]:


dfs = df['I think the school provides good teaching systems.'].value_counts(normalize=True).round(3)
print(dfs)
ax = dfs.plot.pie(
        autopct='%1.1f%%',
        startangle=270,
        counterclock=False,
        label='',
        title='I think the school provides good teaching systems.',
        subplots=True)


# In[13]:


dfs = df['No matter what life throws at me, I believe that I can deal with it.'].value_counts(normalize=True).round(3)
print(dfs)
ax = dfs.plot.pie(
        autopct='%1.1f%%',
        startangle=270,
        counterclock=False,
        label='',
        title='No matter what life throws at me, I believe that I can deal with it.',
        subplots=True)


# In[14]:


dfs = df['How would I rate my study-life balance?'].value_counts(normalize=True).round(3)
print(dfs)
ax = dfs.plot.pie(
        autopct='%1.1f%%',
        startangle=270,
        counterclock=False,
        label='',
        title='How would I rate my study-life balance?',
        subplots=True)


# In[15]:


dfs = df['How much time do I feel hopeful about my future in my study/programme?'].value_counts(normalize=True).round(3)
print(dfs)
ax = dfs.plot.pie(
        autopct='%1.1f%%',
        startangle=270,
        counterclock=False,
        label='',
        title='How much time do I feel hopeful about my future in my study/programme?',
        subplots=True)


# In[16]:


dfs = df['My friends make me feel happy.'].value_counts(normalize=True).round(3)
print(dfs)
ax = dfs.plot.pie(
        autopct='%1.1f%%',
        startangle=270,
        counterclock=False,
        label='',
        title='My friends make me feel happy.',
        subplots=True)


# In[17]:


dfs = df['How much of the time have I felt lonely during the past week?'].value_counts(normalize=True).round(3)
print(dfs)
ax = dfs.plot.pie(
        autopct='%1.1f%%',
        startangle=270,
        counterclock=False,
        label='',
        title='How much of the time have I felt lonely during the past week?',
        subplots=True)


# In[ ]:




