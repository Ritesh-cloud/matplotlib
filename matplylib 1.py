#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['python', 'java', 'c', 'c++']
sizes = [35, 30, 25, 10]  # Percentages

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('language')

# Display the pie chart
plt.axis('equal') 
plt.show()


# In[ ]:




