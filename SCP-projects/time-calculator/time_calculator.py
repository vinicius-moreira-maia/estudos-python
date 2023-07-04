def day_of_the_week(n, weekday):
  days = {
    'Sunday' : 1,
    'Monday' : 2,
    'Tuesday' : 3,
    'Wednesday' : 4,
    'Thursday' : 5,
    'Friday' : 6,
    'Saturday' : 7
  }

  wd_number = days.get(weekday)

  while True:
    wd_number += 1
    n -= 1

    if wd_number > 7:
      wd_number = 1

    if n == 0:
      break

  for day in days:
    if days[day] == wd_number:
      return day


def add_time(start, duration, weekday = ''):
  n = 0

  # extraindo as informações das strings
  horario, sigla = start.split()
  hora, min = horario.split(":")
  hora = int(hora)
  min = int(min)
  h_add, min_add = duration.split(':')
  h_add = int(h_add)
  min_add = int(min_add)

  # convertendo para o formato de 24 horas
  if sigla == 'AM' and hora == 12:
    hora -= 12
  if sigla == 'PM' and hora in range(1, 12):
    hora += 12

  while True:
    # incrementando o tempo
    if min_add:
      min += 1
      min_add -= 1
    if h_add:
      hora += 1
      h_add -= 1

    # + 1 hora a cada 60 minutos
    if min > 59:
      hora += 1
      min = 0

    # se não houver mais o que incrementar, sair do loop
    if min_add <= 0 and h_add <= 0:
      break

  # dividindo a quantidade de horas total por 24 para saber quantos dias se passaram
  n = hora // 24

  if n and weekday:
     weekday = day_of_the_week(n, weekday.capitalize())

  # diminuindo de 24 em 24 até a hora ser válida (no formato de 24h)
  if hora > 24:
    while True:
      hora -= 24
      if hora < 24:
        break

  # convertendo para o formato de 12 horas
  if hora == 0:
    hora += 12
    sigla = 'AM'
  elif hora in range(1, 12):
    sigla = 'AM'
  elif hora == 12:
    sigla = 'PM'
  elif hora in range(13, 24):
    hora -= 12
    sigla = 'PM'

  # exibição correta dos minutos para caso seja um número de apenas 1 dígito
  if min < 10:
    min = '0' + str(min)

  if weekday and not n:
    return f"{hora}:{min} {sigla}, {weekday.capitalize()}"
  elif n and not weekday:
    if n == 1:
      return f"{hora}:{min} {sigla} (next day)"
    else:
      return f"{hora}:{min} {sigla} ({n} days later)"
  elif n and weekday:
    if n == 1:
      return f"{hora}:{min} {sigla}, {weekday.capitalize()} (next day)"
    else:
      return f"{hora}:{min} {sigla}, {weekday.capitalize()} ({n} days later)"
  else:
    return f"{hora}:{min} {sigla}"