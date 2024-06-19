tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

tel['jack']

del tel['sape']
tel['irv'] = 4127
print(tel)

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel