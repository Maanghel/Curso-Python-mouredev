"""
1. Crea una variable con la fecha y hora actual.

2. Imprime solo el año, mes y día de la fecha actual.

3. Crea una fecha específica: 25 de diciembre de 2025 y
    muéstrala.

4. Muestra solo la hora, los minutos y los segundos de un
    objeto time.

5. Calcula cuántos días faltan para el 1 de enero del año
    siguiente.

6. Crea una función que reciba una fecha y devuelva su
    timestamp.

7. Suma 30 días a la fecha actual usando timedelta.

8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30
    días como simplificación).

9. Compara dos fechas y muestra cuál es anterior.

10. Crea una lista con varias fechas y ordénalas
    cronológicamente.
"""

from datetime import datetime, timedelta, date, time

now = datetime.now() # Crea una variable con la fecha y hora actual
print(now) # Imprime la fecha y hora actual

# print(now.year, now.month, now.day) Imprime solo el año, mes y día de la fecha actual
print(f"\n{now.strftime("%Y-%m-%d")}") # Imprime solo el año, mes y día de la fecha actual formateado

specific_date = datetime(2025, 12, 25) # Crea una fecha específica: 25 de diciembre
print(f"\n{specific_date.strftime("%Y-%m-%d")}") # Muestra la fecha específica formateada

time_obj = time(14, 35, 50)
# print(time_obj.hour, time_obj.minute, time_obj.second) Muestra solo la hora, los minutos y los segundos de un objeto time
print(f"\n{time_obj.strftime("%H:%M:%S")}") # Muestra solo la hora, los minutos y los segundos de un objeto time formateado

today = date.today() # Obtiene la fecha actual
next_year = date(today.year + 1, 1, 1) # Crea una fecha para el 1 de enero del año siguiente
diff = next_year - today # Calcula la diferencia entre las dos fechas
print(f"\nFaltan {diff.days} días para el 1 de enero del año siguiente.") # Muestra cuántos días faltan para el 1 de enero del año siguiente

def get_timestamp(date_obj): # Crea una función que reciba una fecha y devuelva su timestamp
    return date_obj.timestamp() # Devuelve el timestamp de la fecha

next_date = datetime.now() + timedelta(days= 30) # Suma 30 días a la fecha actual usando timedelta
print(f"\n{next_date.strftime("%Y-%m-%d")}") # Muestra la fecha actual + 30 días formateada

init_date = datetime(2023, 1, 1) # Crea una fecha inicial
next_month = init_date + timedelta(days= 30) # Añade 1 mes (30 días) a la fecha inicial
print(f"\n{next_month.strftime("%Y-%m-%d")}") # Muestra la fecha inicial + 1 mes formateada

first_date = datetime(2023, 1, 1) # Crea una fecha inicial
second_date = datetime(2024, 1, 1) # Crea una segunda fecha
if first_date < second_date: # Compara las dos fechas
    print(f"\n{first_date.strftime("%Y-%m-%d")} es anterior a {second_date.strftime("%Y-%m-%d")}") # Muestra cuál es anterior
else:
    print(f"\n{second_date.strftime("%Y-%m-%d")} es anterior a {first_date.strftime("%Y-%m-%d")}") # Muestra cuál es anterior

dates_list = [
    datetime(2023, 5, 1),
    datetime(2022, 12, 25),
    datetime(2024, 1, 1),
    datetime(2023, 7, 4)
]
sorted_list = sorted(dates_list) # Ordena la lista de fechas cronológicamente
print("\nFechas ordenadas cronológicamente:")
for d in sorted_list:
    print(d.strftime("%Y-%m-%d")) # Muestra las fechas ordenadas cronológicamente formateadas