import sys
from pathlib import Path
import pandas as pd

file1=r'C:\Users\LENOVO\Desktop\Python_235\Azure.csv'
file2=r'C:\Users\LENOVO\Desktop\Python_235\Bot.csv'
files = [file1,file2]
with pd.ExcelWriter("default.xlsx") as writer:
    for csvfilename in files:
        p = Path(csvfilename)
        sheet_name = p.stem[:31]
        df = pd.read_csv(p)
        df.to_excel(writer, sheet_name=sheet_name)