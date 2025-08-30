import pandas as pd
import numpy as np

grades = np.array([50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64])

study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

student_data = np.array([study_hours, grades])

df_students = pd.DataFrame({
    'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny', 'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
    'StudyHours': student_data[0],
    'Grade': student_data[1]
})

print(df_students.head())

print('Series')
print('Construction')
dict1 = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
dict1_keys = ['Texas', 'Oregon', 'Ohio', 'Utah', 'California']

# Some ways to create a Series.
series1 = pd.Series([4, 7, -5, 3])
series2 = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
series3 = pd.Series(dict1) # From a Python dict.
series4 = pd.Series(dict1, index=dict1_keys, name='population') # From a Python dict with keys in a specific order.
series4.index.name = 'state'
print(series1)
print(series2)
print(series3)
print(series4)

print('Some Operations')
print(series2[series2 > 0])
print('b' in series2)
print(series4.isna())


print('DataFrame')
print('Construction')
dict2 = {
    'state': ['Texas', 'Oregon', 'Ohio', 'Utah', 'California'],
    'year': [2000, 2001, 2002, 2001, 2003],
    'population': [35000, 71000, 16000, 5000, 5000],
}

df1 = pd.DataFrame(dict2)
print(df1)