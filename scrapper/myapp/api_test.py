import json
import requests
from .models import Quotes

url = "https://type.fit/api/quotes"
resp = requests.get(url)
data = resp.json()

for i in range(-1,-6,-1):
    q = data[i]['text']
    a = data[i]['author']
    obj = Quotes(Quoation = q,Author = a) 
    obj.save()
