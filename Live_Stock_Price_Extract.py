#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Introdction to the yahoo_fin package

# The ***yahoo_fin*** package has two modules below.
#  > stock_info
#  
#  > options. 
#  
# ## stock_info 
# stock_info has the below primary methods.
# > get_analysts_info
# 
# > get_balance_sheet
# 
# > get_cash_flow
# 
# > get_data
# 
# > get_day_gainers
# 
# > get_day_losers
# 
# > get_day_most_active
# 
# > get_holders
# 
# > get_income_statement
# 
# > get_live_price
# 
# > get_quote_table
# 
# > get_top_crypto
# 
# > get_stats
# 
# > get_stats_valuation
# 
# > tickers_dow
# 
# > tickers_nasdaq
# 
# > tickers_other
# 
# > tickers_sp500
# 
# ## options
# options are listed below
# 
# > get_calls
# 
# > get_expiration_dates
# 
# > get_options_chain
# 
# > get_puts

# # Installation

# In[4]:


# ignore the warnimng
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


# ## yahoo_fin

# In[1]:


get_ipython().system('pip install yahoo_fin')


# ## Its Dependencies

# In[5]:


get_ipython().system('pip install requests_html')


# # Collecting real-time data from Yahoo Finance for stocks

# In[15]:


import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')

def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1


# In[ ]:


size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.random.randn(len(x_vec))
line1 = []
while True:
    rand_val = np.random.randn(1)
    y_vec[-1] = rand_val
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)
    plot(x_vec,y1_data,'-o',alpha=0.8) 


# In[ ]:





# ## Stock prices

# In[8]:


from yahoo_fin import stock_info as si
# get live price of Apple
si.get_live_price("aapl")


# In[13]:


apple=si.get_live_price("aapl")
print(apple)


# In[19]:


import matplotlib.pyplot as plt
apple=[]
while True:
    #apple=si.get_live_price("aapl")
    apple.append(si.get_live_price("aapl"))
    #print(apple)
    plt.plot(apple,'-o',alpha=0.8) 
    plt.show


# In[10]:


# or Amazon
si.get_live_price("amzn")


# ## cryptocurrency prices

# In[11]:


si.get_top_crypto()


# In[ ]:




