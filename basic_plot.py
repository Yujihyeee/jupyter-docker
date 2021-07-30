#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


def plot_show():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40])
    plt.show()


# In[4]:


plot_show()


# In[5]:


def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()


# In[6]:


plot_two_list_show()


# In[7]:


def plot_three_list_show():
    plt.title("legend")
    plt.plot([10, 20, 30, 40], color = "purple", label = "asc")
    plt.plot([40, 30, 20, 10], color = "black", label = "desc")
    plt.legend()
    plt.show()


# In[8]:


plot_three_list_show()


# In[9]:


def plot_color():
    plt.title("color")
    plt.plot([10, 20, 30, 40], color = "skyblue", label = "skyblue")
    plt.plot([40, 30, 20, 10], color = "pink", label = "pink")
    plt.legend()
    plt.show()


# In[10]:


plot_color()


# In[11]:


def plot_linestyle():
    plt.title("linestyle")
    plt.plot([10, 20, 30, 40], color="r", linestyle = "--", label = "dashed")
    plt.plot([40, 30, 20, 10], color="g", ls =":", label = "dotted")
    plt.legend()
    plt.show()


# In[12]:


plot_linestyle()


# In[13]:


def plot_scatter():
    plt.title("marker")
    plt.plot([10, 20, 30, 40], "r.", label = "circle")
    plt.plot([40, 30, 20, 10], "g^", label = "triangle up")
    plt.legend()
    plt.show()


# In[14]:


plot_scatter()


# In[ ]:




