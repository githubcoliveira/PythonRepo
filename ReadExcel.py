#import os
import pandas as pd



"""
cwd = os.getcwd()
files = os.listdir(cwd)
print("files in %r: %s" %  (cwd, files))
"""


file = "C:/Users/mailc/Documents/Temp/PTOD072023.xls"
sheet = "PTOD072023"


df = pd.read_excel(file, sheet_name=sheet) 

df = df.drop(range(0,3))


#df = df.sort_values

print(df)

