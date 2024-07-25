import queue
import random
import time

# Функція для створення нової заявки
def generate_request(request_queue, request_id):
    request = f"Request {request_id}"
    print(f"Згенерована заявка: {request}")
    # Додати заявку до черги
    request_queue.put(request)

# Функція для обробки заявки
def process_request(request_queue):
    if not request_queue.empty():
        # Видалити заявку з черги
        request = request_queue.get()
        print(f"Обробка заявки: {request}")
        time.sleep(1)  # Імітуємо затримку для спостереження за процесом
    else:
        print("Черга пуста")

# Головний цикл програми
def main():
    # Створити чергу заявок
    request_queue = queue.Queue()
    # Ідентифікатор заявки
    request_id = 0
    try:
        while True:
            time.sleep(1)  # Імітуємо затримку для спостереження за процесом
            # Генерування нових заявок
            if random.choice([True,False]):
                request_id += 1
                generate_request(request_queue, request_id)
            
            # Обробка заявок    
            if random.choice([True,False]):    
                process_request(request_queue)

    except KeyboardInterrupt:
        print("Програма завершена")

if __name__ == "__main__":
    main()
