import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
book_url = 'http://www.gutenberg.org/ebooks/42671.txt.utf-8'

with urllib.request.urlopen(book_url) as f:
    Pride_and_Prejudice_book_text = f.read().decode('utf-8')


chapters=Pride_and_Prejudice_book_text.split('CHAPTER')
chapters=chapters[1:]

pride_df=pd.DataFrame(chapters,columns=['chapters'])
print(pride_df)
