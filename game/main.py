print('¡Vamos a jugar Piedra, Papel o Tijera contra Python!')
juego = input('Crees poder vencer a Python?')
juego = juego.lower()
if juego == 'si':
  print('¡Eso es! Vas confiado, genial.')
else:
  print('Vamos es el juego de toda la vida')

import random

options = ('piedra', 'papel', 'tijera')

Python_wins = 0
User_wins = 0
rounds = 1

while True:
  print('*'*10)
  print('RONDA', rounds)
  print('*'*10)
  
  user_option = input('Elije piedra, papel o tijera => ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('Esa opción no es válida')
    continue 
  
  computer_option = random.choice(options)
  
  print('Tu opción => ', user_option)
  print('Opción de Python => ', computer_option)
  
  
  if user_option == computer_option:
    print('¡Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
     print('piedra gana a tijera')
     print('¡Ganaste!')
     User_wins +=1
    else:
      print('papel le gana a piedra')
      print('Python te ganó')
      Python_wins +=1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('¡Ganaste!')
      User_wins +=1
    else: 
      print('tijera gana a papel')
      print('Python te ganó')
      Python_wins +=1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('¡Ganaste!')
      User_wins +=1
    else:
      print('piedra gana a tijera')
      print('Python te ganó')
      Python_wins +=1

  print('Tus victorias => ', User_wins)
  print('Victorias de Python', Python_wins)

  if Python_wins == 2:
    print('Perdiste el juego, Python es mejor que tú')
    break

  if User_wins == 2:
    print('Ganaste, venciste a Python')
    break

  rounds +=1