informacion_personal ={
    'nombre' : 'Jordy Parion ',
    'edad' : 23,
    'ciudad' : 'El Chaco',
    'provincia':'Napo',
}
print('══════════════════════════')
print('       𝐌𝐢 𝐃𝐢𝐜𝐜𝐢𝐨𝐧𝐚𝐫𝐢𝐨')
print('══════════════════════════')
for clave, valor in informacion_personal.items():
    print(f'{clave}:{valor}')

# Clave "ciudad" y modificarlo con una cuidad diferente.
informacion_personal['ciudad']= 'El Chaco'
informacion_personal['provincia']= 'Napo'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'Ingeniero futbolista '

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0991446579'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('edad')
print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave}:{valor}')