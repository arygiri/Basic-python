#!/usr/bin/env python
# coding: utf-8

# # Ops Math

# In[1]:


s = 13
p = 2
mods = s % p
print(mods)


# In[2]:


m = 5
n = 3
expon = m**n
print(expon)


# In[3]:


z = 50
z -=30
print(z)


# In[4]:


z


# In[5]:


q = 20
q *= 10
print(q)


# In[6]:


c =20
c += 10
print(c)


# # Boolean

# In[7]:


s = 5
t = 2
hasil = s > t
hasil2 = s < t
print(hasil)
print(hasil2)


# # Ops math dengan tipe data yang berbeda 

# In[8]:


f = '3.7'
print(f)
print(f*2)


# In[9]:


g = 3.7
print(g)
print(g*2)


# # User input

# In[10]:


nama = input('Masukkan nama:')
print(nama)


# In[11]:


nama2 = input('Masukkan nama:')
print(nama2)


# In[12]:


nama


# In[13]:


nama2


# In[14]:


print(type(nama))
print(type(nama2))


# In[15]:


umur = input('Umur kamu:')
print(umur)


# In[16]:


print(type(umur))


# # String formatting/casting

# In[1]:


nama = input('Masukkan nama:')
print('nama kamu adalah'+' '+nama)


# In[2]:


umur = input('Umur kamu:')
print('umur kamu adalah'+ ' '+umur)


# In[3]:


umur = int(input('Umur kamu:'))
print('umur kamu adalah'+ ' '+umur)


# In[4]:


umur = int(input('Umur kamu:'))
print('umur kamu adalah'+ ' '+str(umur))


# In[5]:


umur = int(input('Umur kamu:'))
print('umur kamu adalah',umur)


# In[6]:


# Perbedaan antara opsi untuk string formatting


# In[7]:


nama2 = input ('Masukkan nama')
umur2 = input ('Masukkan umur')

text = 'Nama saya {}, dan saya berumur {} tahun'.format(nama2,umur2)
print(text)
text2 = 'Nama saya'+' '+nama2+' '+', dan saya berumur'+' '+umur2+' '+'tahun'
print(text2)
text3 = 'Nama saya',nama2,', dan saya berumur',umur2,'tahun'
print(text3)
print('Nama saya',nama2,', dan saya berumur',umur2,'tahun')


# # String Operation

# In[8]:


a = 'Hello Word'
print(a)


# In[9]:


print(a[0])


# In[10]:


print(a[4])


# In[11]:


print(a[1:])


# In[14]:


print(a[5:])


# In[15]:


print(a[1:5])


# In[16]:


print(a[:4])


# In[17]:


print(len(a))


# # Conditional If 

# In[18]:


a = 10
b = 15

if a > b:
    print('a lebih besar dari b')
elif a == b:
    print('a sama dengan b')
else:
    print('a lebih kecil dari b')


# In[19]:


c = 'Apel'
d = 'Jeruk'

if c != d:
    print('buah c berbeda dengan buah d')
else:
    print('buah c sama dengan buah d')


# In[20]:


print(not True)
print(not False)


# # List

# In[21]:


mylist = []
print (mylist)


# In[22]:


mylist = []
mylist.append (1)
mylist.append (2)
mylist.append (3)
mylist.append (100)
print(mylist)


# In[23]:


mylist =
mylist.append (1)
mylist.append (2)
mylist.append (3)
mylist.append (100)
print(mylist)


# In[24]:


print(len(mylist))


# In[25]:


mylist2 = []
mylist2.append('a')
mylist2.append('b')
print(mylist2)


# In[26]:


print(len(mylist2))


# In[27]:


print(mylist2[0])


# In[28]:


# for loop in list


# In[31]:


for b in mylist:
    print('Nilai:'+' '+str(b))


# In[32]:


for x in mylist2:
    print('Nilai:',x)


# In[33]:


print('Nilai:',mylist[0])
print('Nilai:',mylist[1])
print('Nilai:',mylist[2])
print('Nilai:',mylist[3])


# In[34]:


for z in range(1,11):
    print (z)


# # Pengayaan

# Buat program kalkulator sederhana dengan menu penjumlahan, pengurangan, perkalian, pembagian dengan menggunakan user input dan conditional if 

# In[37]:


operasi = input('Silahkan pilih menu= 1:Penjumlahan, 2:Pengurangan, 3:Perkalian, 4:Pembagian, 5:Keluar')

if operasi == '1':
    x = int(input('Masukkan angka ke-1:'))
    y = int(input('Masukkan angka ke-2'))
    print('Nilai {} + {}'.format(x,y),'=',x+y)
    print('==========================')
elif operasi == '2':
    x = int(input('Masukkan angka ke-1:'))
    y = int(input('Masukkan angka ke-2'))
    print('Nilai {} - {}'.format(x,y),'=',x-y)
    print('==========================')
elif operasi == '3':
    x = int(input('Masukkan angka ke-1:'))
    y = int(input('Masukkan angka ke-2'))
    print('Nilai {} x {}'.format(x,y),'=',x*y)
    print('==========================')
elif operasi == '4':
    x = int(input('Masukkan angka ke-1:'))
    y = int(input('Masukkan angka ke-2'))
    print('Nilai {} : {}'.format(x,y),'=',x/y)
    print('==========================')
elif operasi == '5':
    print('\nOke, terima kasih telah menggunakan kalkulator ini')
    print('==========================')
else:
    print('\nMaaf, pilihan menu angka tidak ada')
    print('==========================')


# In[ ]:




