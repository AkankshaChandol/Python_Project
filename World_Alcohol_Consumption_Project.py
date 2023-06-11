#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


#Load alcohol world alcohol datase
df = pd.read_csv("C:/Users/Lenovo/Downloads/world_alcohol_comsumption.csv")


# In[4]:


df


# In[5]:


#1

df[(df.Year == 1987) | (df.Year == 1989)]


# In[7]:


#2
res = df[df['Year'] == 1987].where(( df['WHO region'] =='Western Pacific')
           & (df['Country'] == 'Viet Nam'))
res


# In[25]:


#2
res = df[df['Year'] == 1987].where(( df['WHO region'] =='Western Pacific')
           & (df['Country'] == 'Viet Nam'))
res = res.dropna() # to drop NAN value
res


# In[11]:


#2
import matplotlib.pyplot as plt
plt.bar ('Beverage Types', 'Display Value', data = res1, label = '1987', color ='Blue')
plt.show()


# In[9]:


#2
import matplotlib.pyplot as plt
plt.barh ('Beverage Types', 'Display Value', data = res1, label = '1987', color ='Orange')#barh means horizontal graph
plt.xlabel('ALCOHOL CONSUMPTION')
plt.ylabel('WESTERN PACIFIC - VIET NAM')
plt.show()


# In[10]:


#2
import matplotlib.pyplot as plt
plt.bar ('Beverage Types', 'Display Value', data = res1, label = '1987', color ='Orange')#barh means horizontal graph
plt.xlabel('ALCOHOL CONSUMPTION')
plt.ylabel('WESTERN PACIFIC - VIET NAM')
plt.show()


# In[12]:


df


# In[31]:


res = df[(df['Year'] == 1986) | (df['Year'] == 1989)].where ((df['WHO region'] == 'Americas') | (df['WHO region'] == 'Europe'))
res = res.dropna()

res1
# In[32]:


res

res
# In[33]:


res2 = res[res['Year']==1989]


# In[34]:


res2


# In[30]:


res


# In[38]:


res1 = res[res['Year'] == 1986]
res1


# In[41]:


#Display bar charts for 1986
import matplotlib.pyplot as plt
plt.bar('WHO region','Display Value', data =res1, labeL = '1986', color  = 'Blue')
plt.xlabel('WHO region')
plt.ylabel('ALCOHOL CONSUMPTION')
plt.legend()
plt.show()


# In[42]:


#Display bar charts for 1986
import matplotlib.pyplot as plt
plt.bar('WHO region','Display Value', data =res1, labeL = '1989', color  = 'Cyan')
plt.xlabel('WHO region')
plt.ylabel('ALCOHOL CONSUMPTION')
plt.legend()
plt.show()


# In[45]:


#4
res = df[(df['Year']==1986) | (df['Year']==1989). where ((df['WHO region'] == 'Americas') | (df['WHO region'] == 'Europe'))][['WHO region','Country','Beverage Types']]


# In[46]:


res


# In[50]:


#5
res  = df[(df['Display Value'] >=5) & (df['Beverage Types'] == 'Beer')]
res


# In[62]:


#6
res1 = df[(df['Display Value']>=4) & (df['Beverage Types']=='Beer')]['Display Value'] #to dispaly a particular column you can write this in [] and for more than 1 column we can write in list like[[]]
res2 = df[(df['Display Value']>=4) & (df['Beverage Types']=='Wine')]['Display Value']
res3 = df[(df['Display Value']>=4) & (df['Beverage Types']=='Spirits')]['Display Value']
print(res1,res2,res3)


# 

# In[64]:


plt.pie(res1, shadow = True, autopct = '%.1f%%')#autopct means automatically calculate percentage
plt.show()
plt.pie(res2, shadow =True, autopct  ='%.1f%%')
plt.show()
plt.pie(res3, shadow = True, autopct = '%.1f%%')
plt.show()


# In[71]:


#7
res= df.loc[0:15, ['WHO region','Beverage Types']]
res
#same can be written using iloc
#res=df.iloc[0:16, [1,3]]
#res


# In[75]:


#8
res = df['WHO region']
res1  = res.str.contains('Ea')
len(df[res1])
#n = len(res1)
#n
#But the output is showing true as well as false records we want only true recoords
#so use len(df[res1])


# In[77]:


#9
# renaming the colum
df1  = df.rename(columns ={'WHO region':'WHO_region'})
df1.query("WHO_region in ['Africa','Eastern Mediterranean','Europe']")#in query we can give only one woed column name if we use WHO region it will take as two columns


# In[107]:


#10
df1.query('WHO_region not in["Africa","Eastern Mediterranean","Europe"]')


# In[90]:


#12
res1 = df[(df['Beverage Types']=='Wine') & (df['Display Value']>2)]
res1


# In[100]:


#13
lst = list(range(0,100,10))
rows = df.iloc[lst, :]
rows


# In[ ]:





# In[102]:


#14
lst = list(range(0, 10))
rows = df.loc[lst, ['Year', 'Country']]


# In[105]:


#17
df.isnull().sum()


# In[108]:


df.dropna(inplace=True)
df


# In[109]:


len(df.columns)


# In[ ]:




