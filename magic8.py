
import random

question = input('Question: ')

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Muy dudoso'
elif random_number == 2:
  answer = 'Mejor no te lo digo ahora' 
elif random_number == 3:
  answer = 'Respuesta incorrecta, intetalo de nuevo'
elif random_number == 4:
  answer = 'Sin duda'
elif random_number == 5:
  answer = 'Mis recursos dicen que no'
elif random_number == 6:
  answer = 'Es definitivamente si'
elif random_number == 7:
  answer = 'Pregunta mas tarde'
elif random_number == 8:
  answer = 'Perspectiva no tan buena'
elif random_number == 9:
  answer = 'Si-definitivamente'
else:
  answer = 'Error'
  
print('Question:      ' + question)
print('Magic 8 Ball:  ' + answer)