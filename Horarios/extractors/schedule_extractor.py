import sys
import pandas as pd

cols = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# leo el archivo 'dicisHORARIOS.csv', no tiene header, quiero
# las columnas [5,6,7,8,9,10], el separador es ','
df = pd.read_csv(sys.argv[1], header=None, usecols=[
                 5, 6, 7, 8, 9, 10], sep=',', names=cols)
# remuevo los renglones que tengan nombres similares. dejando solo el primero
df = df.drop_duplicates(keep='first')
# remuevo los renglones que tengan el mismo UDA. dejando solo el primero
# df = df.drop_duplicates(subset=['Keycode'], keep='first')
# Guardo el la tabla en un archivo, sin indices.
df = df.sort_values(by=['Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday'])
df.to_csv(sys.argv[2], sep=',', index=False)

# df.to_csv('s.csv', sep=',', index=False)
