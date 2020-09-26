import collections
from collections import Counter
import re
import sys
import os
import pandas as pd
import numpy as np
import string
import json
import string
import csv


pd.set_option('display.max_columns', 50)
df=pd.read_json('country_romance_lyrics.json')
df= df.replace(r'\\n',' ', regex=True) 

# print(df.head())

# print(df['Lyrics'].head())

lyrics=[]
for letras in df['Lyrics']:
    if letras !='':
        lyrics.append(letras)
    else:
        continue
# print(lyrics[0:30])


print(lyrics[0:30])

















