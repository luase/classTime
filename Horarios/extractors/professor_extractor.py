import sys
import pandas as pd

cols = ['Name']
# leo el archivo 'dicisHORARIO_2018_2sem_SLAD.csv', no tiene header, quiero
# las columnas [0,1,2], el separador es ','
df = pd.read_csv(sys.argv[1], header=None, usecols=[12], sep=',', names=cols)
# remuevo los renglones que tengan nombres similares. dejando solo el primero
df = df.drop_duplicates(subset=['Name'], keep='first')
# remuevo los renglones que tengan el mismo UDA. dejando solo el primero
# df = df.drop_duplicates(subset=['Keycode'], keep='first')
# Guardo el la tabla en un archivo, sin indices.
df = df.sort_values(by=['Name'])
df.to_csv(sys.argv[2], sep=',', index=False)
