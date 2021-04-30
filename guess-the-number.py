import random
print('Добро пожаловать в числовую угадайку!')

# проверка корректности введенных данных
def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

ans = 'y'
# основной цикл программы
while ans == 'y':
  n = int(input("Введите число правой границы для случайного выбора числа: "))
  num = random.randint(1,n)
  sum = 1
  while True:
    num_user = (input("Какое число загадала угадайка?: "))
    if is_valid(num_user) == False:
      sum += 1
      print('А может быть все-таки введем целое число от 1 до 100?')
      continue

    num_user = int(num_user)
  
    if num_user < num:
      sum +=1
      print('Ваше число меньше загаданного, попробуйте еще разок')
    elif num_user > num:
      sum +=1
      print('Ваше число больше загаданного, попробуйте еще разок')
    else:
      print('Вы угадали, поздравляем!')
      print("Вы угадали за ", sum, 'попыток.')
      break
  print("Продолжим играть? (y/n): ")
  ans = input()
  
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')