import pandas as pd
import numpy as np

data = pd.DataFrame(pd.read_excel('onco_data1_2.xlsx',sheet_name='datos_onco1'))
subset = data[['RECORD_ID']]

np.savetxt(r'datos.txt', subset.values, fmt='%s')