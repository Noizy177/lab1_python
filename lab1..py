#!/usr/bin/env python
# coding: utf-8

# In[67]:


#задание 11
def frange(start, finish, step):
    x = start
    if step > 0:
        while x < finish:
            yield round(x,2)
            x = x + step
    else:
        while x > finish:
            yield round(x,2)
            x = x + step

for x in frange(1,5,0.1):
    print(x)


# In[37]:


#задание 1
try:
    num = float(input("Введите число: "))

    if num < 0:
        raise ValueError

    rub = int(num)
    kop = int(round((num - rub) * 100))

    print(rub, "руб.", kop, "коп.")

except:
    print("Некорректный формат!")


# In[36]:


#задание 2
a = [1, 2, 3, 5, 6]

x = True

for i in range(len(a) - 1):
    if a[i] >= a[i + 1]:
        x = False

print(x)


# In[38]:


#задание 3
card = input("Введите номер карты: ")

res = card[:4] + " **** **** " + card[-4:]

print(res)


# In[40]:


#задание 4
text = input("Введите текст: ")

words = text.split()

big = []
mid = []
small = []

for w in words:
    if len(w) > 7:
        big.append(w)
    elif len(w) >= 4:
        mid.append(w)
    else:
        small.append(w)

for w in big:
    print(w)

for w in mid:
    print(w)

for w in small:
    print(w)


# In[44]:


#задание 5
text = input("Введите текст: ")

words = text.split()

result = []

for w in words:
    if w[0].isupper():
        result.append(w.upper())
    else:
        result.append(w)

print(" ".join(result))


# In[45]:


#задание 6
text = input("Введите текст: ")

for x in text:
    if text.count(x) == 1:
        print(x)


# In[51]:


#задание 7
urls = ["www.google", "www.yandex.ru", "mail.con"]

new_urls = [
    ("http://" + u if u.startswith("www") else u) +
    ("" if u.endswith(".com") else ".com")
    for u in urls
]

print(new_urls)


# In[54]:


#задание 8
import random

n = random.randint(1, 10000)

a = []

for i in range(n):
    a.append(random.randint(0, 100))

size = 1
while size < n:
    size = size * 2

while len(a) < size:
    a.append(0)

print(len(a))


# In[55]:


#заданеи 9
money = {
    1000: 10,
    100: 10,
    50: 10,
    10: 10
}

s = int(input("Введите сумму: "))

res = []

for k in sorted(money.keys(), reverse=True):
    count = s // k
    if count > 0:
        res.append(str(count) + "*" + str(k))
        s = s - count * k

if s != 0:
    print("Операция не может быть выполнена!")
else:
    print(" + ".join(res))


# In[58]:


#задание 10
p = input("Введите пароль: ")

if len(p) < 6:
    print("Слабый пароль")
elif any(c.isdigit() for c in p) and any(c.isalpha() for c in p):
    print("Нормальный пароль")
else:
    print("Средний пароль")


# In[59]:


#задание 12
def get_frames(signal, size, overlap):
    step = int(size * (1 - overlap))

    i = 0

    while i + size <= len(signal):
        yield signal[i:i + size]
        i = i + step


signal = [1,2,3,4,5,6,7,8,9,10]

for frame in get_frames(signal, 4, 0.5):
    print(frame)


# In[61]:


#задание 13
def extra_enumerate(x):
    total = sum(x)
    cum = 0

    for i in x:
        cum = cum + i
        frac = cum / total
        yield i, cum, frac


x = [1,3,4,2]

for elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)


# In[62]:


#задание 14
def non_empty(func):

    def wrapper():
        res = func()

        new = []

        for i in res:
            if i != "" and i is not None:
                new.append(i)

        return new

    return wrapper


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

print(get_pages())


# In[64]:


#задание 15
def pre_process(a=0.97):

    def decorator(func):

        def wrapper(s):
            for i in range(1, len(s)):
                s[i] = s[i] - a * s[i - 1]

            func(s)

        return wrapper

    return decorator


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)


plot_signal([1,2,3,4,5])


# In[65]:


#задание 16
import random
import itertools
from datetime import datetime, timedelta

teams = [
"A","B","C","D",
"E","F","G","H",
"I","J","K","L",
"M","N","O","P"
]

random.shuffle(teams)

groups = [teams[i:i+4] for i in range(0,16,4)]

for i,g in enumerate(groups):
    print("Group",i+1,g)

date = datetime(datetime.now().year,9,14,22,45)

for g in groups:
    games = list(itertools.combinations(g,2))

    for game in games:
        print(date.strftime("%d/%m/%Y, %H:%M"), game)
        date = date + timedelta(days=14)


# In[ ]:




