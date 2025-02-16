#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_excel('articles.xlsx')


# In[3]:


data.info()


# In[6]:


data.groupby(['source_id'])['article_id'].count()


# In[7]:


data.groupby(['source_id'])['engagement_reaction_count'].sum()


# In[8]:


data = data.drop('engagement_comment_plugin_count',axis=1)


# In[9]:


def keyword_flag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keyword_flag('murder')


# In[10]:


data['title'][15]


# In[11]:


data['keyword_flag'] = pd.Series(keywordflag)


# In[12]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[13]:


sent_int = SentimentIntensityAnalyzer()


# In[14]:


text = data['title'][16]
sent = sent_int.polarity_scores(text)


# In[16]:


neg = sent['neg']
pos = sent['pos']
neu = sent['neu']


# In[17]:


title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)


# In[20]:


for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg =0
        pos =0
        neu =0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)


# In[21]:


data['title_neg_sentiment']=pd.Series(title_neg_sentiment)
data['title_pos_sentiment']=pd.Series(title_pos_sentiment)
data['title_neu_sentiment']=pd.Series(title_neu_sentiment)


# In[22]:


data.to_excel('blogme_clean.xlsx',sheet_name='blogmedata')


# In[ ]:




