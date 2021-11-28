import requests
from bs4 import BeautifulSoup
from array import *
import pylab

r = requests.get("https://rozetka.com.ua/ua/")
page = BeautifulSoup(r.text,'html.parser')
print(r.status_code)
ryad1 = page.head.title.text
ryad2 = page.body.text
letters_str = 'абвгґдеєжзиійїклмнопрстуфхцчшщьюя'
letters = list(letters_str)
frequency = []
l = len(letters)
for i in range(l):
     elem = letters[i]
     fr = ryad2.count(elem)
     frequency.append(fr)
xdata = letters
ydata = frequency

pylab.bar(xdata,ydata)
pylab.savefig('file1.png',dpi=200)
pylab.show()