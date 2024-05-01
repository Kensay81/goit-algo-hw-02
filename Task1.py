from queue import Queue
import time
import random

queue = Queue()

# Функція для генерації нової заявки та її додавання до черги
def generate_request():
    num_requests = random.randint(0, 10)  # Випадкова кількість заявок від 0 до 10
    for i in range(num_requests):
        request_number = len(queue.queue) + 1  # Створюємо унікальний номер для заявки
        request = f"Request {request_number}"  # Генеруємо заявку
        queue.put(request)  # Додаємо заявку до черги
        print(f"Нова заявка: {request}")

# Функція для обробки заявок
def process_request():
    if not queue.empty():
        request = queue.get() 
        print(f"Обробка заявки: {request}")
    else:
        print("Черга пуста")

# Головний цикл програми
while True:
    generate_request()  # Генерація нових заявок
    process_request()  # Обробка заявок
    
    # Запит користувача на вихід з програми
    exit_choice = input("Для виходу натисніть 'q', для продовження натисніть Enter: ")
    if exit_choice.lower() == 'q':
        print("Вихід з програми...")
        break  
    
    time.sleep(1)  
