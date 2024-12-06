message = "Привіт, це моє перше повідомлення!"
print(message)
message = "А це вже нове повідомлення."
print(message)

user_name = "Vladislav"
print(f"Hello, {user_name}, would you like to learn some Python today?")

famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

user_name = "  \tВладислав\n  "
print(f"Ім'я з пропусками: '{user_name}'")
print(f"Без пропусків зліва: '{user_name.lstrip()}'")
print(f"Без пропусків справа: '{user_name.rstrip()}'")
print(f"Без пропусків з обох боків: '{user_name.strip()}'")

print("Владислав Корбут")
print("Україна")
print("03142")
print("Місто Київ")
print("Вулиця Доброхотова, 15")

def convert_distance(meters):
    inches = meters * 39.3701  # 1 метр = 39.3701 дюймів
    feet = meters * 3.28084    # 1 метр = 3.28084 футів
    miles = meters * 0.000621371  # 1 метр = 0.000621371 миль
    yards = meters * 1.09361    # 1 метр = 1.09361 ярда

    print(f"{meters} м = {format(inches, '.2f')} дюймів")
    print(f"{meters} м = {format(feet, '.2f')} футів")
    print(f"{meters} м = {format(miles, '.2f')} миль")
    print(f"{meters} м = {format(yards, '.2f')} ярдів")

distance_in_meters = float(input("Введіть відстань в метрах: "))

convert_distance(distance_in_meters)



def calculate_duration(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(f"Тривалість у годинах: {format(hours, '<10d')}")
    print(f"Тривалість у хвилинах: {format(minutes, '<10d')}")
    print(f"Тривалість у секундах: {format(seconds, '<10d')}")

days = int(input("Введіть кількість днів: "))

calculate_duration(days)



def convert_temperature(celsius):
    fahrenheit = 32 + (9/5) * celsius
    kelvin = celsius + 273.15

    print(f"{'Температура в Цельсії:':<15}{format(celsius, '^15.2f')}")
    print(f"{'Температура у Фаренгейтах:':<15}{format(fahrenheit, '^15.2f')}")
    print(f"{'Температура у Кельвінах:':<15}{format(kelvin, '^15.2f')}")

celsius = float(input("Введіть температуру в градусах Цельсія: "))

convert_temperature(celsius)


def sum_of_digits(number):
    a = number // 1000       # Перша цифра
    b = (number // 100) % 10 # Друга цифра
    c = (number // 10) % 10  # Третя цифра
    d = number % 10          # Четверта цифра

    digit_sum = a + b + c + d

    print(f"{a} + {b} + {c} + {d} = {digit_sum}")

number = int(input("Введіть чотирицифрове число: "))

sum_of_digits(number)

import math

def distance_between_points(x1, y1, x2, y2):
    # Перетворення градусів в радіани
    x1_rad = math.radians(x1)
    y1_rad = math.radians(y1)
    x2_rad = math.radians(x2)
    y2_rad = math.radians(y2)

    # Обчислення відстані за формулою
    radius = 6371.032  # середній радіус Землі в кілометрах
    distance = radius * math.acos(
        math.sin(x1_rad) * math.sin(x2_rad) + 
        math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad - y2_rad)
    )
    
    # Виведення результату з форматуванням
    print(f"{'Відстань:':<10}{format(distance, '>10.3f')} км")

# Координати Пекіна і Києва
beijing_lat = 39.9075000
beijing_lon = 116.3972300
kyiv_lat = 50.4546600
kyiv_lon = 30.5238000

# Викликаємо функцію для обчислення відстані
distance_between_points(beijing_lat, beijing_lon, kyiv_lat, kyiv_lon)

# Координати Токіо і Києва
tokio_lat = 35.6895000
tokio_lon = 139.6917100

# Викликаємо функцію для обчислення відстані
distance_between_points(tokio_lat, tokio_lon, kyiv_lat, kyiv_lon)

input("\nНатисніть Enter, щоб завершити програму...")
