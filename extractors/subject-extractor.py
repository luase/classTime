import pandas

colnames = ['Keycode', 'Name', 'Hours At Week', 'Prerequisite', 'Group',
'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
'Classroom', 'Teacher', 'President', 'Assistant']

df = pandas.read_csv('dicisHORARIO_2018_2sem_SLAD.csv',
            index_col='Name',
            header=0,
            names=colnames)

cols_to_keep = ['Keycode', 'Hours At Week']
df[cols_to_keep].to_csv('Subjects.csv', sep=',')
#df.to_csv('test.csv', sep='\t', header=None, mode='a') #agregar mas filas a un archivo
# NOTE:                              ----->  ^^^^^^^^   
