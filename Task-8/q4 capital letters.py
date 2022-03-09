import pandas as pd
import string
ser = pd.Series(['amrita' , 'school' , 'of' , 'enginnering' , 'chennai' , 'campus'])
str = " ".join(ser)
print(string.capwords(str))
