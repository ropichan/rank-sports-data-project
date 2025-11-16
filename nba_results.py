import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_excel('data/NBAResults20182019.xlsx')

print(df.head(20))

print(df.tail(20))