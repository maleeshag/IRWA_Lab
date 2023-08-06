#!/usr/bin/env python
# coding: utf-8

# In[1]:


teams=["India","England","NZ","Aus"]
captain=["Kholi","Root","Williaamson","Smith"]


# In[2]:


teams


# In[4]:


captain


# In[5]:


concat=zip(teams,captain)


# In[6]:


concat


# In[7]:


print(list(concat))


# In[ ]:





# In[8]:


answer2 = {i:j for i, j in zip(teams,captain) }


# In[9]:


print(answer2)


# In[ ]:





# In[ ]:





# In[10]:


books= ["textbooks", "exercise books", "story book", "drawing books"]
prices = [100,60,90,70]
quantities = [3,2,1,4]


# In[11]:


for a,b,c  in zip(books,prices,quantities):
    print(f"You bought {c} {a} for $ {c*b}")


# In[ ]:





# In[ ]:





# In[12]:


answer2


# In[13]:


answer2.items()


# In[14]:


answer2


# In[15]:


answer3=dict([value,key] for key,value in answer2.items())
answer3


# In[ ]:





# In[18]:


List1 = [2,4,6,8,10]
List2={i+10 for i in List1}
List2


# In[ ]:





# In[19]:


list1 = [10, 20, 30, 40]
list2 = ["Apples", "Mangoes", "Oranges", "Grapes"]


# In[20]:


list1


# In[21]:


list2


# In[22]:


list2.reverse()


# In[23]:


list2


# In[24]:


for a,b in zip(list1,list2):
    print(f"{a} {b}")


# In[ ]:





# In[ ]:





# In[ ]:


#incomplete


# In[25]:


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


#Q 6


# In[27]:


List1= [10,15,20,15,32,54,15]


# In[28]:


answer6=[]
for i in List1:
    if i==15:
        continue
    else:
        answer6.append(i)
       


# In[29]:


answer6


# In[ ]:





# In[30]:


#Q 07


# In[31]:


dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
dict_2 = {'Bonnie': 18,'Rick': 20,'Matt': 16}


# In[32]:


dict_1.update(dict_2)


# In[33]:


dict_1


# In[ ]:





# In[34]:


#Q 08


# In[35]:


d = {0: 0, 1: 1, 2: 2, 3: 3}


# In[36]:


k_old = 0
k_new = 4
d[k_new] = d.pop(k_old)
print(d)


# In[ ]:





# In[ ]:





# In[37]:


#Q 09


# In[38]:


country=["USA","France","India"]


# In[39]:


capital= ["Washington D.C.","Paris","New Delhi"]


# In[40]:


answer9={country[i]:capital[i] for i in range(len(country))}


# In[41]:


answer9


# In[ ]:





# In[ ]:





# In[42]:


# Q 10


# In[43]:


My_dict = {"Fruit": "Pear",
"Vegetable": "Carrot",
"Pet": "Cat",
"Book": "Moby dick",
"Crystal": "Amethyst"}
keysToRemove = ["Book", "Crystal"]


# In[46]:


for i in keysToRemove:
    My_dict.pop(i)


# In[47]:


My_dict


# In[ ]:





# In[ ]:





# In[48]:


# Q 11


# In[49]:


sub_dict = {'math' : 100, 'chem' : 98, 'sci' : 100,'eng':100}
key_to_extract = {'math', 'chem','sci'}


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[50]:


#Q 12


# In[51]:


list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]


# In[52]:


answer12=[]
for i in list1:
    if i%5==0:
        answer12.append(i)
    else:
        continue


# In[53]:


answer12


# In[ ]:





# In[ ]:





# In[54]:


# Q 13


# In[55]:


numbers = [12, 75, 150, 180, 145, 525, 50]


# In[56]:


answer13=[]
for i in numbers:
        if i>150:
            continue;
        elif i>500:
            break;
        else:
            if 
            answer13=numbers.append(i)
            


# In[ ]:




