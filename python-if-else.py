#!/usr/bin/env python
# coding: utf-8

# In[30]:


c=22
d=25
if(c>d):
    print("c d'den büyüktür")
elif(c==d):
    print("c ile d eşittir")
elif(d>c):
    print("d c'den büyüktür")
else:
    print("hatalı giriş yapıldı")


# In[2]:


a=200
b=40
c=500


# In[31]:


if(a>b or a>c):
    print("a en az birinden büyüktür")
elif(a>b and a<c):
    print("a ortanca sayıdır")


# In[32]:


gecme_notu = 50
ogrenci1_notu = 60
if(gecme_notu<=ogrenci1_notu<=100):
    print("geçtiniz..")
elif(0<= ogrenci1_notu<gecme_notu):
    print("kaldınız..")
else:
    print("yanlış değer girdiniz..")


# In[8]:


ortalama=0
vize=40
final=70
ortalama=vize*0.4+final*0.6
print(ortalama)


# In[11]:


if(ortalama>=50):
    print("geçti")
elif(ortalama<50):
    print("kaldı")
else:
    print("hatalı giriş")


# In[12]:


x= float(input("vize notunuzu giriniz: "))


# In[13]:


type(x)


# In[23]:


ortalama=0
vize= float(input("vize notunuzu giriniz: "))
final= float(input("final notunuzu giriniz: "))
ortalama=vize*0.4+final*0.6
print(ortalama)


# In[34]:


if(0<=ortalama and ortalama<=40):
    print("ders notu: %.2f 'FF'"%(ortalama))
elif(40<ortalama and ortalama<50):
    print("DC")
elif(ortalama==50):
    print("CC")
elif(50<ortalama and ortalama<=70):
    print("BB")
elif(ortalama>70 and ortalama<=100):
    print("AA")
else:
    print("hatalı")


# In[ ]:




